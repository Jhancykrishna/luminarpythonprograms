def cube():
    num=int(input('enter a number'))
    result=num**3
    print(result)
cube()

print('**************')

def cube(num):
    result=num**3
    print(result)
cube(3)

print('**************')

def cube(num):
    result=num**3
    return result
data=cube(3)
print(data)