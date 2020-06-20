# encoding=utf-8

import telepot
import telegram
import time
import os
from pprint import pprint
from telepot.loop import MessageLoop
import http.client
from xml.dom.minidom import parse, parseString

token = '1157639195:AAElOOwbzdQAhliqYjeAqieNA3F7ImUXK9w'
bot = telepot.Bot(token)
infoMsg = '서울시 대기오염을 보여줍니다.'+'\n'+'지역구를 입력해주세요.'

DataList = [[0] * 25 for _ in range(9)]
DataList.append([])

num = 0

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    #bot.sendMessage(chat_id, '서울시 대기오염 지수 체크봇입니다. \n 지역구를 입력해주세요.')

    if content_type != 'text':
        bot.sendMessage(chat_id, '텍스트만 이해할 수 있어요. . .')
    if content_type == 'text':
        response = msg['text']
        user = chat_id
        setData(response, user)
    if msg['text'] == 'ㅎㅇ' or msg['text']=='시작':
        bot.sendMessage(chat_id, infoMsg)

bot.message_loop(handle)

def setData(check, userN):
    conn = http.client.HTTPConnection("openapi.seoul.go.kr:8088")
    conn.request("GET", "/624a754e616d696e35326b42565763/xml/ListAirQualityByDistrictService/1/25")
    req = conn.getresponse()

    if req.status == 200:
        SeoulAirXml = req.read().decode('utf-8')
        if SeoulAirXml == None:
            print("에러")
        else:
            parseData = parseString(SeoulAirXml)
            Update = parseData.getElementsByTagName('MSRDATE')
            GuNameData = parseData.getElementsByTagName('MSRSTENAME')  # 구이름
            Pm10Data = parseData.getElementsByTagName('PM10')  # 미먼
            Pm25Data = parseData.getElementsByTagName('PM25')  # 초미세
            NitroData = parseData.getElementsByTagName('NITROGEN')  # 이산화질소
            OzoneData = parseData.getElementsByTagName('OZONE')  # 오존
            CarbonData = parseData.getElementsByTagName('CARBON')  # 일산화탄소
            SurfulSData = parseData.getElementsByTagName('SULFUROUS')  # 아황산

            if len(Update) > 0:
                xmltag = Update[0].toxml()
                date = xmltag.replace('<MSRDATE>', '').replace('</MSRDATE>', '')

    i = 0
    for one_tag in GuNameData:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<MSRSTENAME>', '').replace('</MSRSTENAME>', '')
        DataList[0][i] = xmlData
        i += 1
    i = 0
    for one_tag in Pm10Data:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<PM10>', '').replace('</PM10>', '')
        DataList[1][i] = xmlData
        i += 1
    i = 0
    for one_tag in Pm25Data:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<PM25>', '').replace('</PM25>', '')
        DataList[2][i] = xmlData
        i += 1
    i = 0
    for one_tag in NitroData:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<NITROGEN>', '').replace('</NITROGEN>', '')
        DataList[3][i] = xmlData
        i += 1

    i = 0
    for one_tag in OzoneData:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<OZONE>', '').replace('</OZONE>', '')
        DataList[4][i] = xmlData
        i += 1
    i = 0
    for one_tag in CarbonData:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<CARBON>', '').replace('</CARBON>', '')
        DataList[5][i] = xmlData
        i += 1
    i = 0
    for one_tag in SurfulSData:
        xmlTag = one_tag.toxml()
        xmlData = xmlTag.replace('<SULFUROUS>', '').replace('</SULFUROUS>', '')
        DataList[6][i] = xmlData
        i += 1
    i = 0

    for i in range(25):
        if DataList[0][i] == check:
            bot.sendMessage(userN,'지역구:'+ DataList[0][i] +'\n'+
                            '미세먼지'+ DataList[1][i] +'㎍ / ㎥\n'+
                            '초미세먼지'+ DataList[2][i] +'㎍ / ㎥\n'+
                            '이산화질소'+ DataList[3][i] +'ppm\n'+
                            '오존'+ DataList[4][i] +'ppm\n'+
                            '일산화탄소'+ DataList[5][i] +'ppm\n'+
                            '아황산가스'+ DataList[6][i]+"ppm")

while 1:
    time.sleep(10)