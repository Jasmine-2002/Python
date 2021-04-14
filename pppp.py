x=input()
a_list=x.split(",")
for i in range(len(a_list)):
  if a_list[i]%2==0:
    a_list[i]=a_list[i]**2
for i in range(len(a_list)):
  if i!=len(a_list)-1:
    print("%d,"%a_list[i], end="")
  else:
    print("%d"%a_list[i])