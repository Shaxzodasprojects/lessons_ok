a = [[1,2,3,'a'], [4,5,6,'b'], [7,8,9,'c'], ['a','b','c','d']]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()