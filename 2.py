a = input()
b = a.split(',')
for i in range(len(b)):
    b[i] = int(b[i])
for j in range(0, len(b), 2):
    for k in range(j, len(b), 2):
        if b[j] > b[k]:
            b[j], b[k] = b[k], b[j]
print("[",end="")
for m in range(len(b)):
    if m != len(b) -1:
        print("%d"%b[m], end="," )
    else:
        print("%d"%b[m],end="")
print("]")