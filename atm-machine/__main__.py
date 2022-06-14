from interface.atm import Atm

def start():
    """
    The main caller
    """
    account_id = Atm.verify()

# The Application Execution Starts here.
if __name__ == "__main__":
    start()
