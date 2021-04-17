# finally execute with either try or except command in exception handling
try:
    num1 = int(input("enter"))
    print("entered number is", num1)
except:
    print("please enter a integer value")
finally:
    print("inside finally")