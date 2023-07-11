# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ["Bmw","Mercedes","Opel","Mazda"]
print(arabalar)

# 2- Liste kaç elemanlıdır ? 
print(len(arabalar))

# 3- Listenin ilk ve son elemanı nedir ? 
print(arabalar[0])
print(arabalar[-1])

# 4- Mazda değerini Toyota ile değiştirin.
arabalar[-1] = "Toyota"
print(arabalar)

# 5- Mercedes listenin bir elemanı mıdır ?
print("Mercedes" in arabalar)   # in ile içinde var mı kontrolü

# 6- Listenin -2 indeksindeki değer nedir ? 
print(arabalar[-2])

# 7- Listenin ilk 3 elemanını alın.
print(arabalar[:3])

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = "Toyota","Renault"
print(arabalar)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
#arabalar.append("Audi")
#arabalar.append("Nissan")
print(arabalar+["Audi","Nissan"])    #liste birleştirme

# 10- Listenin son elemanını silin.
#arabalar.pop()
del arabalar[-1]         #2 farklı eleman silme şekli
print(arabalar)

# 11- Liste elemanlarını tersten yazdırın.
print(arabalar[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayın.
      #studentA : Yiğit, Bilgi, 2010, (70,60,70)
      #studentB : Sena, Turan, 1999, (80,80,70)
      #studentC : Ahmet, Turan, 1998, (80,70,90)

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

#Liste elemanlarını ekrana yazdırınız.
print(studentA)
print(studentB)
print(studentC)

#Ekrana "Yiğit Bilgi 9 yaşında ve not ortalaması 66" yazdırın
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3 }"
print(result)



      
