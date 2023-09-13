"""
   Soru : Girilen bir sayının asal olup olmadığını bulunuz. 
   ** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

"""

sayi = int(input("Sayıyı giriniz : "))
control = False

for i in range(2,sayi):
    if(sayi % i == 0):
        control = True
        break

if(control == False):
    print(f"{sayi} asaldır")
else:
    print(f"{sayi} asal değildir")

