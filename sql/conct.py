import mysql.connector
from datetime import datetime
from connection import mydb  # Bağlantı objesi ayrı dosyadaysa bu doğrudur

class Student:
    connection = mydb
    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname, birthday, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender

    def save(self):
        sql = "INSERT INTO Student(studentNumber, Name, Surname, Birthday, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = (self.studentNumber, self.name, self.surname, self.birthday, self.gender)
        try:
            Student.mycursor.execute(sql, values)
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)

# Öğrenci listesi
students = [
    Student("101", "Ahmet", "Yılmaz", datetime(2005, 5, 7), "E"),
    Student("102", "Ali", "Yılmaz", datetime(2002, 5, 7), "E"),
    Student("103", "Ayşe", "Yılmaz", datetime(2006, 5, 7), "K"),
    Student("104", "Zeynep", "Yılmaz", datetime(2001, 5, 7), "K"),
    Student("105", "Gülenay", "Yılmaz", datetime(2003, 5, 7), "K"),
]

# Öğrencileri veritabanına kaydet
for ogrenci in students:
    ogrenci.save()

# Bağlantıyı kapat
Student.connection.close()




