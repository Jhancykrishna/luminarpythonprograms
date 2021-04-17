f=open("C:/Users/USER/PycharmProjects/pythonProject/files/data","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
print(words)
# for i in words:
#    if(i not in dict):
#        dict[i]=1
#    else:
#        dict[i]+=1
# print(dict)