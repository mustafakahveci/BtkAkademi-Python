website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

"""
1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki diğer karakterleri silin.

3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapin

4- website içinde kaç tane a karakteri vardir? (count)

5- website 'www' ile başlayip com ile bitiyor mu?

6- website içinde '.com' ifadesi var mi ? 

7- course içindeki karakterlerin hepsi alfabetik mi ? (isaplha,isdigit)

8-contents ifadesini satirda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

9- course karakter dizinindeki tüm boşluk karakterlerini - ile değiştirin

10- Hello World karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

11- course karakter dizisini boşluk karakterlerinden ayirin.



"""


#1
message = ' Hello World '
print(message.strip())

#2
print(website.strip("htp:/w.com"))

#3
print(course.lower())

#4
print(website.count('a'))

#5
print(website.startswith("www"))
print(website.endswith("com"))

#6
print(website.find(".com"))

#7
print(course.isalpha())

#8
word = "Contents"
print(word.center(50,"*"))

#9
print(course.replace(" ","-"))

#10
word2 = "Hello World"
print(word2.replace("World","There"))

#11
print(course.split(" "))