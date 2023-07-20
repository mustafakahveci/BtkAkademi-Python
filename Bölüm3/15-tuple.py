list = [1, 2, 3]

tuple = (1, "iki", 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ["ali", "veli"]
tuple = ("damla", "ayşe")

print(list)
print(tuple)

list[0] = "ahmet"
#tuple[0]= "deniz"   #hata verir "tuple" değerlere atama yapılamaz.
 
names = ("demet", "emel") + tuple

print(names)

# !!tuple da listden farklı olarak elemanlar üstünde güncelleme yapılamaz.

# listeler   []   ile tanımlanır.         tuple ()  ile tanımlanır.