from tkinter import *
from tkinter import font
import tkinter.ttk
import tkinter.messagebox
import mouse

class TermProj:
    def __init__(self):
        self.DataList= [[0]*25 for _ in range(9)]
        self.DataList.append([])
        self.favtimes=0
        self.FavList=[0 for _ in range(3)]
        self.findtimes=0
        self.index=0
        self.window = Tk()
        self.window.title("실시간 서울시 대기오염정보")
        self.window.geometry("1000x600+300+100")
        self.window.configure(bg="white")
        self.GetxmlFile()
        self.SetUIs()
        self.SetUIonFrame3()
        self.UpdateRecentDate()
        self.window.mainloop()

    def SetUIs(self):
        notebook = tkinter.ttk.Notebook(self.window, width=1000, height=600)
        notebook.pack()

        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        notebook.add(self.frame1, text="검색")
        notebook.add(self.frame2, text="상세비교")
        notebook.add(self.frame3, text="즐겨찾기")
        
        self.canvas1=Canvas(self.frame1,width=1000,height=600)
        self.canvas2 = Canvas(self.frame2, width=1000, height=600)
        self.canvas2.pack()

        self.label1 = Label(self.frame1, text="원하는 지역 검색 or 클릭", fg='black', font='helvetica 16')
        self.label1.pack()
        self.label1.place(x=100,y=50)
        self.label2 = Label(self.frame2, text="서울시 평균과 지역 비교", fg='black', font='helvetica 16')
        self.label2.pack()
        self.label2.place(x=100, y=50)

        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        TempFont1 = font.Font(self.window, size=10, weight='bold', family='Consolas')
        TempFont1 = font.Font(self.window, size=12, weight='bold',slant='italic', family='Consolas')
        self.EntryWidget = Entry(self.frame1, bd=5)
        self.EntryWidget.pack()
        self.EntryWidget.place(x=350,y=50)

        self.updateL = Label(self.frame1, text="", fg='black', font=TempFont1)
        self.updateL.pack()
        self.updateL.place(x=650, y=0)

        SearchButton = Button(self.frame1, font=TempFont, text="검색", command=self.SearchGu)
        SearchButton.pack()
        SearchButton.place(x=530, y=45)

        self.bg = PhotoImage(file='SeoulMap.png')
        GetClickL = Label(self.frame1, image=self.bg)
        GetClickL.pack()
        GetClickL.place(x=100, y=100)
        GetClickL.bind("<Button-1>",self.Clicked)

    def Clicked(self,event):
        self.posX = mouse.get_position()[0]  # 현재 마우스 포인터 좌표
        self.posY = mouse.get_position()[1]  # 현재 마우스 포인터 좌표
        self.GuList = [[631, 409, 676, 439],
                       [640, 445, 696, 466],
                       [628, 473, 679, 506],
                       [698, 451, 739, 483],
                       [743, 462, 781, 486],
                       [708, 410, 754, 446],
                       [750, 388, 793, 432],
                       [660, 385, 718, 415],
                       [655, 328, 713, 374],
                       [688, 285, 731, 345],
                       [730, 300, 785, 370],
                       [561, 350, 616, 405],
                       [585, 418, 639, 451],
                       [535, 441, 627, 478],
                       [492, 493, 547, 515],
                       [444, 418, 533, 471],
                       [479, 525, 565, 546],
                       [557, 561, 574, 571],
                       [560, 481, 602, 516],
                       [593, 511, 657, 539],
                       [592, 548, 653, 594],
                       [662, 528, 715, 581],
                       [710, 529, 752, 542],
                       [766, 514, 825, 526],
                       [799, 440, 859, 483] ]

        for i in range(25):
            if self.GuList[i][0] <= self.posX <= self.GuList[i][2]:
                if self.GuList[i][1] <= self.posY <= self.GuList[i][3]:
                    self.findtimes+=1
                    if self.findtimes==1:
                        self.ShowResult(i)
                        self.ShowPollutantList(i)
                        self.averageSeoul()
                        self.DrawGraph(i)
                    elif self.findtimes>=2:
                        self.UpdateResult(i)
                        self.ShowPollutantList(i)
                        self.averageSeoul()
                        self.DrawGraph(i)



    def SearchGu(self):
        self.findtimes+=1
        Entry=self.DataList[0].index(self.EntryWidget.get())
        if self.findtimes==1:
            self.ShowResult(Entry)
            self.ShowPollutantList(Entry)
            self.averageSeoul()
            self.DrawGraph(Entry)
        elif self.findtimes>=2:
            self.UpdateResult(Entry)
            self.ShowPollutantList(Entry)
            self.averageSeoul()
            self.DrawGraph(Entry)


    def UpdateResult(self,index):
        self.index=index
        self.Lname.configure(text=self.DataList[0][index]+" 대기 상태")
        self.LgradeStr.configure(text=self.DataList[1][index])
        self.Lgradenum.configure(text="(수치 "+self.DataList[2][index]+")")
        self.Lpm10.configure(text="미세먼지:" + self.DataList[3][index])
        self.Lpm25.configure(text="초미세먼지:" +self.DataList[4][index])
        self.Lnitro.configure(text="이산화질소:" +self.DataList[5][index])
        self.Lozone.configure(text="오존:" +self.DataList[6][index])
        self.Lcarbon.configure(text="일산화탄소:"+self.DataList[7][index])
        self.Lsurful.configure(text="아황산가스:" +self.DataList[8][index])

        self.GuName.configure(text="(" + str(self.DataList[0][index] + ")"))

        self.canvas2.delete(self.graph0)
        self.canvas2.delete(self.graph1)
        self.canvas2.delete(self.graph2)
        self.canvas2.delete(self.graph3)
        self.canvas2.delete(self.graph4)
        self.canvas2.delete(self.graph5)


    def ShowResult(self, index):
        self.index=index
        self.Lname = Label(self.frame1, text=str(self.DataList[0][index]), fg='black', font='helvetica 16')
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
        self.Baddfav=Button(self.frame1,text="즐겨찾기 등록",command=self.AddtoFav)
        self.Baddfav.pack()
        self.Baddfav.place(x=800,y=500)

    def SetUIonFrame3(self):
        lab=Label(self.frame3,text="나의 즐겨찾기 목록")
        lab.pack()
        lab.place(x=100,y=20)

        self.Bfav1=Button(self.frame3,text="Empty",command=self.ShowMyFav1)
        self.Bfav1.pack()
        self.Bfav1.place(x=50,y=100)
        self.Bfav2 = Button(self.frame3, text="Empty", command=self.ShowMyFav2)
        self.Bfav2.pack()
        self.Bfav2.place(x=50, y=150)
        self.Bfav3 = Button(self.frame3, text="Empty", command=self.ShowMyFav3)
        self.Bfav3.pack()
        self.Bfav3.place(x=50, y=200)

    def AddtoFav(self):
        self.FavList[self.favtimes]=self.index
        self.Lnamef3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.Lnamef3.pack()
        self.Lnamef3.place(x=700, y=50)
        self.LgradeStrf3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.LgradeStrf3.pack()
        self.LgradeStrf3.place(x=700, y=100)
        self.Lgradenumf3 = Label(self.frame3, text="", fg='black',font='helvetica 16')
        self.Lgradenumf3.pack()
        self.Lgradenumf3.place(x=750, y=100)
        self.Lpm10f3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.Lpm10f3.pack()
        self.Lpm10f3.place(x=700, y=200)
        self.Lpm25f3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.Lpm25f3.pack()
        self.Lpm25f3.place(x=700, y=250)
        self.Lnitrof3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.Lnitrof3.pack()
        self.Lnitrof3.place(x=700, y=300)
        self.Lozonef3 = Label(self.frame3, text="" , fg='black', font='helvetica 16')
        self.Lozonef3.pack()
        self.Lozonef3.place(x=700, y=350)
        self.Lcarbonf3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.Lcarbonf3.pack()
        self.Lcarbonf3.place(x=700, y=400)
        self.Lsurfulf3 = Label(self.frame3, text="", fg='black', font='helvetica 16')
        self.Lsurfulf3.pack()
        self.Lsurfulf3.place(x=700, y=450)

        if self.favtimes==0:
            self.Bfav1.configure(text=self.DataList[0][self.index])
        elif self.favtimes==1:
            self.Bfav2.configure(text=self.DataList[0][self.index])
        elif self.favtimes==2:
            self.Bfav3.configure(text=self.DataList[0][self.index])
        self.favtimes += 1

    def ShowMyFav1(self):
        self.Lnamef3.configure(text=str(self.DataList[0][self.FavList[0]]))
        self.LgradeStrf3.configure(text=str(self.DataList[1][self.FavList[0]]))
        self.Lgradenumf3.configure(text="(수치 " + str(self.DataList[2][self.FavList[0]]) + ")")
        self.Lpm10f3.configure(text="미세먼지:" + str(self.DataList[3][self.FavList[0]]))
        self.Lpm25f3.configure(text="초미세먼지:" + str(self.DataList[4][self.FavList[0]]))
        self.Lnitrof3.configure(text="이산화질소:" + str(self.DataList[5][self.FavList[0]]))
        self.Lozonef3.configure(text="오존:" + str(self.DataList[6][self.FavList[0]]))
        self.Lcarbonf3.configure(text="일산화탄소:" + str(self.DataList[7][self.FavList[0]]))
        self.Lsurfulf3.configure(text="아황산가스:" + str(self.DataList[8][self.FavList[0]]))
    def ShowMyFav2(self):
        self.Lnamef3.configure(text=str(self.DataList[0][self.FavList[1]]))
        self.LgradeStrf3.configure(text=str(self.DataList[1][self.FavList[1]]))
        self.Lgradenumf3.configure(text="(수치 " + str(self.DataList[2][self.FavList[1]]) + ")")
        self.Lpm10f3.configure(text="미세먼지:" + str(self.DataList[3][self.FavList[1]]))
        self.Lpm25f3.configure(text="초미세먼지:" + str(self.DataList[4][self.FavList[1]]))
        self.Lnitrof3.configure(text="이산화질소:" + str(self.DataList[5][self.FavList[1]]))
        self.Lozonef3.configure(text="오존:" + str(self.DataList[6][self.FavList[1]]))
        self.Lcarbonf3.configure(text="일산화탄소:" + str(self.DataList[7][self.FavList[1]]))
        self.Lsurfulf3.configure(text="아황산가스:" + str(self.DataList[8][self.FavList[1]]))

    def ShowMyFav3(self):
        self.Lnamef3.configure(text=str(self.DataList[0][self.FavList[2]]))
        self.LgradeStrf3.configure(text=str(self.DataList[1][self.FavList[2]]))
        self.Lgradenumf3.configure(text="(수치 " + str(self.DataList[2][self.FavList[2]]) + ")")
        self.Lpm10f3.configure(text="미세먼지:" + str(self.DataList[3][self.FavList[2]]))
        self.Lpm25f3.configure(text="초미세먼지:" + str(self.DataList[4][self.FavList[2]]))
        self.Lnitrof3.configure(text="이산화질소:" + str(self.DataList[5][self.FavList[2]]))
        self.Lozonef3.configure(text="오존:" + str(self.DataList[6][self.FavList[2]]))
        self.Lcarbonf3.configure(text="일산화탄소:" + str(self.DataList[7][self.FavList[2]]))
        self.Lsurfulf3.configure(text="아황산가스:" + str(self.DataList[8][self.FavList[2]]))


    def InitInputLabel(self):#검색칸
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

    def UpdateRecentDate(self):
        year = self.date[0:4]
        month = self.date[4:6]
        day = self.date[6:8]
        time=self.date[8:10]
        self.updateL.configure(text="업데이트 시간:" + year + "년 " + month + "월 " + day + "일 "+time+"시 "+"00분")

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

    def averageSeoul(self):
        self.sum = 0
        numtodivide=0
        self.average = [0] * 6

        #미세먼지
        for i in range(25):
            if self.DataList[3][i]!='점검중':
                self.sum += int(self.DataList[3][i])
                numtodivide+=1
        self.average[0] = self.sum /numtodivide
        self.sum = 0
        numtodivide=0

        #초미세
        for i in range(25):
            if self.DataList[4][i] != '점검중':
                self.sum += int(self.DataList[4][i])
                numtodivide+=1
        self.average[1] = self.sum /numtodivide
        self.sum = 0
        numtodivide=0

        #이산화질소
        for i in range(25):
            if self.DataList[5][i] != '점검중':
                self.sum += float(self.DataList[5][i])
                numtodivide+=1
        self.average[2] = self.sum/numtodivide
        self.sum = 0
        numtodivide=0

        #오존
        for i in range(25):
            if self.DataList[6][i] != '점검중':
                self.sum += float(self.DataList[6][i])
                numtodivide+=1
        self.average[3] = self.sum/numtodivide
        self.sum = 0
        numtodivide=0

        #일산화탄소
        for i in range(25):
            if self.DataList[7][i] != '점검중':
                self.sum += float(self.DataList[7][i])
                numtodivide+=1
        self.average[4] = self.sum/numtodivide
        self.sum = 0
        numtodivide=0

        #아황산가스
        for i in range(25):
            if self.DataList[8][i] != '점검중':
                self.sum += float(self.DataList[8][i])
                numtodivide+=1
        self.average[5] = self.sum/numtodivide
        self.sum = 0

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

        #미세먼지부터 아황산 가스

        if self.nullArray[0] != '점검중':
            self.graph0 = self.canvas2.create_rectangle(120, 450 - int(self.nullArray[0]), 140, 450, fill='black')
        if self.nullArray[1] != '점검중':
            self.graph1 = self.canvas2.create_rectangle(270, 450 - int(self.nullArray[1]), 290, 450, fill='black')
        if self.nullArray[2] != '점검중':
            self.graph2 = self.canvas2.create_rectangle(425, 450 - float(self.nullArray[2]) * 100, 445, 450, fill='black')
        if self.nullArray[3] != '점검중':
            self.graph3 = self.canvas2.create_rectangle(575, 450 - float(self.nullArray[3]) * 100, 595, 450, fill='black')
        if self.nullArray[4] != '점검중':
            self.graph4 = self.canvas2.create_rectangle(720, 450 - float(self.nullArray[4]) * 10, 740, 450, fill='black')
        if self.nullArray[5] != '점검중':
            self.graph5 = self.canvas2.create_rectangle(880, 450 - float(self.nullArray[5]) * 100, 900, 450, fill='black')

        self.canvas2.create_rectangle(60, 450 - int(self.average[0]), 80, 450, fill='black')
        self.canvas2.create_rectangle(210, 450 - int(self.average[1]), 230, 450, fill='black')
        self.canvas2.create_rectangle(365, 450 - float(self.average[2]) * 100, 385, 450, fill='black')
        self.canvas2.create_rectangle(515, 450 - float(self.average[3]) * 100, 535, 450, fill='black')
        self.canvas2.create_rectangle(665, 450 - float(self.average[4]) * 10, 685, 450, fill='black')
        self.canvas2.create_rectangle(825, 450 - float(self.average[5]) * 100, 845, 450, fill='black')





TermProj()