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
        address=["",]
        address.append(str(receiver))
        content="※"+str(lst[0][idx])+'의 대기 상태※\n'+'업데이트 날짜:'+'\n'+"상태: "+str(lst[1][idx])+"(수치:"+str(lst[2][idx]+")\n")+"미세먼지: "+str(lst[3][idx])+"㎍/㎥ \n"+"초미세먼지: "+str(lst[4][idx])+"㎍/㎥ \n"+"이산화질소: "+str(lst[5][idx])+"ppm\n"+"오존: "+str(lst[6][idx])+"ppm\n"+"일산화탄소: "+str(lst[7][idx])+"ppm\n"+"아황산가스:"+str(lst[8][idx])+"ppm"
        msg = MIMEText(content)

        msg['Subject'] = '실시간 서울시 대기오염 상태:'+str(lst[0][idx])
        msg['From']="parksiyeon1020@gmail.com"
        msg['To']=",".join(address)

        self.session.sendmail('parksiyeon1020@gmail.com',address, msg.as_string())
        self.session.quit()

