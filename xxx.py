import re

def is_palindrome_1(tmp_str):
    for i in range(len(tmp_str)):
        if tmp_str[i] != tmp_str[-(i+1)]:
            return False
    return True

x=input().lower()
r='[’!"#$%&\'()*+,-./:;<=>?@[ \\]^_`{|}~\n。！，]+'
a=re.sub(r,'',x)
b=list(a.replace(" ",''))
n=is_palindrome_1(b)
if n==True:
    print('yes')
else:
    print('no')