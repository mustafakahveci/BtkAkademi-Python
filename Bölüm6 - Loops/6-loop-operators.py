#RANGE   (BAŞLANGIÇ , BİTİŞ , ARTIŞ MİKTARI)
#belli aralıktaki sayıları yazdırmak için kullanılan bir metod

for item in range(10):
    print(item)
print("------------------------------------------")
for item in range(5,20):
    print(item)
print("------------------------------------------")
for item in range(0,10,2):
    print(item)
print("------------------------------------------")
for item in range(50,100,20):
    print(item)

print(list(range(5,100,10)))






#ENUMERATE 
#indeksleri de görmeye yarar. numaralandırmak anlamına gelir.

greeting = "Hello World"

for index,item in enumerate(greeting):
    print(f"index: {index} letter: {item}")






#ZİP
#dictionary yapısına benzerlik gösterir.

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1 , list2 , list3):
    print(item)

for a,b,c in zip(list1 , list2 , list3):
    print(a,b,c)