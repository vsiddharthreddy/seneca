class Service():
    @staticmethod
    def verify(name,email):
        """
        this is checking input from users with database and hence called in service layer
        """
        if(name == users.name and email == user_details.email):
            return true

    @staticmethod
    def withdrawl():
        """
        this is checking input from users with database and hence called in service layer
        function also calculates wheter user input for withdrawal amount <= balance and if true
        then it will also print the new balance
        """
        if(accno == accounts.account_no and pin == accounts.pin):
            if(withdrawalamt <= accounts.balance ):
               curr_balance= accounts.balance - withdrawalamt
               return True,curr_balance

    @staticmethod
    def deposit():
        """
        this is takign user input for deposit amount and adding to balance
        """
        curr_balance = accounts.balance
        curr_balance += deposit_amt
        return curr_balance

    @staticmethod    
    def balance_check():
        """
        checks the balance from database only after retrieving user name and emai
        """
        return accounts.balance
