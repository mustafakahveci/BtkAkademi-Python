# 1- Girilen iki sayıdan hangisi büyüktür ? 

sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

print(f"{sayi1} değeri {sayi2} değerinden büyük müdür ? = {sayi1 > sayi2}")


# 2- Kullanıcıdan vize (%40) ve final (%60) notunu alıp ortalama hesaplayınız.

vize = int(input("Vize sonucunuzu giriniz : "))
final = int(input("Final sonucunuzu giriniz : "))
print(f"Ortalamanız : {(vize * (0.4)) + (final * (0.6))}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın. 

number = int(input("Sayı giriniz : "))
print(f"Sayı çift mi ? : {number%2 == 0}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

sayi = int(input("Sayı giriniz : "))
print(f"{sayi} poziif midir ? = {(sayi > 0)}")


# 5- Parola ve e-mail bilgisini isteyip doğruluğuunu kontrol ediniz. (email: email@gmail.com - parola: abc123)

email = "email@gmail.com"
parola = "abc123"

input_email = input("e-mail giriniz : ")
input_parola = input("parola giriniz : ")

print(f"Girilen email bilgisi doğru mu ? = {email == input_email}")
print(f"Girilen parola bilgisi doğru mu ? = {parola == input_parola}")

