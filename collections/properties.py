lst=[10,10.5,True,"jhancy"] #heterogeneous data support
print(lst)

lst=[10,10.5,True,"jhancy","jhancy"]# duplicate data support
print(lst)

lst=[False,10,10.5,True,"jhancy"]#insertion order preserve
print(lst)
print(lst[2]) #index 0 to n-1
lst[1]=5
print(lst) #list is mutable
