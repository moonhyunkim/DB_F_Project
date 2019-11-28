import pymysql
from datetime import datetime 
import time

def account_withdraw(value) :
    ing = True
    now = datetime.now()

    conn = pymysql.connect(host='192.168.56.103', port=4567 ,user='project_user',password='Sjrnfl1!2!',db='ATMProject')
    cur = conn.cursor()
    
    print("\n\n\n\n\n\n\n\n\n\n-------------------------------------계좌출금 메뉴------------------------------------")
    another_bank=False
    retry_count = 0 
    retry_count_int = 0
    while ing : 
        #계좌 조회
        input_accountid = input('* 계좌번호를 입력해 주세요 : ')
        sql_account = 'SELECT * FROM ACCOUNT WHERE account_id = '+ "\'"+input_accountid+"\'"
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
                print("! alert) 계좌 번호가 존재하지 않습니다("+str(retry_count)+")  다시입력해주세요")
                continue
        else : 
            
            while True :
                retry_count_int += 1
                try :
                    #타행은행 출금
                    if res_account[0][6] != 2003 :
                        print("! alert) 해당 계좌는 타행계좌입니다 수수료 1000원이 부과됩니다")
                        another_bank = True
                    input_withdraw_amount = int(input("* 출금 하실 금액을 입력해 주세요 : "))
                except ValueError :
                    if retry_count_int >= 3 :
                        print("--------------------------------------------------------------------------------------")
                        print(">>> 재시도 횟수 초과("+str(retry_count_int)+")  초기 화면으로 돌아갑니다")
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
                        break 
                    else :
                        print("! alert) 숫자만 입력해 주세요("+str(retry_count_int)+")")
                    continue
                input_NY = input('* 출금하실 금액이 '+str(input_withdraw_amount)+'원이 맞습니까?(Y/N) : ')
                if input_NY == 'N' :
                    continue
                elif input_NY != 'Y' and input_NY != 'N' :
                    print('! alert) N/Y 만 입력이 가능합니다 다시 입력해 주세요')
                    continue
                elif input_NY =='Y' :
                    break
            
            if retry_count_int >= 3 : break

            input_accountpw = input("* 비밀번호를 입력해 주세요 : ") 
            try :
                if res_account[0][1] != int(input_accountpw) : 
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
                    if input_withdraw_amount > res_account[0][2] :
                        ing = False 
                        print("--------------------------------------------------------------------------------------")
                        print(">>> 계좌 잔액이 부족합니다 초기화면으로 돌아갑니다")
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
                        if another_bank : input_withdraw_amount += 1000

                        #예금 잔액 업데이트(출금) 
                        sql_update_account_balance = 'UPDATE ACCOUNT SET account_balance = '+str(res_account[0][2])+'-'+str(input_withdraw_amount)+' WHERE account_id = '+ "\'"+input_accountid+"\'"
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
                        sql_update_ATM_balance = 'UPDATE ATM SET atm_cash_balance = '+str(res_ATM_balance[0][0])+'-'+str(input_withdraw_amount)+' WHERE atm_id = 3001'
                        cur.execute(sql_update_ATM_balance)
                        cur.execute(sql_ATM_balance)
                        res_ATM_balance = cur.fetchall()
                        
                        #거래기록 기재
                        input_withdraw_amount -= 1000
                        sql_inset_trans = 'INSERT INTO TRANSACTION (trans_type, trans_amount, trans_balance, trans_account) VALUE (\'출금\',' + str(input_withdraw_amount)+','+str(res_updated_account_balance[0][0])+',\''+input_accountid+'\')'
                        cur.execute(sql_inset_trans)
                        
                        pwd_date_time = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                    
                        sql_inset_operate= 'INSERT INTO OPERATE SELECT max(trans_id), user_id, 3001, \''+pwd_date_time+'\'  FROM TRANSACTION, USER  WHERE USER.user_id = \''+str(res_account[0][5])+'\''
                        cur.execute(sql_inset_operate)
                        
                        conn.commit()


                        while True :
                            input_YN = input('* 거래 명세표를 출력하시겠습니까?(Y/N) :')
                            if input_YN == 'N' : 
                                print("--------------------------------------------------------------------------------------")
                                print(">>> 출금 처리 되었습니다 초기화면으로 돌아갑니다")
                                time.sleep(1)
                                print('>>> 초기화면으로 돌아가는 중', end='', flush = True)
                                time.sleep(1)
                                print('.', end='',flush = True)
                                time.sleep(1)
                                print('.', end='',flush = True)
                                time.sleep(1)
                                print('.')
                                print("--------------------------------------------------------------------------------------\n\n\n\n\n")
                                break
                            elif input_YN != 'Y' and input_YN != 'N' :
                                print('alert) N/Y 만 입력이 가능합니다. 다시 입력해 주세요')
                                continue
                            elif input_YN =='Y' :
                                print("--------------------------------------------------------------------------------------")
                                print('>>> 명세표 출력 중', end='', flush = True)
                                time.sleep(1)
                                print('.', end='',flush = True)
                                time.sleep(1)
                                print('.', end='',flush = True)
                                time.sleep(1)
                                print('.')
                                time.sleep(1)
                                sql_receipt = 'SELECT user_name, trans_type, trans_amount, trans_balance, operate_date, trans_account FROM USER u, TRANSACTION t, OPERATE o WHERE o.user_id = u.user_id and o.trans_id = t.trans_id ORDER BY operate_date DESC LIMIT 1'
                                cur.execute(sql_receipt)
                                res_receipt = cur.fetchall()
                                
                                print("-------------------------------------명  세  표---------------------------------------")
                                print("예   금   주 : ",res_receipt[0][0])
                                print("거 래  계 좌 : ",res_receipt[0][5])
                                print("거 래  일 자 : ",res_receipt[0][4])
                                print("거 래  유 형 : ",res_receipt[0][1])
                                print("거 래  금 액 : ",res_receipt[0][2])
                                print("거래 전 잔액 : ",res_account[0][2])
                                print("거래 후 잔액 : ",res_receipt[0][3])
                                if another_bank : print("수   수   료 :  타행계좌 1000원")
                                else : print( "수   수   료 :  면제")
                                print("--------------------------------------------------------------------------------------")
                                break
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

