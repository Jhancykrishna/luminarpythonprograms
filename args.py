# def print_person(**datas):
#     print(datas)
#
# print_person(name="ajay",bplace="tcr")
#
#
# def add(*args):
#     print(args)
#
# res=add(10,20,30)



employees={1000:{"name":"sajay","desig":"python tutor", "exp":3},
           1001:{"name":"ajay","desig":"bd tutor", "exp":2},
           1002:{"name":"sanil","desig":"ml tutor", "exp":2},
           }


#
# eid=int(input("enter employee id"))
# if(eid in employees):
#     print(employees[eid]["name"])
# else:
#     print("eid not exist")



def emp_details(**kwargs):#kwargs={eid:1000,prop:"desig"}

    id = kwargs['eid']
    prop=kwargs['prop']

if (id in employees):
    print(employees[id]["name"])
    print(employees[id]["desig"])
else:
    print("id not exist")


emp_details(eid=1000,prop="desig")