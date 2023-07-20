# key - value

# 41 => kocaeli    34 => istanbul

sehirler = ["kocaeli", "istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("istanbul")])

plakalar = {"kocaeli":41 , "istanbul":34}    # dictionary tanımlama 

print(plakalar["istanbul"])
print(plakalar["kocaeli"])

plakalar["ankara"] = 6      # eleman eklenebilir.
plakalar["kocaeli"] = "new value"     # value değerleri değiştirilebilir.
print(plakalar)


users = {                        #dictionary içinde farklı özellikler de eklenebilir.
    "sadikturan": {
        "age" : 36,
        "roles" : ["user"],
        "email" : "sadik@gmail.com",
        "address" : "kocaeli",
        "phone" : "1325612"
    },
    "cinarturan": {
        "age" : 2,
        "roles" : ["admin","user"],
        "email" : "cinar@gmail.com",
        "address" : "kocaeli",
        "phone" : "54645546"
    }
}

print(users["cinarturan"])
print(users["cinarturan"]["age"])
