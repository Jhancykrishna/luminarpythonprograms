class Bank:
    bankname="sbi"
    def accreate(self,accnum,name):
        self.accnum=accnum
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal

    def deposit(self,amount):
        self.balance+=amount
        print("your",Bank.bankname,"account has been created with amount",amount)
        print("your current balance=",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",amount)
            self.balance-=amount
            print("available balance=",self.balance)

obj=Bank()
obj.accreate(123,"abc")
obj.deposit(2500)
obj.withdraw(1500)