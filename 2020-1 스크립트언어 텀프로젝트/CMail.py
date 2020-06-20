import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Mail:
    def __init__(self):
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.ehlo()
        self.session.starttls()#tls 연결모드(넷기에서배운듯 ㅋㅋ )
        self.session.ehlo()
        self.session.login('parksiyeon1020@gmail.com','meayskqrggkwsbwa')

    def MessageSet(self,receiver,lst,datelst,idx):
        msg = MIMEMultipart()

        address=["",]
        address.append(str(receiver))
        content=MIMEText("※"+str(lst[0][idx])+'의 대기 상태※\n'+'최신 업데이트: '+str(datelst[0:4])+'년 '+str(datelst[4:6])+'월 '+str(datelst[6:8])+'일 '+str(datelst[8:10])+"시 00분\n"+"\n상태: "+str(lst[1][idx])+"(수치:"+str(lst[2][idx]+")\n")+"미세먼지: "+str(lst[3][idx])+"㎍/㎥ \n"+"초미세먼지: "+str(lst[4][idx])+"㎍/㎥ \n"+"이산화질소: "+str(lst[5][idx])+"ppm\n"+"오존: "+str(lst[6][idx])+"ppm\n"+"일산화탄소: "+str(lst[7][idx])+"ppm\n"+"아황산가스: "+str(lst[8][idx])+"ppm")

        imgsource=open('emailattachimg.png','rb').read()
        img=MIMEImage(imgsource,name=os.path.basename('emailattachimg.png'))

        msg['Subject'] = '실시간 서울시 대기오염 상태'
        msg['From']="parksiyeon1020@gmail.com"
        msg['To']=",".join(address)

        msg.attach(content)
        msg.attach(img)

        self.session.sendmail('parksiyeon1020@gmail.com',address, msg.as_string())
        self.session.quit()

