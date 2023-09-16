def changeName(n):
    n = "ada"

name = "Yiğit"
changeName(name)
print(name)

#isim değiştirilmez.




def change(n):
    n[0] = "istanbul"

sehirler = ["ankara" , "izmir"]
change(sehirler)
print(sehirler)

#değiştirilir içerik 








def add(*params):
    return sum((params))

print(add(10,20))
print(add(10,20,30))
print(add(10,20,40,50))
print(add(10,20,5,7,9,5,5,2,))
print(add(10))

def add(*params):
    sum = 0
    for i in params:
        sum += i
    return sum

# "*" tuple tipinde parametreleri alır.
#sum metodu kullanmadan




def displayUser(**args):
    for key, value in args.items():
        print("{} is {}".format(key,value))

displayUser(name="Çinar", age = 2, city= "istanbul")
displayUser(name="Ada", age = 12, city= "kocaeli", phone="13146456")
displayUser(name="Çinar", age = 2, city= "istanbul", phone="56462234")

# "**" dictionary tipinde parametreleri alır.






def myFunc(a,b,c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70, key1="value1", key2="value2")


