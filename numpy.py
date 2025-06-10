import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]


# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))


py_multi = ([1,2,3], [4,5,6], [7,8,9])
np_multi = np_array.reshape(3,3)
print(py_multi)

print("array dizinin boyutu:",np_array.ndim)
print("multi dizinin boyutu:",np_multi.ndim)

print(np_array.shape)
print(np_multi.shape)

#numpy dizileri ile çalışma
result = np.arange(10,100,3)
#sadece sıfırlardan olusan dizi 
result = np.zeros(10)
#birlerden olusan dizi
result = np.ones(10)
#belirli aralıkta artışa sahip dizi
result = np.linspace(0,100,5)
#random
result = np.random.randint(0,10)
#rastgele sayı atama
result = np.random.randint(0,10)
#rastgele 3 sayı ata
result = np.random.randint(0,10,3)
#eksili rastgele 5 sayı atama
result = np.random.randn(5)
#5 e 10 luk matris olustur
result= np_array.reshape(3,3)
#empty 3 elemanlı farklı bir numpy dizisi olusturur. diziyi hızlıca doldurur.
result = np.empty(3)
print(result)


#Dizilerin indekslenmesi

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[:3]
result = numbers[3:]
result = numbers[::]
print(result)

numbers2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
result = numbers2[0]
result = numbers2[2]
result = numbers2[0,2]
result = numbers2[1,2]
result = numbers2[:,2]
result = numbers2[:,0:2]
result = numbers2[-1,:]
print(result)


arr1 = np.arange(0,10)
#arr2 = arr1 #referans
arr2= arr1.copy()
arr2[0]=20
print(arr2)
print(arr1)


#Numpy Dizi operasyonları

num1 = np.random.randint(10,100,6)
num2 = np.random.randint(10,100,6)

print(num1)
print(num2)

result = num1+ num2 #karsılıklı değerleri toplar
result = num1 - num2 #iki kümeyi birbirinden cıkarır
result = num1+ 10 # tüm değerlere 10 ekler
result = np.sin(num1)
result = np.cos(num1)

multinumbers = num1.reshape(2,3)
print(multinumbers)
print(result)

#Numpy Uygulamalar

# (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturun

array1 = np.array([10,15,30,45,60])
print(array1)

# (5-15) arasındaki sayılarla numpy dizisi olusturun
array2 = np.arange(5,15)
print(array2)
 
# (50-100) arasında 5 er 5 er artarak numpy dizisi oluştur
array3 = np.arange(50,100,5)
print(array3)

# 10 elemanlı sıfırlardan oluşan bir dizi olusturun
array4 = np.zeros(10)
print(array4)

# 10 elemanlı birlerden oluşan bir dizi olusturun
array5 = np.ones(10)
print(array5)

# (0-100) arasında eşit aralıklı 5 sayı üretin
array6 = np.linspace(0,100,5)
print(array6)

#10-30 arasında rastgele 5 tane tamsayı üretin
array7= np.random.randint(10,30,5)
print(array7)

# -1 ile 1 arasında 10 adet satı üretin
result = np.random.randn(10)
print(result)

# 3x5 boyutlarında 10-50 arasında rastgele bir matris olusturun
matris= np.random.randint(-10,50,15).reshape(3,5)
print(matris)

#üretilen matrisin satır ve sütun sayıları toplamlarını hesapla
rowTotal= matris.sum(axis = 1)
colTotal= matris.sum(axis = 0)
print(rowTotal)
print(colTotal)

# üretilen matrisin en büyük ve en küçük değeri ve ortalamsı nedir
maxVal = matris.max()
minVal = matris.min()
average= matris.mean()
print(maxVal)
print(minVal)
print(average)

#üretilen matrisin en büyük değerinin indeksi kaçtır?
argMax = matris.argmax()
argMin = matris.argmin()
print(argMax)
print(argMin)

# 10 20 arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz
arr = np.arange(10,20)
print(arr)

result= arr[0:3]
print(result)

#üretilen dizinin elemanlarını tersten yazdırın
result = arr[::-1]
print(result)

# üretilen matrisin ilk satırını seçin
result= matris[0]
print(result)

#üretilen matrisin 2.satır ve 3.sütundaki elemanı seçiniz
result= matris[1,2]
print(result)

# üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
result = matris[:,1]
print(result)

# üretilen matris elemanlarının hangisi pozitif çift sayıdır
cift= matris[matris % 2==0]
result = cift[cift>0]
print(result)
