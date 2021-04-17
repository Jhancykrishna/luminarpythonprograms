lst=[]
for i in range(50,101):
    lst.append(i)
print(lst)

lst=[]
evenlst=[]
oddlst=[]
for i in range(50,101):
    lst.append(i)
for i in lst:
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print(lst)
print(evenlst)
print(oddlst)