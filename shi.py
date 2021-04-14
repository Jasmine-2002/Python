import math

def wan(n):
    for i in range(10 ** (n - 1), 10 ** n - 1):
        list = []
        for j in range(1, i):
            if i % j == 0:
                list.append(j)
        sum_list = sum(list)
        if sum_list == i:
            a_list = []
            count = 0
            a_list.append(i)
            count += 1
    return count, a_list

n=int(input())
x,lst=wan(n)
print(x)
print(lst)




