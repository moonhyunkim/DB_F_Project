
drop database ATMProject;
create database ATMProject;
USE ATMproject;


CREATE TABLE USER
( user_id         INT   NOT NULL,
  user_name       VARCHAR(20)      NOT NULL,
  user_address    VARCHAR(30),
  user_phone      VARCHAR(20),
  user_authority  VARCHAR(20),
  user_authority_pw  VARCHAR(20),
PRIMARY KEY   (user_id));

CREATE TABLE BANK
( bank_id          		INT             NOT NULL,
  bank_name    			VARCHAR(30)     NOT NULL,
  bank_phone 		 	VARCHAR(30)		NOT NULL,
  bank_location         VARCHAR(30) 	NOT NULL,
PRIMARY KEY (bank_id) );

CREATE TABLE ACCOUNT
( account_id         VARCHAR(30)       NOT NULL,
  account_pw         INT               NOT NULL,
  account_balance    INT               NOT NULL,
  account_type       CHAR(9)           NOT NULL,
  account_open_date  DATE			   NOT NULL,
  user_id			 INT			   NOT NULL,
  bank_id			 INT			   NOT NULL,
PRIMARY KEY (account_id),
FOREIGN KEY (user_id) REFERENCES USER(user_id),
FOREIGN KEY (bank_id) REFERENCES BANK(bank_id));

CREATE TABLE TRANSACTION 
( trans_id         INT  auto_increment             NOT NULL,
  trans_type       VARCHAR(15)       NOT NULL,
  trans_amount	   INT               NOT NULL,
  trans_balance    INT               NOT NULL,
  trans_account    VARCHAR(30)       NOT NULL,
PRIMARY KEY (trans_id));


ALTER TABLE TRANSACTION auto_increment=1001;


CREATE TABLE ATM
( atm_id           INT              NOT NULL,
  atm_location     VARCHAR(30)     NOT NULL,
  atm_cash_balance INT,
  bank_id         INT,
PRIMARY KEY (atm_id),
FOREIGN KEY (bank_id) REFERENCES BANK(bank_id) );

CREATE TABLE OPERATE
( trans_id         INT               NOT NULL,
  user_id          INT               NOT NULL,
  atm_id           INT               NOT NULL,
  operate_date	   DATETIME              NOT NULL,
PRIMARY KEY (trans_id, user_id, atm_id),
FOREIGN KEY (trans_id) REFERENCES TRANSACTION(trans_id),
FOREIGN KEY (user_id) REFERENCES USER(user_id),
FOREIGN KEY (atm_id) REFERENCES ATM(atm_id) );


INSERT INTO USER
VALUES      (1001,'김문현','충청북도 청주시 흥덕구 49-12','010-6338-7119','관리자','1234'),
            (1002,'나지현','인천광역시 연수구 19-15','010-9491-2774','','' ),
            (1003,'김경준','충청남도 태안시 어쩌구  19-12','010-2313-4423','',''),
            (1004,'장찬용','충북 청주시 서원구 52-122','010-1234-5323','',''),
            (1005,'황승혜','대전광역시 서구 122-25','010-5645-9786','',''),
            (1006,'이재우','서울특별시 광진구 312-44','010-2314-2312','',''),
            (1007,'김창현','경상남도 진해시 동구 493-142','010-5334-5534','',''),
            (1008,'김권우','경상북도 상주시 492-12','010-5512-2211','','');

INSERT INTO BANK
VALUES      (2001,'Shinhan',1599-8000,'서울특별시 중구 세종대로9길 20'),
            (2002,'KB','1588-9999','서울특별시 중구 남대문로 84'),
            (2003,'NH Bank','02-733-2615','서울특별시 중구 충정로1가 통일로 120'),
            (2004,'IBK Bank','02-1588-2588','서울특별시 중구 명동 을지로 79'),
            (2005,'KEB Bank','02-3788-5464','서울특별시 중구 을지로2가 을지로 35'),
            (2006,'Woori Bank','02-1588-5000','서울특별시 중구 회현동1가 소공로 51'),
            (2007,'Kakao Bank','02-6420-3333','경기도 성남시 분당구 판교역로 231, 에스동 5층');
            
INSERT INTO ACCOUNT
VALUES      ('3333-03-9105862',1234,1000000,'일반예금','2018-7-30',1001,2007),
			('3333-04-2351436',3124,2000000,'일반예금','2018-1-20',1002,2007),
            ('3333-02-1234142',5323,3000000,'일반예금','2018-5-31',1003,2007),
            ('3333-03-4365745',1243,1500000,'일반예금','2017-6-23',1004,2007),
            ('3333-01-7854674',5231,3600000,'일반예금','2018-7-30',1005,2007),
            ('3333-07-7456254',1234,5100000,'일반예금','2018-7-30',1006,2007),
            ('3333-08-4523543',5523,7300000,'일반예금','2018-7-30',1007,2007),
            ('3333-02-8564356',5687,8800000,'일반예금','2018-7-30',1008,2007),
            ('3333-03-4512353',9676,8400000,'일반예금','2018-7-30',1001,2001),
            ('110-123-3256334',1765,1200000,'일반예금','2018-7-30',1002,2003),
            ('110-534-1234123',4123,2400000,'일반예금','2018-7-30',1003,2002),
            ('110-123-1231451',1899,9900000,'일반예금','2018-7-30',1004,2005),
            ('110-634-2354234',1888,2500000,'일반예금','2018-7-30',1005,2004),
            ('110-032-1233124',1778,1800000,'일반예금','2018-7-30',1006,2005),
            ('123-123-1234567',1564,8600000,'일반예금','2018-7-30',1007,2001),
            ('123-331-5341234',1334,5400000,'일반예금','2018-7-30',1008,2002),
            ('123-423-1235234',8884,700000,'일반예금','2018-7-30',1001,2006),
            ('6717834-03-1234',9564,8900000,'일반예금','2018-7-30',1002,2004),
            ('6717834-03-2413',1854,7000000,'일반예금','2018-7-30',1003,2001),
            ('6717834-02-5231',1124,7800000,'자유적금','2018-7-30',1004,2002),
            ('6717834-41-2312',1574,960000,'자유적금','2018-7-30',1005,2004),
            ('6717834-52-3124',3574,4500000,'자유적금','2018-7-30',1006,2005),
            ('6717834-12-4123',1254,67300000,'자유적금','2018-7-30',1007,2006);
            

INSERT INTO ATM
VALUES      (3001,'충청북도 청주시 서원구 충대로 1 개신문화관 농협 1층',10000000,2003);


ALTER TABLE ACCOUNT
 ADD CONSTRAINT Account_user1 FOREIGN KEY (user_id) REFERENCES USER(user_id);
ALTER TABLE ACCOUNT
 ADD CONSTRAINT Account_bank FOREIGN KEY (bank_id) REFERENCES BANK(bank_id);

ALTER TABLE ATM
 ADD CONSTRAINT Atm_bank FOREIGN KEY (bank_id) REFERENCES BANK(bank_id);
 
ALTER TABLE OPERATE
 ADD CONSTRAINT Operate_trans FOREIGN KEY  (trans_id) REFERENCES TRANSACTION(trans_id);
ALTER TABLE OPERATE
 ADD CONSTRAINT Operate_account FOREIGN KEY  (user_id) REFERENCES USER(user_id);
ALTER TABLE OPERATE
 ADD CONSTRAINT Operate_atm FOREIGN KEY  (atm_id) REFERENCES ATM(atm_id); 
 
