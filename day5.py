x,y,z = 10, 10.0, '10'
print(type(x))
print(type(y))
print(type(z))

print(x+y)
print(type(x+y))

print(x+int(z))

z = int(z)

print(type(z))
print(x+z)

a,b = 0,''
print(bool(a))
print(bool(b))

x,y,z = '100', 10.5, 20

print(int(x) + y)
print(x + str(z))
print(str(y) + str(float(z)))
print(str(int(x) + y) + str(z))
