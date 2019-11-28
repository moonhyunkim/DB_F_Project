import pymysql
import time

def check_balance(value) :
    ing = True
    conn = pymysql.connect(host='localhost', port=3306, user='root', password ='sjrnfl12', db='ATMProject')
    cur = conn.cursor()
   
    print("\n\n\n\n\n\n\n\n\n-------------------------------------잔액조회 메뉴------------------------------------")
    retry_count = 0 
    while ing : 
        input_accountid = input('* 계좌번호를 입력해 주세요: ')
        sql_accountid = 'SELECT * FROM ACCOUNT WHERE account_id = '+ "\'"+input_accountid+"\'"
        cur.execute(sql_accountid)
        res_accountid = cur.fetchall()
        if not res_accountid : 
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
                print("! alert) 계좌 번호가 존재하지 않습니다("+str(retry_count)+")  다시입력해주세요")
                continue
        else : 
            input_accountpw = input("* 비밀번호를 입력해 주세요 : ") 
            sql_accountpw = 'SELECT account_pw FROM ACCOUNT WHERE account_id = '+ "\'"+input_accountid+"\'"
            cur.execute(sql_accountpw)
            res_accountpw = cur.fetchall()
            try :
                if res_accountpw[0][0] != int(input_accountpw) : 
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
                    print("----------------------------------------------------------------------------\n\n\n\n\n\n")
                else : 
                    #예금 주 SQL
                    sql_username = 'SELECT user_name FROM USER WHERE user_id = '+ str(res_accountid[0][5])
                    cur.execute(sql_username)
                    res_username = cur.fetchall()
                    
                    #거래 은행 SQL 
                    sql_bankname = 'SELECT bank_name FROM BANK WHERE bank_id = '+ str(res_accountid[0][6])
                    cur.execute(sql_bankname)
                    res_bankname = cur.fetchall()
                    print("--------------------------------------------------------------------------------------")
                    print('>>> 잔액조회 결과 출력중', end='', flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("--------------------------------------조회 결과---------------------------------------")
                    print("예금  주 : ",res_username[0][0])
                    print("거래은행 : ",res_bankname[0][0])
                    print("예금종류 : ",res_accountid[0][3])
                    print("개설날짜 : ",res_accountid[0][4])
                    print("잔    액 : ",res_accountid[0][2])
                    print("--------------------------------------------------------------------------------------\n")
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

