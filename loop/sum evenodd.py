low=int(input('enter lower limit'))
upp=int(input('enter upper limit'))
evensum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        evensum=evensum+1
    else:
        oddsum=oddsum+1
print(evensum)
print(oddsum)