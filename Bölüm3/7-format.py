name = "Çınar"
surname = "Turan"
age = 45

print("My name is {} {}".format(name,surname))
print("My name is {1} {0}".format(name,surname))
print("My name is {s} {n}".format(n=name,s=surname))
print("My name is {} {} and I am {} years old".format(name,surname,age))
print("My name is {} {} and I am {} years old".format(name,name,name))

print(f"My name is {name} {surname} and I am {age} years old")

result = 200/700
print("the result is {}".format(result))
print("the result is {r:1.3}".format(r=result))
print("the result is {r:10.3}".format(r=result))