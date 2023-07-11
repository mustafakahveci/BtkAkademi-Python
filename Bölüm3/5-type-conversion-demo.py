"""

      Daire Alani   : (π) * (r**2)
      Daire Çevresi : 2πr

      Yari çarpi verilen bir dairenin 
      alan ve çevresini hesaplayiniz. 
      (π=2)

"""

yaricap = float(input("yari çap : "))
pi = 3.14
daireCevre = 2 * pi * yaricap
daireAlan = pi * (yaricap ** 2)

print("Dairenin alani : ",daireAlan)
print("Dairenin çevresi : ", daireCevre)