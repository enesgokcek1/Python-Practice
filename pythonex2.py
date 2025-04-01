# Math Module 

import math

value = dir(math)
value = help(math)  #destek için detay verir
value = help(math.floor)
value = math.factorial(49)
value = math.floor(5.8)
print(value)

# # or math adını değişebilirsin
# import math is islem
# value = islem.floor(49)


# from math import * ile direkt kütüphane içindekilere ulaşabilirsin
# value = factroial(5) gibi

# from math import factorial,sqrt, floor gibi spesifik seçebilirsin


# Random modül kullanımı

import random

result = dir(random)
result = help(random)
result = random.random()
result = int(random.uniform(1, 100)) #1-100 arası üretir
result = random.randint(1, 100) #int 1-100 sayı üretir
names = ["ali","ahmet","aslı","efe","cihat"]
result = names[random.randint(0, len(names)-1)]
result = random.choice(names)#bi üst satırdakinin hazır hali
print(result)


liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 3)
print(result)


 # error handling: kullanıcın yapabileceği olası hatalara cevap yazıyoruz
 
# try:
#       x = int(input("x:"))
#       y = int(input("y:"))
     
# except ZeroDivisionError:
#     print("y için 0 girilemez")
# except ValueError:
#     print("x ve y için sayısal değer gir")

 
# try:
#       x = int(input("x:"))
#       y = int(input("y:"))
     
# except:
#     print("yanlış bilgi girdiniz")

while True:
    try:
        x = int(input("x:"))
        y = int(input("y:"))
        print(x/y)
    except Exception as ex:
        print("yanlış bilgi girdiniz", ex)
    else:
        break
    finally:
        print("try exception sonlandı")


# EXCEPTION RAISE

x = 10
if x > 5:
    raise Exception("x 5 den büyük değer alamaz")


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir")

password = "asd213aas"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola: ", password)
finally:
    print("validayion tamamlandı")
    
    
# ERROR HANDLING EXAMPLE

liste = ["1","2","5a","10b","abc","10","50"]

# liste elemanları içinden sayısal değerleri bulunuz

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue


# kullanıcı q değerini girmedikçe aldığınız her inputun 
# sayısal olduğundan emin olunuz aksi taktirde hata mesajı yazın

while True:
    sayi = input("sayı:")
    if sayi == "q":
        break    
    try:
        result = float(sayi)
        print("girdiğiniz sayı:", result)
    except ValueError:
        print("geçersiz sayı")
        continue
    



# girilen parola içinde türkçe karakter hatası verin

turkce_karakterler = "şçğüöıİ"

parola = input("parola giriniz:")

for i in parola:
    if i in turkce_karakterler:
        raise TypeError("parola türkçe karakter içeremez")
    else:
        pass
        
print("geçerli parola : " , parola)
   


# NOT UYGULAMASI
def not_hesapla(satir):
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1]
    not1= notlar[0]
    not2= notlar[1]
    not3= notlar[2]
    ortalama = (not1 + not2 + not3)/3
    
    



def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
            
def not_gir():
    ad = input("öğrenci adı:")
    soyad = input("öğrenci soyad:")
    not1 = input("öğrenci not:")
    not2 = input("öğrenci not2:")
    not3 = input("öğrenci not3:")
    
    with open("sinav_notlari.txt", "a",encoding="utf-8") as file :
        file.write(ad+ " " + soyad + " : " + not1+ "," + not2+ " , " +not3+ "\n" )
        
        
        
def notları_kayitet():
    with open ("sinav_notları.txt", "r", encoding="utf-8") as file:
        liste = []
        
        for i in file:
            liste.append(not_hesapla(i))
            
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
    
while True:
    islem=input("1-notları oku\n2 - Not Gir\n3- Notları Kayıt et\n4- Çıkış\n ")
    
    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem =="3":
        notları_kayitet()
    else:
        break
        
        
# encapsulation

def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1 
    num2= inner_increment(num1)
    print(num1,num2)

outer(10)



# iterators

liste = [1,2,3,4,5]

for i in liste:
    print(i)
    
print(dir(liste))

iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
    
    
    
class MyNumbers:
    def __iter__(self,start,stop):
        self.start = start
        self.stop = stop
    
    def next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1 
            return x 
        else: 
            raise StopIteration
            
list = MyNumbers(20,50)

for x in list:
     print(x)
    
    
# İterator için generators lazım.bellekte yer işgal etmeyen itarator açar

def cube():
    
    for i in range(5):
        yield i **3 # yield ile tek kullanımlık değer atar 

    for i in cube():
        print(i)

print(cube())


    
# Datetime modülü


# from datetime import datetime
# from datetime import date
# from datetime import time
# bu şekilde spesifik bir özelliği de çağırabiliriz



import datetime
result = dir(datetime.datetime) # dir fonksiyonu, bir nesnenin veya modülün sahip olduğu tüm nitelikleri listemeleye yarar
result = dir(datetime.date)
print(result)

# or

from datetime import datetime

simdi = datetime.now()
month = datetime.now().month
day = datetime.now().day
stringDateTime = datetime.ctime(simdi)

print(simdi)
print(month)
print(day)
print(stringDateTime)

birthday = datetime(1983,5,9)
result = datetime.timestamp(birthday)
print(birthday)
print(result)



# OS modülü

import os

result = dir(os)
result = os.name

print(result)


# RE modül(regular expression)


import re

result = dir(re)

print(result)

str = "python kursu : python programlama rehberi "

# re.findall() arama

result = re.findall("python", str)
result = len(result)

# re.split() listelere bölme

result = re.split(" ", str)

# re.sub() değiştirme
result = re.sub(" ", "-", str)

# re.search()
result = re.search("python", str)

    
