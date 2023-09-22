import random

#print(dir(random))
#print(help(random))

print(random.random())
print(random.uniform(10,35))
print(random.randint(1,100))

names = ["ali","yağmur","deniz","cenk","ahmet","efe"]
print(names[random.randint(0,len(names)-1)])

print(random.choice(names))    #rastgele 1 tane seçer

print("----------------------------------")

my_list = list(range(10))
random.shuffle(my_list)    #listeyi karıştırır.
print(my_list)

liste = range(100)
result = random.sample(liste, 3)    # liste içinden rastgele 3 tanesini seçer 
print(result)