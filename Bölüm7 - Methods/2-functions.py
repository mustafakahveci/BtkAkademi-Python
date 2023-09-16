def sayHello():
    print("Hello")

def sayHelloPerson(name = "user"):
    print("Hello " + name)

def sayHelloPersonReturn(name = "user"):
    return "Hello " + name 

sayHello()
sayHelloPerson()
sayHelloPerson("Mustafa")

message = sayHelloPersonReturn("Mustafa")
print(message)


def total(num1,num2):
    return num1+num2

result = total(10,20)
print(result)

result = total(12,45)
print(result)

def yasHesapla(dogumYili):
    return 2023 - dogumYili

ageMustafa = yasHesapla(2000)
ageCinar = yasHesapla(2006)

print(ageMustafa)
print(ageCinar)

def emekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRING: Doğum yılınıza göre emekliliğine kaç yıl kaldı.
    Input:Doğum yılı
    Output: emekliliğe kalan süre
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if(emeklilik > 0):
        print(f"{isim} emekliliğine {emeklilik} yıl kaldı.")
    else:
        print(f"{isim} zaten emeklisin.")


emekliligeKacYilKaldi(2000,"Mustafa")
emekliligeKacYilKaldi(1987,"Ali")
emekliligeKacYilKaldi(1954,"Ahmet")

