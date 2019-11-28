import pymysql
import time

def check_trans_details(value) :
    ing = True
    conn = pymysql.connect(host='localhost', port=3306, user='root', password ='sjrnfl12', db='ATMProject')
    cur = conn.cursor()
   
    print("\n\n\n\n\n\n\n\n\n\n-------------------------------------거래내역 조회------------------------------------")
    retry_count = 0 
    while ing : 
        input_accountid = input('* 계좌번호를 입력해 주세요 : ')
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
                    sql_trans_details = 'SELECT  user_name, operate_date, trans_type, trans_amount FROM OPERATE o, TRANSACTION t, USER u WHERE o.trans_id = t.trans_id and o.user_id = u.user_id and t.trans_account = \''+input_accountid+'\''
                    cur.execute(sql_trans_details)
                    res_trans_details = cur.fetchall()

                    print("--------------------------------------------------------------------------------------")
                    print('>>> 거래내역 조회 결과 출력 중', end='', flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.', end='',flush = True)
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    print("--------------------------------------조회 결과---------------------------------------")
                    print("\t번호\t예금주\t\t거래일자\t\t\t거래유형\t거래금액")
                    print("--------------------------------------------------------------------------------------")
                    for i in range(0, len(res_trans_details)) :
                        print('\t',i+1,'\t',end ='')
                        for j in range(0, len(res_trans_details[0])) :
                            print (res_trans_details[i][j],'\t\t',end ='')
                        print()
                    print("--------------------------------------------------------------------------------------\n\n\n\n")
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

