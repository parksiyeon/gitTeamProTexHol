import telepot
import time
import Tkinter
from telepot.loop import MessageLoop

token = '1157639195:AAElOOwbzdQAhliqYjeAqieNA3F7ImUXK9w'
bot = telepot.Bot(token)

update = bot.getUpdates()
#bot.sendMessage(chat_id = '1132666012', text="안녕하세요. 서울시 대기오염 체크 챗봇입니다.")

class chatBot:
def handleMain(msg):
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
    print(msg)
    if msg_type == 'text':
        for i in range(25):
            if Tkinter.self.DataList[0][i] == msg:
                search(i)
                #bot.sendMessage((chat_id, ))
        bot.sendMessage(chat_id, '그런 구는 없어요.')


def search(num):
    guName = Tkinter.DataList[0][num]
    pm10 = Tkinter.DataList[3][num]
    pm25 = Tkinter.DataList[4][num]
    nitrogen = Tkinter.DataList[5][num]
    ozon = Tkinter.DataList[6][num]
    carbon = Tkinter.DataList[7][num]
    sulfurous = Tkinter.DataList[8][num]

    update.message.reply_text('실시간'+guName+'대기오염 지수\n'
                                           '미세먼지'+pm10+'㎍/㎥\n'
                                           '초미세먼지'+pm25+'㎍/㎥\n'
                                           '이산화질소'+nitrogen+'ppm\n'
                                           '오존'+ozon+'ppm\n'
                                           '일산화탄소'+carbon+'ppm\n'
                                           '아황산가스'+sulfurous+'ppm\n')





MessageLoop(bot, handleMain).run_as_thread()
while True:
    time.sleep(10)