a,b=map(int,input().split())
c=round(1.1*b)
d=round(1.5*b)
if a<c:
    print("OK")
elif a<d:
    print('Exceed {:.0%}. Ticket 200'.format((a-b)/b))
else:
    print('Exceed {:.0%}. License Revoked'.format((a-b)/b))