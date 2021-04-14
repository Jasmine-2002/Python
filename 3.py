n = int(input())
num = 1
a = [[0]*n for i in range(n)]

begy = int(n/2)

if n%2 == 0:
    begx = begy-1
else:
    begx = begy

a[begx][begy] = num

def luxian(i):
    if i%2!=0:
        a = [[0,-1], [1,0],[0,1]]
    else:
        a = [[0,1],[-1,0],[0,-1]]
    return a

def zhixin(x):
    global num,begx,begy
    num += 1
    begx += FX[x][0]
    begy += FX[x][1]
    a[begx][begy] = num


for i in range(1,n):
    FX = luxian(i)
    zhixin(0)
    for j in range(i):
        zhixin(1)
    for j in range(i):
        zhixin(2)

for i in range(n):
    for j in range(n):
        if j != n-1:
            print(str(a[i][j]).ljust(4),end="")
        else:
            print(a[i][j],end="")

    print()