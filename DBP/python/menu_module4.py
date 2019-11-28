import pymysql
from datetime import datetime 
import time

def check_ATM_status(value) :
    ing = True
    now = datetime.now()

    conn = pymysql.connect(host='192.168.56.103', port=4567 ,user='project_user',password='Sjrnfl1!2!',db='ATMProject')
    cur = conn.cursor()
    
    print("\n\n\n\n\n\n\n\n\n\n-------------------------------------ATM 정보 조회------------------------------------")
    retry_count = 0 
    retry_count_int = 0
    while ing : 
        #관리자 조회
        input_name = input('* 관리자 이름을 입력해 주세요 : ')
        sql_account = 'SELECT user_authority FROM USER WHERE user_name = '+ "\'"+input_name+"\'"
        cur.execute(sql_account)
        res_account = cur.fetchall()

        if not res_account : 
            retry_count += 1
            if retry_count >= 3 :
                print("--------------------------------------------------------------------------------------")
                print(">>> 재시도 횟수 초과("+str(retry_count)+")  초기 화면으로 돌아갑니다")
                print('>>> 초기화면으로 돌아가는 중', end='', flush = True)
                time.sleep(1)
                print('.', end='',flush = True)
                time.sleep(1)
                print('.', end='',flush = True)
                time.sleep(1)
                print('.')
                print("--------------------------------------------------------------------------------------\n\n\n\n\n\n")
                retry_count = 0 
                ing = False 
            else :
                print("! alert) 해당 관리자가 존재하지 않습니다("+str(retry_count)+")  다시입력해주세요")
                continue
        else : 
            input_accountpw = input("* 비밀번호를 입력해 주세요 : ") 
            sql_account_pw = 'SELECT user_authority_pw FROM USER WHERE user_name = '+ "\'"+input_name+"\'"
            cur.execute(sql_account_pw)
            res_account_pw = cur.fetchall()
            try :    
                if res_account_pw[0][0] != input_accountpw : 
                    ing = False
                    print("--------------------------------------------------------------------------------------")
                    print(">>> 비밀번호가 틀렸습니다 초기화면으로 돌아갑니다")
                    time.sleep(1)
                    print('>>> 초기화면으로 돌아가는 중', end='', flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.')
                    print("--------------------------------------------------------------------------------------\n\n\n\n\n\n")
                else :
                    print("--------------------------------------------------------------------------------------")
                    print('>>> ATM 정보 출력 중', end='', flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    #ATM 정보 출력 쿼리
                    sql_atm_status = 'SELECT bank_name, atm_location, atm_cash_balance FROM ATM, BANK WHERE ATM.bank_id = BANK.bank_id'
                    cur.execute(sql_atm_status)
                    res_sql_atm_status = cur.fetchall()
                    print("-------------------------------------A T M 정보---------------------------------------")
                    print("운 영 은 행 : ",res_sql_atm_status[0][0])
                    print("설 치 위 치 : ",res_sql_atm_status[0][1])
                    print("기 기 잔 액 : ",res_sql_atm_status[0][2])
                    print("--------------------------------------------------------------------------------------\n\n\n")
                    ing = False 
            except ValueError : 
                ing = False
                print("--------------------------------------------------------------------------------------")
                print(">>> 비밀번호를 잘못 입력하셨습니다 초기화면으로 돌아갑니다")
                time.sleep(1)
                print('>>> 초기화면으로 돌아가는 중', end='', flush = True)
                time.sleep(1)
                print('.', end='',flush = True)
                time.sleep(1)
                print('.', end='',flush = True)
                time.sleep(1)
                print('.')
                print("--------------------------------------------------------------------------------------\n\n\n\n\n\n")
    cur.close()
    conn.close()            

