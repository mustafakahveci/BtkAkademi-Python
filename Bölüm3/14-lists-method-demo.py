names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz.
#names.append("Cenk")
#print(names)

#2- "Sena" değerini listenin başına ekleyiniz.
#names.insert(0,"Sena")
#print(names)

#3- "Deniz" ismini listeden siliniz.
#names.remove("Deniz")
#print(names)

#4- "Deniz" isminin indeksi nedir?
#print(names.index("Deniz"))

#5- "Ali" listenin bir elemanı mıdır ? 
#print("Ali" in names)

#6- Liste elemanlarını ters çevirin.
#names.reverse()
#print(names)

#7- Liste elemanlarını alfabetik olarak sıralayınız.
#names.sort()
#print(names)

#8- years listesinin rakamsal büyüklüğe göre sıralayınız.
#years.sort()
#years.reverse()
#print(years)

#9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
#str = "Chevrolet,Dacia".split(',')
#print(str)

#10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(min(years))
print(max(years))

#11- years dizisinde kaç tane 1998 değeri vardır ? 
print(years.count(1998))

#12- years dizisinin tüm elemanlarını silin. 
years.clear()
print(years)

#13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

markalar.append(input("marka: "))
markalar.append(input("marka: "))
markalar.append(input("marka: "))

print(markalar)