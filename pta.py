def Freq(line):
    rlist = list(line)
    rdict = {}
    for i in rlist:
        if rdict.get(i,-1)==-1:
            rdict[i] = 1
        else:
            rdict[i] += 1
    print(len(rdict))
    res = sorted(rdict)
    print(res)
    k = 0
    for j in range(len(rdict)):
        for key,value in rdict.items():
            if key == res[k]:
                print("{} = {}".format(key, value))
        k+=1

line = input()
Freq(line)