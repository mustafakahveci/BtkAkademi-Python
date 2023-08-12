"""
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol
   ediniz.
"""

num1 = float(input("sayıyı giriniz : "))

if(num1>0 and num1<100):
    print(f"{num1}, 0-100 arasındadır...")
else:
    print(f"{num1}, 0-100 arasında değildir...")




"""
2- Girilen bir sayının pozitif çift sayı olup olmadığını 
   kontrol ediniz.
"""

num2 = int(input("sayıyı giriniz : "))

if(num2 % 2 == 0):
    print(f"{num2}, çift sayıdır.")
else:
    print(f"{num2}, tek sayıdır.")




"""
3- Email ve parola bilgileri ile giriş kontrolü yapınız.
"""

email = "kahvecimstfa@gmail.com"
password = "123456789"

enteredEmail = input("E-mail adresinizi giriniz : ")
enteredPassword = input("Şifrenizi giriniz : ")

if(email == enteredEmail and password == enteredPassword):
    print("Giriş işlemi başarılı")
else:
    print("E-mail ya da şifre yanlış !!!")




"""
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
"""

sayi1 = int(input("1. sayiyi giriniz : "))
sayi2 = int(input("2. sayiyi giriniz : "))
sayi3 = int(input("3. sayiyi giriniz : "))

if(sayi1 > sayi2 and sayi1 > sayi3):
    print(f"{sayi1} en büyük sayıdır.")
elif(sayi2 > sayi1 and sayi2 > sayi3):
    print(f"{sayi2} en büyük sayıdır.")
elif(sayi3 > sayi1 and sayi3 and sayi2):
    print(f"{sayi3} en büyük sayıdır.")
else:
    print("En büyük en az iki sayı var")




"""
5- Kullancıdan 2 vize(%60) ve final(%40) notunu alıp ortalama
   hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse
   kaldı yazdırın.
   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
"""

vize1 = int(input("1. vize notunuzu giriniz : "))
vize2 = int(input("2. vize notunuzu giriniz : "))
final = int(input("Final notunuzu giriniz : "))

ort = vize1 * (0.3) + vize2 * (0.3) + final * (0.4)

if(final >= 70):
    if(ort < 50):
        print(f"Ortalamanız : {ort} - Final notunuz : {final} ")
        print("Final notu ile geçtiniz...")
    elif(ort >= 50):
        print(f"Ortalamanız : {ort} - Final notunuz : {final} ")
        print("Final notu ve ortalama ile geçtiniz...")
elif(ort > 50):
    if(final < 50):
        print(f"Ortalamanız : {ort} - Final notunuz : {final} ")
        print("Ortalamanız yeterli fakat final notunuzdan dolayı kaldınız")
    elif(final >= 50):
        print(f"Ortalamanız : {ort} - Final notunuz : {final} ")
        print("Dersi geçtiniz...")
else:
    print(f"Ortalamanız : {ort} - Final notunuz : {final} ")
    print("Dersten kaldınız...")




"""
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini 
   hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
   0 - 18.5  => Zayıf
   18.5 - 25 => Normal 
   25.0 - 30 => Fazla Kilolu
   30+       => Şişman (Obez)
"""

name = input("adınızı giriniz : ")
kilo = int(input("kilonuzu giriniz: "))
boy = float(input("boyunuzu giriniz (1.82m): "))

bmi = kilo / (boy ** 2)

if(bmi > 0 and bmi < 18.5):
    print(f"Vücut kitle indeksiniz : {bmi} ==> Zayıf ")
elif(bmi >= 18.5 and bmi <25):
    print(f"Vücut kitle indeksiniz : {bmi} ==> Normal ")
elif(bmi >= 25 and bmi < 30):
    print(f"Vücut kitle indeksiniz : {bmi} ==> Fazla Kilolu ")
else:
    print(f"Vücut kitle indeksiniz : {bmi} ==> Şişman(Obez) ")