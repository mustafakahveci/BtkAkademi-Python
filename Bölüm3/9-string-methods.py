message = "Hello There. My name is Mustafa Kahveci"

print(message.upper())  #büyük harf yapar
print(message.lower())  #küçük harf yapar
print(message.title())  #her kelimenin ilk harfini büyük yapar
print(message.capitalize()) #stringin ilk harfini büyük diğerlerini küçük yapar.
print(message.strip())   #en baştaki boşluk karakterini kaldırır
print(message.split())  #boşluk karakterlerinden itibaren ayırıp diziye atar
print(message.split(".")) #noktadan itibaren ayırır

index= message.find("Mustafa")    #karakter hangi indexte
print(index)

print(message.startswith("H"))  #H ile başlıyor mu
print(message.endswith("i"))  #H ile bitiyor mu

print(message.replace("There","guys"))  #There yazısını guys ile değiştir

