f=open("numbers","r")
# list=[]
# for num in f:
#     list.append(int(num.rstrip("\n")))
# print(list)
# print(sum(list))

evenlist=[]
oddlist=[]
for num in f:
    if(int(num)%2==0):
        evenlist.append(int(num.rstrip("\n")))
    else:
        oddlist.append(int(num.rstrip("\n")))
print(evenlist)
print(oddlist)
print(sum(evenlist))
print(sum(oddlist))