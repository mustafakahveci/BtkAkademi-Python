message = "Hello There. My name is Mustafa Kahveci".split()    #kelimelerine göre liste oluşturdu.
print(message[0])

message = "Hello There. My name is Mustafa Kahveci"
print(message[0])   # ilk harfi basar

my_list = [1,2,3]
my_list = ["bir",2,True,5.6]    #farklı değişkenlerle liste oluşturabildik.
print(my_list)

list1 = ["one","two","three"]
list2 = ["four","five","six"]
numbers = list1 + list2     #liste birleştirme işlemi
print(numbers)
print(len(numbers))          #liste uzunluğu
 
userA = ["Sadık",36]
userB = ["Çınar",2]
users = [userA,userB]       #2 listeli tek liste oluşturdu liste içinde liste
print(users)
 