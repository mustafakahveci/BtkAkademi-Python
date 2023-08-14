# 1-100 e kadar

x = 0

while(x < 100):
    print(x)
    x+=1
print("SON...")

#1 den 100 e kadar sadece çift sayılar
y = 0
while(y < 100):
    if(y % 2 == 0):
        print(y)
    y+=1
print("SON...")    

name = "" 
while not name:
    name = input("isminizi giriniz : ")

print(f"{name} hoşgeldin")