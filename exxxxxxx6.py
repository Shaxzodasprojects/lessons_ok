a = [1, 4,2, 3, 'a']
a.append(9)
a.append([1,2,3])
print(a)
b = a.copy()
print(a.count(1))
a.extend([1,2,3,4])
print(a)
print(a.index(4))
a.insert(1, 'a')
print(a)
a.pop()
print(a)
d = a.pop(1)
print(a, d)
a.remove(1)
print(a)
a.reverse()
print(a)
i = 0
while i < len(a):
    if not isinstance(a[i], int):
        a.remove(a[i])
        i -= 1
    i += 1
print(a)
a.sort()
print(a)