import smtplib
from email.mime.text import MIMEText

class Mail:
    def __init__(self):
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.ehlo()
        self.session.starttls()#tls 연결모드(넷기에서배운듯 ㅋㅋ )
        self.session.ehlo()
        self.session.login('parksiyeon1020@gmail.com','meayskqrggkwsbwa')

    def MessageSet(self,receiver,lst,idx):
        address=str(receiver)
        content=str(lst[0][idx])+'의 대기 상태 입니다.\n'+'업데이트 날짜:'+'\n'+"되나?"
        msg = MIMEText(content)

        msg['Subject'] = '실시간 서울시 대기오염 상태:'+str(lst[0][idx])
        msg['From']="parksiyeon1020@gmail.com"
        msg['To']=address

        self.session.sendmail('parksiyeon1020@gmail.com', [address], msg.as_string())
        self.session.quit()

