def fact():
    factorial=1
    num=int(input('enter a number'))
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
fact()

print('************')

def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
fact(5)

print('************')

def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
data=fact(5)
print(data)