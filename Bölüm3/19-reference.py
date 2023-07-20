#value types => string, number

x = 5
y = 25

x = y
y = 10               # değişim olmadı

print(x,y)

#reference types => list, class

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0] = "grape"           # değişim oldu 

print(a,b)

