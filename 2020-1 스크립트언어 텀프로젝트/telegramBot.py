# encoding=utf-8

import telepot
import telegram
import os
import ChatBotParsing
from telepot.loop import MessageLoop

class talkBot:
    def __init__(self):
        self.token = '1157639195:AAElOOwbzdQAhliqYjeAqieNA3F7ImUXK9w'
        self.bot = telepot.Bot(self.token)
        self.id = 1132666012

        self.update = self.bot.getUpdates()

        self.bot.message.loop(self.TalkMe)

        me = self.bot.getMe()
        print(me)



    def TalkMe(self, msg):
        msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
        print(msg)
        if msg_type == 'text':
            if msg['text'] == '서울':
                self.bot.sendMessage(chat_id, '지역구를 입력해주세요')
                if msg_type == 'text':
                    for i in range(25):
                        if ChatBotParsing.self.DataList[0][i] == msg['text']:
                            self.sendData(i)

    def sendData(self, num):
        self.message.repay_text('지역구:'+ChatBotParsing.self.DataList[0][num]+'\n'+
                                '미세먼지'+ChatBotParsing.self.DataList[3][num]+'\n'+
                                '초미세먼지'+ChatBotParsing.self.DataList[4][num]+'\n'+
                                '이산화질소'+ChatBotParsing.self.DataList[5][num]+'\n'+
                                '오존'+ChatBotParsing.self.DataList[6][num]+'\n'+
                                '일산화탄소'+ChatBotParsing.self.DataList[7][num]+'\n'+
                                '아황산가스'+ChatBotParsing.self.DataList[8][num])




talkBot()