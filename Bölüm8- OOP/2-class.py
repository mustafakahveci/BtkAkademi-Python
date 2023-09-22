# class
class Person:
    # class attributes
    address = "-"
    # constructor (yapıcı metod)
    def __init__(this, name, year):
        # object attributes
        this.name = name
        this.year = year

    # instance methods
    def intro(this):
        print("Hello there. I am " +this.name)
    # instance methods 
    def calculateAge(this):
        return 2023 - this.year


# object

p1 = Person(name="ali", year=1990)
p2 = Person(name="yagmur", year=1995)

print(p1)  
print(type(p1))
print(p2)  
print(type(p2))
print(p1.name)
print(p1.year)
print(p1.address)
print(p2.name)
print(p2.year)
print(p2.address)

#updating
p1.address = "Kocaeli"
print(p1.address)
p1.intro()
p2.intro()
print(p1.calculateAge())
print(p2.calculateAge())



class Circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap
    
    def cevreHesapla(self):
        return 2 * self.yaricap * self.yaricap
    
    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)
    

c1 = Circle(yaricap=3) 
c2 = Circle()
print(c1.alanHesapla())
print(c2.alanHesapla())