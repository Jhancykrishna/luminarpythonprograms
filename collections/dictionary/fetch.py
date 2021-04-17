# student={"roll no":1001,"name":"arun","age":25,"cpp":25}
# for i in student:
#     print(i,":",student[i])

student={"roll no":1001,"name":"arun","age":25,"cpp":25}
student["name"]="arjun"
print(student)

student={"roll no":1001,"name":"arun","age":25,"cpp":25}
student["cpp"]+=10
del student["cpp"]
print(student)