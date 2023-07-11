website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

"""
     1- 'course' karakter dizininde kaç karakter bulunmaktadir ? 
     2- 'website' içinden wwww karakterlerini alin.
     3- 'website' içinden com karakterlerini alin.
     4- 'course' içinden ilk 15 ve son 15 karakterlerini alin
     5- 'course' ifadesindeki karakterleri tersten yazdirin.

"""

#1
print(len(course))

#2
print(website[7:10])

#3
print(website[-3:])

#4
print(course[:15]) #ilk 15
print(course[-15:]) #son 15

#5
print(course[::-1])


name, surname, age, job = "Bora","Yilmaz", 32,"mühendis"

"""
   6- Yukaridaki verilen değişkenler ile ekrana aşağidaki ifadeyi yazdirin.
   "Benim adim Bora Yilmaz, yaşim 32 ve mesleğim mühendis."

   7-"Hello world" ifadesindeki w harfini 'W' ile değiştirin.

   8-abc ifadesini yan yana 3 defa yazdirin.

"""

#6 
print(f"Benim adim {name} {surname}, yaşim {age} ve mesleğim {job}")

#7
word = "Hello world"
word = word[0:6]+'W'+ word[7:]
print(word)

#8

word2 = "abc "
print(word2*3)






