import pymysql
from datetime import datetime 

def account_deposit(value) :
    ing = True
    now = datetime.now()

    conn = pymysql.connect(host='localhost', port=3306, user='root', password ='sjrnfl12', db='ATMProject')
    cur = conn.cursor()
    
    print("계좌입금 메뉴입니다.")
    retry_count = 0 
    while ing : 
        #계좌 조회
        input_accountid = input('계좌번호 입력 : ')
        sql_account = 'SELECT * FROM ACCOUNT WHERE account_id = '+ "\'"+input_accountid+"\'"
        cur.execute(sql_account)
        res_account = cur.fetchall()

        if not res_account : 
            retry_count += 1
            if retry_count == 3 :
                print("재시도 횟수 초과("+str(retry_count)+")  초기 화면으로 돌아갑니다.")
                print("----------------------------------------------------------------------------\n\n\n\n\n\n")
                retry_count = 0 
                ing = False 
            else :
                print("계좌 번호가 존재하지 않습니다("+str(retry_count)+")  다시입력해주세요")
                continue
        else : 

            while True :
                try :
                    input_deposit_amount = int(input("입금 하실 금액을 입력해 주세요 : "))
                except ValueError :
                    print("숫자만 입력해 주세요")
                    continue
                
                input_NY = input('입금하실 금액이 '+str(input_deposit_amount)+'가 맞습니까?(Y/N)')
                if input_NY == 'N' : 
                    continue
                elif input_NY != 'Y' and input_NY != 'N' :
                    print('N/Y 만 입력이 가능합니다. 다시 입력해 주세요')
                    continue
                elif input_NY =='Y' :
                    break
            

            input_accountpw = input("비밀번호 입력 : ") 
            try :
                if res_account[0][1] != int(input_accountpw) : 
                    ing = False
                    print("비밀번호가 틀렸습니다. 초기화면으로 돌아갑니다.")
                    print("----------------------------------------------------------------------------\n\n\n\n\n\n")
                else : 
                    #예금 잔액 업데이트
                    sql_update_account_balance = 'UPDATE ACCOUNT SET account_balance = '+str(res_account[0][2])+'+'+str(input_deposit_amount)+' WHERE account_id = '+ "\'"+input_accountid+"\'"
                    cur.execute(sql_update_account_balance)
                    sql_select_updated_account_balance = 'SELECT account_balance FROM ACCOUNT WHERE account_id = '+ "\'"+input_accountid+"\'"
                    cur.execute(sql_select_updated_account_balance)
                    res_updated_account_balance = cur.fetchall()
                    
                    #ATM기 잔액 업데이트 
                    #Update를 위한 잔액 조회
                    sql_ATM_balance = 'SELECT atm_cash_balance FROM ATM'
                    cur.execute(sql_ATM_balance)
                    res_ATM_balance = cur.fetchall() 

                    #Update후 잔액 조회
                    sql_update_ATM_balance = 'UPDATE ATM SET atm_cash_balance = '+str(res_ATM_balance[0][0])+'+'+str(input_deposit_amount)+' WHERE atm_id = 3001'
                    cur.execute(sql_update_ATM_balance)
                    cur.execute(sql_ATM_balance)
                    res_ATM_balance = cur.fetchall()
                 
                    #거래기록 기재
                    sql_inset_trans = 'INSERT INTO TRANSACTION (trans_type, trans_amount, trans_balance) VALUE (\'입금\',' + str(input_deposit_amount)+','+str(res_updated_account_balance[0][0])+')'
                    cur.execute(sql_inset_trans)
                    
                    pwd_date_time = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                
                    sql_inset_operate= 'INSERT INTO OPERATE SELECT max(trans_id), user_id, 3001, \''+pwd_date_time+'\'  FROM TRANSACTION, USER  WHERE USER.user_id = \''+str(res_account[0][5])+'\''
                    cur.execute(sql_inset_operate)
                    
                    conn.commit()


                    while True :
                        input_YN = input('명세표를 출력하시겠습니까?(Y/N)')
                        if input_YN == 'N' : 
                            print("입금 처리 되었습니다. 초기화면으로 돌아갑니다.")
                            print("----------------------------------------------------------------------------\n\n\n\n\n\n")
                            break
                        elif input_YN != 'Y' and input_YN != 'N' :
                            print('N/Y 만 입력이 가능합니다. 다시 입력해 주세요')
                            continue
                        elif input_YN =='Y' :
                            sql_receipt = 'SELECT user_name, trans_type, trans_amount, trans_balance, operate_date FROM USER u, TRANSACTION t, OPERATE o WHERE o.user_id = u.user_id and o.trans_id = t.trans_id ORDER BY operate_date DESC LIMIT 1'
                            cur.execute(sql_receipt)
                            res_receipt = cur.fetchall()
                            print("--------------------------------명  세  표----------------------------------")
                            print("예   금   주 : ",res_receipt[0][0])
                            print("거 래  일 자 : ",res_receipt[0][4])
                            print("거 래  유 형 : ",res_receipt[0][1])
                            print("입 금  금 액 : ",res_receipt[0][2])
                            print("거래 후 잔액 : ",res_receipt[0][3])
                            print("----------------------------------------------------------------------------\n")
                            break
                    ing = False
            except ValueError : 
                ing = False
                print("비밀번호를 잘못 입력하셨습니다. 초기화면으로 돌아갑니다.")
                print("----------------------------------------------------------------------------\n\n\n\n\n\n")
                

