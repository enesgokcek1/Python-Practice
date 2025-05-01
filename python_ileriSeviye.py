#Exchange api

import requests
import json

api_key = "2cc7174d248dfa64c19dfd73"
api_url = f"https://v6.exchangerate-api.com/v6/2cc7174d248dfa64c19dfd73/latest/"

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alinan döviz türü: ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdumrak istiyorsunuz: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, sonuc_json ["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
