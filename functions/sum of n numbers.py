def sumN():
    sum=0
    num=int(input('enter a number'))
    for i in range(1,num+1):
        sum=sum+i
    print(sum)
sumN()

print('************')

def sumN(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    print(sum)
sumN(5)

print('************')

def sumN(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
data=sumN(5)
print(data)