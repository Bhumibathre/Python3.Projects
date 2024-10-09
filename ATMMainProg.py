#ATMMainProg.py<---Main Program
from ATMMenu import menu
import sys
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffFundError
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("\tDon't try to deposit alnums,str and symbols--invalid Deposits-try again")
                except DepositError:
                    print("\tDon't try to deposit Negative and Zero Values--try again")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\tDon't try to With alnums,str and symbols--invalid Withdrwa-try again")
                except WithdrawError:
                    print("\tDon't try to Withdraw Negative and Zero Values--try again")
                except InSuffFundError:
                    print("\tUr Account xxxxx123 does not suff funds--read python notes:")
            case 3:
                balenq()
            case 4:
                print("Thx for using this Program")
                sys.exit()
            case _:
                print("Ur Selection of Operation is wrong-try again")
    except ValueError:
        print("Don't enter alnums,symbols,strs and floats as Choice")
