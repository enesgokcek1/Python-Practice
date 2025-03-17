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
















