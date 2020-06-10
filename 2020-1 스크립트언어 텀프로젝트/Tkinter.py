from tkinter import *
from tkinter import font
import tkinter.ttk
import tkinter.messagebox

class TermProj:
    def __init__(self):
        self.DataList= [[0]*25 for _ in range(9)]
        self.DataList.append([])
        #self.searchKeyword=StringVar()
        self.window = Tk()
        self.window.title("실시간 서울시 대기오염정보")
        self.window.geometry("1000x600")
        self.window.configure(bg="white")
        #self.initSearchList()
        #self.initInputLabel()
        self.GetxmlFile()
        self.setLabelandButtons()
        #self.averageSeoul()


        self.window.mainloop()


    def setLabelandButtons(self):
        notebook = tkinter.ttk.Notebook(self.window, width=1000, height=600)
        notebook.pack()
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        notebook.add(self.frame1, text="검색")
        notebook.add(self.frame2, text="상세비교")
        self.label1 = Label(self.frame1, text="원하는 지역 검색 or 클릭", fg='black', font='helvetica 16')
        self.label1.pack()
        self.label1.place(x=100,y=50)
        self.label2 = Label(self.frame2, text="서울시 평균과 지역 비교", fg='black', font='helvetica 16')
        self.label2.pack()
        self.label2.place(x=100, y=50)
        self.bg = PhotoImage(file='SeoulMap.png')
        self.SeoulMap = Label(self.frame1, image=self.bg, bd=0)
        self.SeoulMap.pack()
        self.SeoulMap.place(x=100,y=100)
        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        self.EntryWidget = Entry(self.frame1, bd=5)
        self.EntryWidget.pack()
        self.EntryWidget.place(x=350,y=50)
        self.canvas = Canvas(self.frame2, width = 1000 , height = 600)
        self.canvas.pack()
        SearchButton = Button(self.frame1, font=TempFont, text="검색", command=self.SearchGu)
        SearchButton.pack()
        SearchButton.place(x=530, y=45)


    def SearchGu(self):
        Entry=self.DataList[0].index(self.EntryWidget.get())
        self.ShowResult(Entry)
        self.ShowPollutantList(Entry)
        self.DrawGraph(Entry)


    def ShowResult(self, index):
        #self.SeoulMap.configure(image='')
        #self.label1.configure(text="")
        print(str(self.DataList[0][index]))
        self.Lname = Label(self.frame1, text=str(self.DataList[0][index])+" 대기 상태", fg='black', font='helvetica 16')
        self.Lname.pack()
        self.Lname.place(x=700, y=50)
        self.LgradeStr = Label(self.frame1, text=str(self.DataList[1][index]), fg='black', font='helvetica 16')
        self.LgradeStr.pack()
        self.LgradeStr.place(x=700, y=100)
        self.Lgradenum = Label(self.frame1, text="(수치 "+str(self.DataList[2][index])+")", fg='black', font='helvetica 16')
        self.Lgradenum.pack()
        self.Lgradenum.place(x=750, y=100)
        self.Lpm10 = Label(self.frame1, text="미세먼지:" + str(self.DataList[3][index]), fg='black',font='helvetica 16')
        self.Lpm10.pack()
        self.Lpm10.place(x=700, y=200)
        self.Lpm25 = Label(self.frame1, text="초미세먼지:" + str(self.DataList[4][index]), fg='black', font='helvetica 16')
        self.Lpm25.pack()
        self.Lpm25.place(x=700, y=250)
        self.Lnitro = Label(self.frame1, text="이산화질소:" + str(self.DataList[5][index]), fg='black', font='helvetica 16')
        self.Lnitro.pack()
        self.Lnitro.place(x=700, y=300)
        self.Lozone = Label(self.frame1, text="오존:" + str(self.DataList[6][index]), fg='black', font='helvetica 16')
        self.Lozone.pack()
        self.Lozone.place(x=700, y=350)
        self.Lcarbon = Label(self.frame1, text="일산화탄소:" + str(self.DataList[7][index]), fg='black', font='helvetica 16')
        self.Lcarbon.pack()
        self.Lcarbon.place(x=700, y=400)
        self.Lsurful = Label(self.frame1, text="아황산가스:" + str(self.DataList[8][index]), fg='black', font='helvetica 16')
        self.Lsurful.pack()
        self.Lsurful.place(x=700, y=450)

    def initInputLabel(self):#검색칸
        global InputLabel
        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        InputLabel = Entry(self.window, font=TempFont, width=26, borderwidth=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=10, y=105)

    def GetxmlFile(self):
        import http.client
        from xml.dom.minidom import parse, parseString
        conn = http.client.HTTPConnection("openapi.seoul.go.kr:8088")
        conn.request("GET", "/624a754e616d696e35326b42565763/xml/ListAirQualityByDistrictService/1/25")
        req = conn.getresponse()

        # global DataList
        # self.DataList.clear()

        if req.status == 200:
            HaccpDoc = req.read().decode('utf-8')
            if HaccpDoc == None:
                print("에러")
            else:
                print("잘불러옴")
                self.parseData = parseString(HaccpDoc)
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

        #rotated = list(zip(*reversed(self.DataList)))
        for i in range(10):
            print(self.DataList[i])

    def averageSeoul(self):

        self.sum = 0
        self.average = [0] * 6

        #미세먼지
        for i in range(25):
            self.sum += int(self.DataList[3][i])
        self.average[0] = self.sum /25
        self.sum = 0

        #초미세
        for i in range(25):
            self.sum += int(self.DataList[4][i])
        self.average[1] = self.sum /25
        self.sum = 0

        #이산화질소
        for i in range(25):
            self.sum += float(self.DataList[5][i])
        self.average[2] = self.sum/25
        self.sum = 0

        #오존
        for i in range(25):
            self.sum += float(self.DataList[6][i])
        self.average[3] = self.sum/25
        self.sum = 0

        #일산화탄소
        for i in range(25):
            self.sum += float(self.DataList[7][i])
        self.average[4] = self.sum/25
        self.sum = 0

        #아황산가스
        for i in range(25):
            self.sum += float(self.DataList[8][i])
        self.average[5] = self.sum/25
        self.sum = 0

        for i in range(6):
            print(self.average[i])






    def ShowPollutantList(self, index):
        self.PollutantL1 = Label(self.frame2, text="평균 / 미세먼지", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50, y=480)

        self.PollutantL1 = Label(self.frame2, text="평균 / 초미세먼지", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50*3.9, y=480)

        self.PollutantL1 = Label(self.frame2, text="평균 / 이산화질소", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50*7.1, y=480)

        self.PollutantL1 = Label(self.frame2, text="평균 / 오존", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50*10.5, y=480)

        self.PollutantL1 = Label(self.frame2, text="평균 / 일산화탄소", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50*12.9, y=480)

        self.PollutantL1 = Label(self.frame2, text="평균 / 아황산가스", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50*16.2, y=480)

        for i in range(0, 6):
            self.GuName = Label(self.frame2, text="(" + str(self.DataList[0][index]) + ")", fg='black', font='helvetica 12')
            self.GuName.pack()
            self.GuName.place(x=95+(50*3.1*i), y=500)

    def DrawGraph(self, index):
        self.nullArray = [0] * 6
        startN = 3  #미세먼지부터 아황산 가스

        for i in range(0, 6):
            self.nullArray[i] = self.DataList[startN][index]
            startN += 1

        for i in range(6):
            print(self.nullArray[i])

        #미세먼지부터 아황산 가스

        self.canvas.create_rectangle(120, 450-int(self.nullArray[0]), 140, 450, fill='black')
        self.canvas.create_rectangle(270, 450-int(self.nullArray[1]), 290, 450, fill='black')
        self.canvas.create_rectangle(425, 450-float(self.nullArray[2])*100, 445, 450, fill='black')
        self.canvas.create_rectangle(575, 450-float(self.nullArray[3])*100, 595, 450, fill='black')
        self.canvas.create_rectangle(720, 450-float(self.nullArray[4])*10, 740, 450, fill='black')
        self.canvas.create_rectangle(880, 450-float(self.nullArray[5])*100, 900, 450, fill='black')

        self.canvas.create_rectangle(60, 450 - int(self.average[0]), 80, 450, fill='black')
        self.canvas.create_rectangle(210, 450 - int(self.average[1]), 230, 450, fill='black')
        self.canvas.create_rectangle(365, 450 - float(self.average[2]) * 100, 385, 450, fill='black')
        self.canvas.create_rectangle(515, 450 - float(self.average[3]) * 100, 535, 450, fill='black')
        self.canvas.create_rectangle(665, 450 - float(self.average[4]) * 10, 685, 450, fill='black')
        self.canvas.create_rectangle(825, 450 - float(self.average[5]) * 100, 845, 450, fill='black')










TermProj()