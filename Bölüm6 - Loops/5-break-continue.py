name = "Sadık Turan"

for letter in name:
    if letter == "ı":
        break               
    print(letter)           

# "break" = bulunduğu yerde döngüyü sonlandırıp çıkar.

print("-----------------------------------------------------")
for letter in name:
    if letter == "ı":
        continue               
    print(letter)  

# "continue" = bulunduğu yerde o adımı sonlandırıp devam eder.  



print("-----------------------------------------------------")

#1'den 100'e kadar olan tek sayıların toplamı

x = 1
toplam = 0
while(x <= 100):
    if(x % 2 == 1):
        toplam+=x
    x+=1
print(toplam)