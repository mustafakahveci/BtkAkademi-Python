name = "Mustafa"
surname = "Kahveci"
age = 23

greeting = "My name is "+ name +" "+ surname + " and \nI am "+ str(age) + " years old."
length = len(greeting) #string uzunluğu

print(greeting)
print(greeting[0])   #ilk karakter
print(greeting[3])
print(greeting[-1])  #son karakter 
print(greeting[length-1])
print(greeting[3:7]) #3'ten başla 7'ye kadar
print(greeting[3:])  #3'ten başla sonuna kadar
print(greeting[:16]) #0. indexten başla  16. karaktere kadar
print(greeting[2:40:2]) #2. karakterden başla 40. karaktere kadar 2'şer 2'şer ilerle.




