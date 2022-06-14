class Atm:
    verify = False
    num = 0
    def __init__(self):
        pass

    @staticmethod
    def verify():
        """
        This function will welcome the user and verify his credentials
        """
        print("HELLO!!!    Welcome to my ATM machine... :) ")
        print("Will you please tell me your name before going ahead -")
        name = input()
        print("Will you please tell me your email-id before going ahead -")
        email_id = input()
        
        # Call a Service and verify the user from database.
        
        print("User Verification Successfull")
        return account_id
    
    @staticmethod        
    def atm_operations(account_id):
        """
        This function will ask the user for choice of operation.
        """
        print("Please tell me how can I help you./n")
        print("Please enter 1 for withdrawl, 2 for deposit, 3 for checking balance")
        choice = int(input())
        Atm.evaluate_choice(choice, account_id)
        
    @staticmethod
    def evaluate_choice(choice, account_id):
        if choice == 1:
            current_balance, withdraw_amount = Atm.withdrawl(account_id)
            print(f"HEY!!, Your current withdrawn amount is : {withdraw_amount}, Current Available Balance : {current_balance}")            
        elif choice == 2: 
            current_balance, deposit_amount = Atm.deposit(account_id)
            print(f"HEY!!, Your current deposited amount is : {deposit_amount}, Current Available Balance : {current_balance}")            
        elif choice == 2: 
            current_balance = Atm.balance_check(account_id)
            print(f"HEY!!, Your current Balance in your account is : {current_balance}")            

    @staticmethod
    def withdrawl():
        """
        Withdraw money from account
        """
        print("I need your account number -")
        acc_number = input()
        print("I need your atm pin number -")
        atm_pin = input()
        # Call service to validate and verify and complete the withdrawl process.
        return cur_bal, with_amt
    
    @staticmethod
    def deposit():
        """
        Deposit money into account
        """
        # Call service to validate and verify and complete the deposit process.
        pass
    
    def balance_check():
        """
        Check current Account balance
        """
        # Call service to validate and verify and complete the balance checking process.
        pass
    
            
        
        