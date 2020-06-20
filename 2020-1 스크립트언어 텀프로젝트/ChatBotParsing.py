import telegram
from bs4 import *
import requests
import time
import telegramBot
from telepot.loop import MessageLoop

class setData:
    def __init__(self):
        self.token = '1157639195:AAElOOwbzdQAhliqYjeAqieNA3F7ImUXK9w'
        self.bot = telegram.Bot(self.token)
        id = 1132666012

        self.DataList = [[0] * 25 for _ in range(9)]
        self.DataList.append([])
        self.GetxmlFile()
        self.printData()

        update = self.bot.getUpdates()

        self.bot.getMe() # 텔레그램 정보 확인용
        self.startChat()

    def GetxmlFile(self):
        import http.client
        from xml.dom.minidom import parse, parseString
        conn = http.client.HTTPConnection("openapi.seoul.go.kr:8088")
        conn.request("GET", "/624a754e616d696e35326b42565763/xml/ListAirQualityByDistrictService/1/25")
        req = conn.getresponse()

        if req.status == 200:
            SeoulAirXml = req.read().decode('utf-8')
            if SeoulAirXml == None:
                print("에러")
            else:
                self.parseData = parseString(SeoulAirXml)
                self.Update=self.parseData.getElementsByTagName('MSRDATE')
                self.GuNameData=self.parseData.getElementsByTagName('MSRSTENAME')#구이름
                self.GradeMaxIndex=self.parseData.getElementsByTagName('MAXINDEX')#대기상태 숫자수치
                self.GradeData = self.parseData.getElementsByTagName('GRADE')#보통 나쁨 그거..
                self.Pm10Data = self.parseData.getElementsByTagName('PM10')#미먼
                self.Pm25Data = self.parseData.getElementsByTagName('PM25')#초미세
                self.NitroData=self.parseData.getElementsByTagName('NITROGEN') #이산화질소
                self.OzoneData = self.parseData.getElementsByTagName('OZONE')  # 오존
                self.CarbonData = self.parseData.getElementsByTagName('CARBON')  # 일산화탄소
                self.SurfulSData = self.parseData.getElementsByTagName('SULFUROUS')  # 아황산

                if len(self.Update)>0:
                    xmltag=self.Update[0].toxml()
                    self.date=xmltag.replace('<MSRDATE>','').replace('</MSRDATE>','')


        self.SetDatastoList()

    def SetDatastoList(self):
        i=0
        for one_tag in self.GuNameData:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<MSRSTENAME>', '').replace('</MSRSTENAME>', '')
            self.DataList[0][i]=self.xmlData
            i+=1
        i=0
        for one_tag in self.GradeData:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<GRADE>', '').replace('</GRADE>', '')
            self.DataList[1][i]=self.xmlData
            i += 1
        i=0
        for one_tag in self.GradeMaxIndex:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<MAXINDEX>', '').replace('</MAXINDEX>', '')
            self.DataList[2][i]=self.xmlData
            i += 1
        i=0
        for one_tag in self.Pm10Data:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<PM10>', '').replace('</PM10>', '')
            self.DataList[3][i]=self.xmlData
            i += 1
        i=0
        for one_tag in self.Pm25Data:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<PM25>', '').replace('</PM25>', '')
            self.DataList[4][i]=self.xmlData
            i += 1
        i = 0
        for one_tag in self.NitroData:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<NITROGEN>', '').replace('</NITROGEN>', '')
            self.DataList[5][i]=self.xmlData
            i += 1

        i = 0
        for one_tag in self.OzoneData:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<OZONE>', '').replace('</OZONE>', '')
            self.DataList[6][i] = self.xmlData
            i += 1
        i = 0
        for one_tag in self.CarbonData:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<CARBON>', '').replace('</CARBON>', '')
            self.DataList[7][i] = self.xmlData
            i += 1
        i = 0
        for one_tag in self.SurfulSData:
            self.xmlTag = one_tag.toxml()
            self.xmlData = self.xmlTag.replace('<SULFUROUS>', '').replace('</SULFUROUS>', '')
            self.DataList[8][i] = self.xmlData
            i += 1
        i = 0

    def printData(self):
        for i in range(25):
            print(self.DataList[0][i])


    def startChat(self):
        # 구현해야하는 것 - 사용자가 아무말이나 치면 아무말에서 얻은 id 값으로 '~체크 봇입니다' 출력하기
        self.chat_id = self.bot.getUpdates()[-1].message.chat.id
        print('user id :', self.chat_id)
        self.bot.sendMessage(self.chat_id, '서울 대기오염 체크봇입니다.')



setData()