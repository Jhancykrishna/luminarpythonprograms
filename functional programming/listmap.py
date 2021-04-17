# lst=[4,2,1,6,7,8]
#output=3,1,0,7,8,9

# updatelist=[]
# for i in lst:
#     if(i<5):
#         i-=1
#         updatelist.append(i)
#     else:
#         i+=1
#         updatelist.append(i)
# print(updatelist)

# result=list(map(lambda num:num-1 if num<5 else num+1,lst))
# print(result)


# from functools import reduce
# list=[10,20,30,40,50]
# total=reduce(lambda no1,no2:no1+no2,list)
# print(total)
# max=reduce(lambda no1,no2:no1 if no1>no2 else no2,list)
# print(max)
# min=reduce(lambda no1,no2:no1 if no1<no2 else no2,list)
# print(min)


#list comprehension
list=[1,2,3,4]
lst=[10,20]
squares=[num**2 for num in list]
print (squares)

even=[num for num in list if num%2==0]
print (even)

pairs=[(i,j) for i in list for j in lst]
print(pairs)
