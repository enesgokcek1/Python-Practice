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


 