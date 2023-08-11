 # Identity Operator : is

x = y = [1,2,3]
z = [1,2,3]

print(x==y)     #True
print(x==z)     #True
print(x is y)   #True
print(x is z)   #False
# Çünkü "is" ile referanslar karşılaştırılır.

print("-----------------------------------------------------")

a = [1,2,3]
b = [2,4]

del a[2]
b[1] = 1
b.reverse()

print(a==b)
print(a is b)
print(a is not b)
#elemanlar aynıdır fakat referanslar farklıdır.


#Membership Operator : in
print("-----------------------------------------------------")

m = ["apple", "banana"]
print("banana" in m)

name = "Çınar"
print("a" in name)
print("a" not in name)


