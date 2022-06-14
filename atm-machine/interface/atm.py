class atm:
    verify = False
    num = 0
    def __init__(self):
        pass

    def askname(self):
        name = input("please enter your name")
        print(name)
    def askaccno(self):
        accno = input("please enter you account no:")
        print(accno)

    def askusertopick(self):
        num = input("please select 1 for balance.\nPlease select 2 for Withdrawal.\nPlease select 3 for deoposit")

