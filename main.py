#1-misol
numbers = (15, 8, 22, 3, 19)
katta = max(numbers)
print(katta)

2-misol
numbers = (4, 9, 16, 25, 36)

#1-misol
bow_lugat = dict()
print(bow_lugat)

#2-misol
talaba = {"ism": "Ali",
          "yosh": 20,
          "shahar": "Toshkent"
}
print(talaba)

#3-misol
talaba = {
    "ism": "Sardor",
    "yosh": 22,
    "shahar": "Samarqand"
}
print(talaba["ism"])

#4-misol
talaba = {
    "ism": "Nozila",
    "yosh": 14,
    "shahar": "Xorazm",
    "telefon": "+998885140605"
}
print(talaba)

#5-misol
talaba = {"ism": "Jasur",
          "yosh": 21,
          "shahar": "Namangan"
}
talaba["yosh"] = 23
print(talaba)

#6-misol
talaba = {"ism": "Dilnoza",
          "yosh": 20,
          "shahar": "Andijon",
          "kurs": 2
}
print(talaba)

del talaba["shahar"]
print(talaba)

#7-misol
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000
}
print("Kalit ro'yxati:", meva.keys())

#8-misol
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000
}
print("Qiymat ro'yxati:", meva.values())

#9-misol
kitob = {"nomi": "O'tkan kunlar",
         "muallif": "Abdulla Qodiriy",
         "yil": 1925, "sahifa": 320
}
print("Qiymat ro'yxati:", kitob.items())

#10-misol
kitob = {"nomi": "Mehrobdan chayon",
         "muallif": "Abdulla Qahhor",
         "sahifa": 280
}
if "muallif" in kitob:
    print("Muallif kitobi mavjud!")
else:
    print("Muallif kitobi mavjud emas!")

#11-misol
rang = {"qizil": "red",
        "ko'k": "blue",
        "yashil": "green",
        "sariq": "yellow",
        "qora": "black"
}
print(len(rang))

#12-misol
foydalanuvchi = {"ism": "Aziza",
                 "yosh": 25,
                 "shahar": "Farg'ona"
}
print(foydalanuvchi.get("Email", "Email topilmadi"))

#13-misol
mahsulot = {"nomi": "Telefon",
            "brend": "Samsung",
            "narx": 3500000,
            "rang": "qora"
}
ochirilgan_elem = mahsulot.pop("narx")
print(ochirilgan_elem)

#14-misol
sozlamalar = {"til": "uz",
              "rang_rejim": "tungi",
              "shrift": "14px",
              "ovoz": True
}
sozlamalar.clear()
print(sozlamalar)

#15-misol
asl_dict = {"a": 1,
            "b": 2,
            "c": 3,
            "d": 4
}
copus = asl_dict.copy()
new_als_dict = copus
print(new_als_dict)

#16-misol
maktab = {
    "10-A": {"o'quvchilar": 25, "sinf_rahbar": "Olimova N."},
    "10-B": {"o'quvchilar": 28, "sinf_rahbar": "Karimov S."},
    "11-A": {"o'quvchilar": 22, "sinf_rahbar": "Rahimova D."}
}
print(maktab)

#17-misol
maktab = {
    "10-A": {"o'quvchilar": 25, "sinf_rahbar": "Olimova N."},
    "10-B": {"o'quvchilar": 28, "sinf_rahbar": "Karimov S."}
}
sinf_oquvchilari = maktab["10-A"]
print(sinf_oquvchilari)

#18-misol
dict1 = {"a": 1,
         "b": 2,
         "c": 3
}
dict2 = {"c": 10,
         "d": 4,
         "e": 5
}
dict1.update(dict2)
print(dict1)

#19-misol
davlatlar = {"UZ": "O'zbekiston",
             "RU": "Rossiya",
             "US": "Amerika",
             "TR": "Turkiya"
}
for key in davlatlar:
    print(key)

#20-misol
baholar = {"Matematika": 5,
           "Fizika": 4,
           "Kimyo": 5,
           "Biologiya": 4,
           "Tarix": 5
}
for key, qiymat in baholar.items():
    print(key, ":", qiymat)

#21-misol
shaxs = {"ism": "Jamshid", "yosh": 21, "shahar": "Xorazm"}
print(shaxs)
shaxs.setdefault("kasb", "Talaba")
print(shaxs)

#22-misol
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

dict1.update(dict2)
dict1.update(dict3)
print(dict1)

#23-misol
talaba = {
    "ism": "Nodira",
    "familiya": "Rahimova",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturiy injiniring",
    "stipendiya": True
}

#24-misol
narxlar = {
    "Non": 3000,
    "Sut": 9000,
    "Tuxum": 18000,
    "Go'sht": 85000,
    "Yog'": 45000,
    "Sabzi": 7000
}
print(narxlar["Go'sht"])

#25-misol
matn = "salom dunyo salom python python python dunyo"
soz = matn.split()
natija = {}

for soz in soz:
    if soz in natija:
        natija[soz] += 1
    else:
        natija[soz] = 1

print(natija)

#1-misol
numbers = [12, -5, 7, -3, 0, 25, -11, 8]
print(numbers)

for el in numbers[:]:
    if el < 0:
        numbers.remove(el)

print(numbers)

#2-misol
numbers = [45, 12, 78, 3, 56, 89, 23]
katta = max(numbers)
print("Eng katta son:",katta)

kicci = min(numbers)
print("Eng kichik son:",kicci)

#3-misol
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[::-1])

#4-misol
numbers = [14, 7, 22, 9, 31, 18, 5]

#5-misol
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print()
list3 = list1 + list2
print(list3)

list3 = set(list3)
print(list3)

list3 = list(list3)
print(list3)

#6-misol
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))

#7-misol
numbers = [5, 3, 7, 3, 9, 3, 1]
print(numbers.count(3))

#9-misol
numbers = [29, 10, 14, 37, 13]

numbers.sort(reverse=False)
print(numbers)

#10-misol
numbers = [4, 6, 2, 6, 8, 4, 6, 2]
print(numbers.count(6))

#11-misol
words = ["python", "java", "c++", "golang"]
print(words)

words = [word.upper() for word in words]

print(words)

#13-misol
numbers = [100, 200, 300, 400]
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

#14-misol
roy = []
for i in range(6):
    x = int(input("son kiriting: "))
    if x >= 0:
        roy.append(x)

print(roy)

#15-misol
words = ["apple", "banana", "kiwi", "strawberry"]
m = max(words, key=len)
print(m)


#1-misol
numbers = (15, 8, 22, 3, 19)
katta = max(numbers)
print(katta)

#21 Qoshish natijasi
def qoshish (a,b):
    return a+b

res =qoshish (11,5)
print (res)
