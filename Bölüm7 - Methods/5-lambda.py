#map bir listedeki elemanlara tek tek ulaşıp fonksiyona ulaşma işini kolaylaştırır.

def square(num):
    return num**2

numbers = [1,2,3,4,5,6,7,8]

result = list(map(square , numbers))
print(result)

for item in map(square , numbers):
    print(item)





#lambda : fonksiyonu yazmadan kullanırız.

numbers = [1,2,3,4,5,6,7,8]
result = list(map(lambda num: num**2 , numbers))
print(result)




#filter : liste üstünde filtreleme işlemi map ve lambda'ya benzer

def checkEven(num):
    return num%2==0

result = list(filter(checkEven , numbers))
print(result)