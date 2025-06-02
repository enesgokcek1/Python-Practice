import requests
from bs4 import BeautifulSoup
import json

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# ld+json script etiketini al
json_ld_script = soup.find("script", type="application/ld+json")

if json_ld_script:
    data = json.loads(json_ld_script.string)

    # data içindeki 'itemListElement' listesini al
    film_listesi = data.get("itemListElement", [])

    # İlk 10 filmi yazdır
    for film in film_listesi[:10]:
        item = film.get("item", {})
        ad = item.get("name", "Film adı yok")
        puan = item.get("aggregateRating", {}).get("ratingValue", "Puan yok")
        print(f"{ad}: {puan}")
else:
    print("JSON formatında veri bulunamadı.")



# N11 Web scraping

import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/masaustu-bilgisayar"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15"
    
    }

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html,"html.parser")

liste = soup.find_all("li", {"class":"column"}, limit = 10)

for li in liste:
    link = li.a.get("href")
    p_name = li.a.h3.text
    images = li.find("img",{"class":"cardImage"}).get("data-images").split(",")
    price = li.find("div", {"class":"priceContainer"}).ins.text
    
print(f"ürün ismi {p_name} resmi {images} fiyatı {price}")


#Bot Yazımı (Selenium)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Safari sürücüsünü başlat
driver = webdriver.Safari()


url = "http://github.com"
driver.get(url)

# Sayfa yüklenene kadar bekle
WebDriverWait(driver, 10).until(EC.title_contains("GitHub"))


driver.maximize_window()


driver.save_screenshot("github-homepage.png")


url = "http://github.com/enesgokcek1"
driver.get(url)


print(driver.title)

# Sayfa yüklenene kadar bekle
WebDriverWait(driver, 10).until(EC.title_contains("enesgokcek1"))


driver.back()

# Geri gitme işlemi tamamlanana kadar bekle
WebDriverWait(driver, 10).until(EC.title_contains("GitHub"))

# Kapanmadan önce 2 saniye bekle
time.sleep(2)


driver.close()

#Selenium ile sayfa etkileşimi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Safari driver'ı başlatıyoruz
driver = webdriver.Safari()

# Sayfayı açıyoruz
driver.get("https://www.hepsiburada.com")
time.sleep(2)

# Class adı ile arama kutusunu buluyoruz
search_input = driver.find_element(By.XPATH, '//*[@id="SearchBoxOld_ecef953b-b527-4f40-8f16-5a78ce04731d"]/div/div/div/div')


# Arama kutusuna 'python' yazıyoruz
search_input.send_keys("python")
time.sleep(1)

# Enter tuşuna basıyoruz
search_input.send_keys(Keys.ENTER)
time.sleep(2)

# Tarayıcıyı kapatıyoruz
driver.close()





























