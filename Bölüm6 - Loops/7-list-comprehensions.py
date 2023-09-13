numbers = []

for x in range(10):
    numbers.append(x)

print(numbers)

numbers = [x for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10) if x%3==0]
print(numbers)

myString = "Hello World"
myList = [letter for letter in myString]
print(myList)


years = [1983, 1999, 2008, 1956, 1986]
ages = [2023-year for year in years]
print(ages)

results = [x if x%2==0 else "TEK" for x in range(10)]
print(results)


sayilar = []

for x in range(3):
    for y in range(3):
        sayilar.append((x,y))

print(sayilar)

sayilar = [(x,y) for x in range(3) for y in range(3)]
print(sayilar)