x = 5
y = 10
z = 20

x, y, z = 5, 10, 20

print(x, y, z)

x, y = y, x
print(x, y, z)

x = x + 5     # x += 5
print(x, y, z)

values = 1, 2, 3
print(values)
print(type(values))

x, y, z = values
print(x, y, z)