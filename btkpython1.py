# Customer information
import datetime

customerName = "john"
customerSurname = "patrick"
customerFullName = customerName +' '+ customerSurname
customerGender = True #Male
customerId = "82934910031"
customerBirthday = 1995
customerAddress = "xxxx-xxxx-xxxx"
currentYear = datetime.datetime.now().year
customerAge = currentYear - customerBirthday
print(customerAge)

# Circle calculation
r = float(input("radius : " ))
pi = 3.14
circleArea = pi * r**2
circleEnvironment = 2*pi * r**2
print("area : " , str(circleArea))
print("environment : ", str(circleEnvironment))


# string format.py
name= "xxx"
surname = "yyy"
age = "00"
print("my name is {} {} and I'm {} years old " .format(name, surname, age))


# string exercise

website = "https://baykartech.com/tr/"
course = "python course: python guide programming from zero 40 hours"

# course length
courseLength = len(course)
print(courseLength)

# choose https character into the website

websiteInHttps = website[0:5]
print(websiteInHttps)

# choose com character into the website
websiteInCom = website[-7:-4]
print(websiteInCom)

# choose first and last 15th character

courseCharacter = course[0:15]
courseCharacter = course[:15]
courseCharacter = course[-15:]

# String method

message = "hello world"
message = message.upper()
message = message.lower()
message = message.title() 
message = message.capitalize()
message = message.strip() #baş sondaki karakterleri siler
index = message.find("hello")
isFound = message.startswith("H")
isFound2 = message.endswith("j")
replace = message.replace("hello","Hi")
print(isFound)
print(isFound2)
print(index)
print(replace)


# training part 2 

web_site = "https://www.google.com"
web_site_name = "  google homepage " 

strip = web_site_name.strip()
print(strip)
stripLeft = web_site_name.lstrip()
print(stripLeft)
smallText = web_site_name.lower()
print(smallText)
countO = web_site_name.count("o")
print(countO)
websiteStart = web_site_name.startswith("www")
print(websiteStart)
webFind = web_site_name.find("com")
print(webFind)
result = "contents".center(50, "*")
print(result)
changeCharacter = result.replace("*","_")
print(changeCharacter)



# LIST TRAINING 

carList = ["bmw", "mercedes", "opel", "mazda"]
print(len(carList))
ilkEleman = carList[0]
sonEleman = carList[-1]
print(ilkEleman, sonEleman)
# mazdayı toyota ile değiştirin
carList[-1] = "toyota"
print(carList)
# mercedes listeye dahil mi
Mercedes = "mercedes" in carList
print(Mercedes)
# ilk 3 aracı seç
betweenValue = carList[0:3]
print(betweenValue)
# son 2 elemanı seç
lastTwoCar = carList[-2:] = ["toyota", "renault"]
print(lastTwoCar)
addCar = carList + ["audi","nissan"]
print(addCar) 
# delete last car
del carList[-1]
print(carList)
# tersten yazdır
ters = carList[::-1]
print(ters)

# liste yazdırma
studentA = ["yiğit", "bilgi",2010,[53,67,67]]
studentB = ["ahmet", "bilgi",2013,[43,37,47]]
studentC = ["osman", "bilgi",1009,[73,67,57]]

listeler = (studentA + studentB + studentC )
print(listeler)

# or

listleYapısı = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalamsı {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}           "
print(listleYapısı)


# LİSTE METOT ÇALIŞMASI
names = ["ali" , "yağmur" , "hakan", "deniz"]
years = [1998,2000,1998,1987]
names.append("cenk")
# liste basına ekleme
names.insert(0,"sena")
names.remove("deniz")
# indeksini bulma
index = names.index("ali")
print(index)

# ali listede var mı
find = "ali" in names
print(find)

# liste eleman ters çevir
names.reverse()

# liste elemanı alfabetik sırala
names.sort()

# years listesini rakamsal büyüklüğe göre sırala
years.sort()
print(years)

# kaç tane 1998 vardır
howManyYears = years.count(1998)
print(howManyYears)

# tüm eleman silme
years.clear()

# kullanıcıdan marka al liste yap
marka1 = input("marka: ")
marka2 = input("marka: ")
marka3 = input("marka: ")


markalar= [marka1 , marka2 , marka3]
print(markalar)



# TUPLE

normalList = [1,2,3]
tupleList = (1,"iki",3)
# tuple list is not changing!
tupleList.append(44)
print(tupleList)



# DICTIONRY(key,value)

plakalar = {"eskişehir" : 14 , "istanbul" : 34 , "bursa" : 16}
print(plakalar["eskişehir"])

plakalar["bartın"] = 74
print(plakalar)

