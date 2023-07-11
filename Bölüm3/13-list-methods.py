numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a','g','s','b','y','a','s']

print(min(numbers))          #min-max alabiliriz.
print(max(numbers))
print(min(letters))
print(max(letters))

print(numbers[3:6])
print(numbers[:3])
print(numbers[4:])

numbers[4] = 40
print(numbers)

numbers.append(49)          #sonuna ekleme
print(numbers)

numbers.insert(3,78)         #verilen index'e ekleme
print(numbers)

numbers.insert(-1,52) 
print(numbers)

numbers.pop(3)               #verilen index'teki elemanı silme
print(numbers)

numbers.remove(49)            #verilen elemanı silme
print(numbers)

numbers.sort()                #listeyi sıralama
print(numbers)
letters.sort()
print(letters)

numbers.reverse()             #listeyi ters çevirme
print(numbers)

print(len(numbers))

print(numbers.count(10))         #kaç tane 10 var

numbers.clear()                  #listeyi temizleme
print(numbers)