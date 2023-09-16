#global scope
x = "global x"

def function():
    #local scope
    x = "local x"
    print(x)

function()
print(x)