users={
  "enes":{
          "age":22,
          "gender":"Male",
          "email":"asdasd@gmail.com",
          "phone":"432334"
      
      
      },
  "osman":
  {
          "age":24,
          "gender":"Male",
          "email":"aascczd@gmail.com",
          "phone":"4334095"
   
   }
  }

print(users["enes"]["age"])


# DICTIONARY EXAMPLE
students = {
"120": {
    "name": "ali",
    "surname": "yılmaz",
    "age": 22
},
"111": {
    "name": "osman",
    "surname": "kılıc",
    "age": 22
},
"132": {
    "name": "haydar",
    "surname": "ogut",
    "age": 25
}
}

# number verisini al ve students a ekle
students={}
number = input("lütfen numaranı gir:")
name = input("lütfen ad gir:")
surname= input("lütfen soyad gir:")
age =int(input("lütfen yaş gir:"))
students.update(
    {
        number:
            {
                "ad":name,
                "soyad": surname,
                "yaş":age
                }
        
    
    })

print(students)


# set kavramı

fruits ={"orange",,"apple","banana"}
# print(fruits[0]) bu şekilde indeks alınamaz 

for x in fruits:
print(x)
fruits.add("cherry")
fruits.update(["mango","grape"])
prints(fruits)    


#  VALUE TYPES --> string,number

x = 5
y=25
x=y
y=10
print(x,y)

# REFERENCE TYPES -->list

a = ["apple","banana"]
b = ["hgj","banana"]
a=b
b[0]="grape"
print(a,b)


# atama operator egzersiz

x,y,z = 2,5,10
toplam= x+y+z
mumbers = 1,5,7,10,6
kullaniciDegeri = input("deger giriniz:")
kullaniciDegeri = int(kullaniciDegeri)
islem = kullaniciDegeri-toplam
print("islem farkı:",islem)
kalnsizBolme = y//x
toplamMod =toplam%3
 

# karşılaştırma operatörü

a = int(input("sayı giriniz:"))
b = int(input("sayı giriniz:"))
if a>b:
    
     print("a b den büyüktür")
     
else:
    print("b a dan büyüktür")
     

vize1 = int(input("vize 1 : "))
vize2 = int(input("vize 2 : "))
final = int(input("final : "))
ortalama = (vize1 + vize2 )*0.3 + (final*0.6)
if ortalama<50:
    print("kaldın" , ortalama)
else:
    print("geçtin", ortalama)
    

girilenSayi = int(input("sayi giriniz"))
if girilenSayi%2==0 and girilenSayi!=0:
    print("girilen sayi çift", girilenSayi)
elif girilenSayi%2==1:
    print("girilen sayi tektir", girilenSayi)
elif girilenSayi==0:
    print("girilen sayı sıfırdır" , girilenSayi)
    

girilenSayi2 = int(input("sayi giriniz:"))
if girilenSayi2>0:
    print("girilen sayi pozitiftir", girilenSayi2)
elif girilenSayi2<0:
    print("girilen sayi negatiftir", girilenSayi2)
elif girilenSayi2==0:
    print("girilen sayi nötr", girilenSayi2)


email = "email@sadikturan.com"
password = "abc123"
userEmail = input("lütfen email adresinizi giriniz : ")
userPassword = input("lütfen şifreinizi giriniz ")
if userEmail==email and password == userPassword:
    print("hoşgeldiniz ")
elif userEmail ==email and password !=userPassword:
    print("kullanıcı adı veya şifre yanlış ")
elif userEmail !=email and password ==userPassword:
    print("kullanıcı adı veya şifre yanlış ")
else:
    print("kullanıcı adı veya şifre yanlış ")




# IDENTITY(is operator) (2 nesne aynı bellek adresinde mi?)
x =[1,2,3]
y= [1,2,3]
print(x is y)
z=x
print(x is z)

# Membership operator : in

x = ["apple", "banana"]
print("banana" in x)
name ="çınar"
print("a" in name)
print("a" not in name)


# ELSE İF ALIŞTIRMA

name = input("isiminiz : ")
age = input("yaşınız : ")
education = input("eğitim durumu: ")

if(age>=18) and (education=="lise") or egitim=="üniversite":
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet alamaz")

import datetime

tarih = input("aracaınız hangi tarihte trafiğe çıktı (YYYY/MM/DD):")
tarih = tarih.split("/")
print(tarih[0])
print(tarih[1])
print(tarih[2])

trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[1]))
simdi=datetime.datetime.now()
simdi = datetime.datetime.now()
fark = simdi-trafigecikis
print(fark)


days = input("aracınız kaç gündür trafikte")

if days<=365:
    print("1.servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı")
elif days>365*2 and days<=365*3:
    print("2.servis aralığı")
else:
    print("hatalı süre")
    
























