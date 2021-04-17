employee={"id":1001,"ename":"arun","designation":"teacher","salary":25000}
print(employee)
print(employee["ename"])
print("company"in employee)
employee["company"]="luminar"
employee["salary"]+=15000
print(employee)
for i in employee:
    print(i,":",employee[i])
