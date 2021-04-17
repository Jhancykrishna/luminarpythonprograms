employee=[[1001,"arjun",15000],
          [1002,"anu",20000],
          [1003,"abi",25000],
          [1004,"ajay",10000]]
print(employee)

for i in employee:
    print(i)

for i in employee:
    print(i[1])

for i in employee:
    if(i[2]>17000):
     print(i[1])