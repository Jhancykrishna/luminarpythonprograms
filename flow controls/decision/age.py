by=int(input('enter your birth year'))
bm=int(input('enter your birth month'))
bd=int(input('enter your birth date'))
cy=int(input('enter your current year'))
cm=int(input('enter your current month'))
cd=int(input('enter your current date'))
if(bm==cm)&(bd==cd):
    print('age=',cy-by)
else:
    print('age=',(cy-by)-1)