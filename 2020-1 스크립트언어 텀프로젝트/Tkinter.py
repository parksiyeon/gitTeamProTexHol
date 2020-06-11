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

        self.label2 = Label(self.frame2, text="서울시 대기 평균과의 비교", fg='black', font='helvetica 16')
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
                        self.printAverL()
                    elif self.findtimes>=2:
                        self.resetMatterN()
                        self.UpdateResult(i)
                        self.ShowPollutantList(i)
                        self.averageSeoul()
                        self.DrawGraph(i)




    def SearchGu(self):
        self.findtimes+=1
        Entry=self.DataList[0].index(self.EntryWidget.get())
        self.ShowPollutantList(Entry) #그래프 하단 라벨 세팅 함수. 두번부를필요 ㄴㄴ
        if self.findtimes==1:
            self.ShowResult(Entry)
            self.averageSeoul()
            self.DrawGraph(Entry)
        elif self.findtimes>=2:
            self.resetMatterN()
            self.UpdateResult(Entry)
            self.averageSeoul()
            self.DrawGraph(Entry)


    def UpdateResult(self,index):
        self.index=index
        self.Lname.configure(text=self.DataList[0][index])
        self.LgradeStr.configure(text=self.DataList[1][index])
        self.Lgradenum.configure(text="(수치 "+self.DataList[2][index]+")")
        self.Lpm10.configure(text="미세먼지:" + self.DataList[3][index])
        self.Lpm25.configure(text="초미세먼지:" +self.DataList[4][index])
        self.Lnitro.configure(text="이산화질소:" +self.DataList[5][index])
        self.Lozone.configure(text="오존:" +self.DataList[6][index])
        self.Lcarbon.configure(text="일산화탄소:"+self.DataList[7][index])
        self.Lsurful.configure(text="아황산가스:" +self.DataList[8][index])
        self.GuName.configure(text="")
        self.GuName.configure(text=self.DataList[0][index])

        self.canvas2.delete(self.graph0)
        self.canvas2.delete(self.graph1)
        self.canvas2.delete(self.graph2)
        self.canvas2.delete(self.graph3)
        self.canvas2.delete(self.graph4)
        self.canvas2.delete(self.graph5)

        self.canvas2.delete(self.averGraph0)
        self.canvas2.delete(self.averGraph1)
        self.canvas2.delete(self.averGraph2)
        self.canvas2.delete(self.averGraph3)
        self.canvas2.delete(self.averGraph4)
        self.canvas2.delete(self.averGraph5)


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
        self.average[0] = round(self.sum /numtodivide, 1)
        self.sum = 0
        numtodivide=0

        #초미세
        for i in range(25):
            if self.DataList[4][i] != '점검중':
                self.sum += int(self.DataList[4][i])
                numtodivide+=1
        self.average[1] = round(self.sum /numtodivide, 1)
        self.sum = 0
        numtodivide=0

        #이산화질소
        for i in range(25):
            if self.DataList[5][i] != '점검중':
                self.sum += float(self.DataList[5][i])
                numtodivide+=1
        self.average[2] = round(self.sum /numtodivide, 3)
        self.sum = 0
        numtodivide=0

        #오존
        for i in range(25):
            if self.DataList[6][i] != '점검중':
                self.sum += float(self.DataList[6][i])
                numtodivide+=1
        self.average[3] = round(self.sum /numtodivide, 1)
        self.sum = 0
        numtodivide=0

        #일산화탄소
        for i in range(25):
            if self.DataList[7][i] != '점검중':
                self.sum += float(self.DataList[7][i])
                numtodivide+=1
        self.average[4] = round(self.sum /numtodivide, 2)
        self.sum = 0
        numtodivide=0

        #아황산가스
        for i in range(25):
            if self.DataList[8][i] != '점검중':
                self.sum += float(self.DataList[8][i])
                numtodivide+=1
        self.average[5] = round(self.sum /numtodivide, 4)
        self.sum = 0



    def ShowPollutantList(self, index):
        print(self.findtimes)
        self.PollutantL0 = Label(self.frame2, text="평균 / 선택지역", fg='black', font='helvetica 12')
        self.PollutantL0.pack()
        self.PollutantL0.place(x=50, y=480)

        self.PollutantL1 = Label(self.frame2, text="평균 / 선택지역", fg='black', font='helvetica 12')
        self.PollutantL1.pack()
        self.PollutantL1.place(x=50*4, y=480)

        self.PollutantL2 = Label(self.frame2, text="평균 / 선택지역", fg='black', font='helvetica 12')
        self.PollutantL2.pack()
        self.PollutantL2.place(x=50*7.2, y=480)

        self.PollutantL3 = Label(self.frame2, text="평균 / 선택지역", fg='black', font='helvetica 12')
        self.PollutantL3.pack()
        self.PollutantL3.place(x=50*10.4, y=480)

        self.PollutantL4 = Label(self.frame2, text="평균 / 선택지역", fg='black', font='helvetica 12')
        self.PollutantL4.pack()
        self.PollutantL4.place(x=50*12.9, y=480)

        self.PollutantL5 = Label(self.frame2, text="평균 / 선택지역", fg='black', font='helvetica 12')
        self.PollutantL5.pack()
        self.PollutantL5.place(x=50*16.2, y=480)

        self.GuName = Label(self.frame2, text=str(self.DataList[0][index]), fg='black', font='helvetica 15')
        self.GuName.pack()
        self.GuName.place(x=400, y=50)

        self.matterName1 = Label(self.frame2, text = "["+"미세먼지"+"]", fg = 'black', font='helvetica 12')
        self.matterName1.pack()
        self.matterName1.place(x=70 , y=500)

        self.matterName2 = Label(self.frame2, text = "["+"초미세먼지"+"]", fg = 'black', font='helvetica 12')
        self.matterName2.pack()
        self.matterName2.place(x=210, y=500)

        self.matterName3 = Label(self.frame2, text = "["+"이산화질소"+"]", fg = 'black', font='helvetica 12')
        self.matterName3.pack()
        self.matterName3.place(x=370, y=500)

        self.matterName4 = Label(self.frame2, text = "["+"오존"+"]", fg = 'black', font='helvetica 12')
        self.matterName4.pack()
        self.matterName4.place(x=550, y=500)

        self.matterName5 = Label(self.frame2, text = "["+"일산화탄소"+"]", fg = 'black', font='helvetica 12')
        self.matterName5.pack()
        self.matterName5.place(x=655, y=500)

        self.matterName6 = Label(self.frame2, text = "["+"아황산가스"+"]", fg = 'black', font='helvetica 12')
        self.matterName6.pack()
        self.matterName6.place(x=820, y=500)

    def DrawGraph(self, index):
        self.nullArray = [0] * 6
        startN = 3  #미세먼지부터 아황산 가스


        for i in range(0, 6):
            self.nullArray[i] = self.DataList[startN][index]
            startN += 1

        #미세먼지부터 아황산 가스

        if self.nullArray[0] != '점검중':
            self.graph0 = self.canvas2.create_rectangle(120, 450 - int(self.nullArray[0])*5, 140, 450, fill='black')
            self.pollutantValue0 = Label(self.frame2, text=str(self.nullArray[0]), fg='black',font='helvetica 12',tags='label')
            self.pollutantValue0.pack()
            self.pollutantValue0.place(x=110, y=400 - int(self.nullArray[0])*5)

        if self.nullArray[1] != '점검중':
            self.graph1 = self.canvas2.create_rectangle(270, 450 - int(self.nullArray[1])*5, 290, 450, fill='black')
            self.pollutantValue1 = Label(self.frame2, text=str(self.nullArray[1]), fg='black',font='helvetica 12',tags='label')
            self.pollutantValue1.pack()
            self.pollutantValue1.place(x=265, y=400 - int(self.nullArray[1])*5)

        if self.nullArray[2] != '점검중':
            self.graph2 = self.canvas2.create_rectangle(425, 450 - float(self.nullArray[2]) * 100, 445, 450, fill='black')
            self.pollutantValue2 = Label(self.frame2, text=str(self.nullArray[2]), fg='black',font='helvetica 12',tags='label')
            self.pollutantValue2.pack()
            self.pollutantValue2.place(x=415, y=400 - float(self.nullArray[2]))

        if self.nullArray[3] != '점검중':
            self.graph3 = self.canvas2.create_rectangle(575, 450 - float(self.nullArray[3]) * 100, 595, 450, fill='black')
            self.pollutantValue3 = Label(self.frame2, text=str(self.nullArray[3]), fg='black',font='helvetica 12',tags='label')
            self.pollutantValue3.pack()
            self.pollutantValue3.place(x=557, y=400 - float(self.nullArray[3]))

        if self.nullArray[4] != '점검중':
            self.graph4 = self.canvas2.create_rectangle(720, 450 - float(self.nullArray[4]) * 10, 740, 450, fill='black')
            self.pollutantValue4 = Label(self.frame2, text=str(self.nullArray[4]), fg='black',font='helvetica 12',tags='label')
            self.pollutantValue4.pack()
            self.pollutantValue4.place(x=707, y=400 - float(self.nullArray[4]))

        if self.nullArray[5] != '점검중':
            self.graph5 = self.canvas2.create_rectangle(880, 450 - float(self.nullArray[5]) * 100, 900, 450, fill='black')
            self.pollutantValue5 = Label(self.frame2, text=str(self.nullArray[5]), fg='black',font='helvetica 12',tags='label')
            self.pollutantValue5.pack()
            self.pollutantValue5.place(x=865, y=400 - float(self.nullArray[5]))

        self.averGraph0 = self.canvas2.create_rectangle(60, 450 - int(self.average[0]*5), 80, 450, fill='black')
        self.averGraph1 = self.canvas2.create_rectangle(210, 450 - int(self.average[1]*5), 230, 450, fill='black')
        self.averGraph2 = self.canvas2.create_rectangle(365, 450 - float(self.average[2]) * 100, 385, 450, fill='black')
        self.averGraph3 = self.canvas2.create_rectangle(515, 450 - float(self.average[3]) * 100, 535, 450, fill='black')
        self.averGraph4 = self.canvas2.create_rectangle(665, 450 - float(self.average[4]) * 10, 685, 450, fill='black')
        self.averGraph5 = self.canvas2.create_rectangle(825, 450 - float(self.average[5]) * 100, 845, 450, fill='black')


    def printAverL(self):
        self.averageValue0 = Label(self.frame2, text=str(self.average[0]), fg='black', font='helvetica 12',tags='label')
        self.averageValue0.pack()
        self.averageValue0.place(x=52, y=400 - int(self.average[0]) * 5)

        self.averageValue1 = Label(self.frame2, text=str(self.average[1]), fg='black', font='helvetica 12',tags='label')
        self.averageValue1.pack()
        self.averageValue1.place(x=195, y=400 - int(self.average[1]) * 5)

        self.averageValue2 = Label(self.frame2, text=str(self.average[2]), fg='black', font='helvetica 12',tags='label')
        self.averageValue2.pack()
        self.averageValue2.place(x=345, y=400 - int(self.average[2]))

        self.averageValue3 = Label(self.frame2, text=str(self.average[3]), fg='black', font='helvetica 12',tags='label')
        self.averageValue3.pack()
        self.averageValue3.place(x=505, y=400 - int(self.average[3]))

        self.averageValue4 = Label(self.frame2, text=str(self.average[4]), fg='black', font='helvetica 12',tags='label')
        self.averageValue4.pack()
        self.averageValue4.place(x=652, y=400 - int(self.average[4]))

        self.averageValue5 = Label(self.frame2, text=str(self.average[5]), fg='black', font='helvetica 12',tags='label')
        self.averageValue5.pack()
        self.averageValue5.place(x=795, y=400 - int(self.average[5]))

    def resetMatterN(self):
        self.canvas2.delete('label')






TermProj()
