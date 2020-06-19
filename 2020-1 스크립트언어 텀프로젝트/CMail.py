import smtplib
from email.mime.text import MIMEText

class Mail:
    def __init__(self):
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.starttls()#tls 연결모드(넷기에서배운듯 ㅋㅋ )
        self.session.login('parksiyeon1020@gmail.com','meayskqrggkwsbwa')

    def MessageSet(self,lst,idx):
        msg = MIMEText(str(lst[0][idx]+'의 대기 상태 입니다.'))

        msg['Subject'] = '서울시 대기오염 상태'
        msg['From']='parksiyeon1020@gmail.com'
        msg['To']='potatochipskpu@gmail.com'

        self.session.sendmail('parksiyeon1020@gmail.com', 'potatochipskpu@gmail.com', msg.as_string())
        self.session.quit()

