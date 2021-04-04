inner=int(input("Количество строк в треугольнике Паскаля: "))
list=[]
for n in range(inner):
    nextlist=[]
    for m in range (n+1):
        if m==0 or m==n:
            nextlist.append(1)
        else:
            nextlist.append(list[n-1][m-1]+list[n-1][m])
    list.append(nextlist)
for n in range (inner):
    for m in range (inner-n-1):
        print(format(' ','<4'),end='')
    for m in range(n+1):
        print(format(list[n][m],'<8'), end='')
    print(' ')