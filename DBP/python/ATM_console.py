from menu_module1 import *
from menu_module2 import *
from menu_module3 import *
from menu_module4 import *

online = True

def check_input_error(value) :
    if value < 1 or value > 5 :
        print('올바르지 않은 메뉴 입니다. 다시 입력해 주세요 (1-5)')
        print("----------------------------------------------------------------------------\n\n\n")
        return True
    return False



while online :
    print("-----------------------------------A T M------------------------------------")
    print('1. 잔액조회      2.계좌입금     3.계좌출금     4.ATM정보출력      5.종료')
    try : 
        input_num = (int(input('메뉴 입력 : ')))
    except ValueError :
        print("숫자가 아닙니다. 숫자를 입력해주세요 (1-5)")
        print("----------------------------------------------------------------------------\n\n\n")
        continue
    
    if not check_input_error(input_num) : 
        if input_num == 1 : check_balance(input_num)
        elif input_num == 2 : account_deposit(input_num)
        elif input_num == 3 : account_withdraw(input_num)
        elif input_num == 4 : check_ATM_status(input_num)
        elif input_num == 5 : 
            online = False 
            print("-----------------------------------종 료------------------------------------")