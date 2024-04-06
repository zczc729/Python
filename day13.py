
lst = [1, 2, 3]

print(lst)
print(lst[0])
print(lst[1])


lst = [1, 2, 3]
lst[0] = 'a'
lst[2] = lst[1] * 2
lst[1] = lst[0] * lst[2]

print(lst)

print(lst[-1])
print(lst[-3])



lst = [1, 2, 3]

lst[-3] = 'b'
lst[-1] = lst[1] * 2
lst[-2] = lst[0] * lst[2]

print(lst)


lst = [1, 2, 3]

print(lst)
print(lst[0:2])
print(lst[1:3])

lst[0:2] = [2, 4]

print(lst)

lst[1:3] = 'a', 'b'

print(lst)

print(lst)
print(lst[-3:-1])
print(lst[-2:])


lst = [1, 2, 3]

lst[0:2] = [2, 4]

print(lst)

lst[1:3] = 'a', 'b'

print(lst)

lst = [1, 2, 3]

lst[-3:-1] = [4, 8]

print(lst)

lst[2:] = 'c', 'd'

print(lst)


lst = [1, 2, 3]

for value in lst:
	print(value)


lst = [1, 2, 3]

for idx in range(3):
	lst[idx] = lst[idx] + 1
	print(lst[idx])

lst = [1, 2, 3]

for idx in range(len(lst)):
	lst[idx] = lst[idx] + 1
	print(lst[idx])


lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]

print(lst[0])
print(lst[1])
print(lst[2][0])


lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]

for val in lst:
	print(val[0], val[1])



lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]

for val in lst:
	for x in val:
		print(x, end='')
	print()

lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]

for idx in range(len(lst)):
    for idy in range(len(lst[idx])):
        lst[idx][idy] = idx + idy
        print(lst[idx][idy], end='')
    print()








