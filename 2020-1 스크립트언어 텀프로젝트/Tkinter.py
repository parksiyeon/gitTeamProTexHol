from tkinter import *
from tkinter import font
import tkinter.ttk
import tkinter.messagebox

class TermProj:
    def __init__(self):
        self.DataList= [[0]*25 for _ in range(10)]
        self.DataList.append([])
        self.window = Tk()
        self.window.title("실시간 서울시 대기오염정보")
        self.window.geometry("1000x600")
        self.window.configure(bg="white")
        #self.initSearchList()
        #self.initInputLabel()
        self.GetxmlFile()
        self.setLabelandButtons()
        self.window.mainloop()


    def setLabelandButtons(self):
        notebook = tkinter.ttk.Notebook(self.window, width=1000, height=600)
        notebook.pack()
        self.frame1 = Frame(self.window)
        self.frame2=Frame(self.window)
        notebook.add(self.frame1, text="검색")
        notebook.add(self.frame2, text="상세뭐시기")
        label1 = Label(self.frame1, text="조회를 원하는 지역을 클릭하세요", fg='black', font='helvetica 16')
        label1.pack()
        label1.place(x=100,y=50)
        self.bg = PhotoImage(file='SeoulMap.png')
        self.SeoulMap = Label(self.frame1, image=self.bg, bd=0, bg='green')
        self.SeoulMap.pack()
        self.SeoulMap.place(x=250,y=100)
        TempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
        # SearchButton = Button(self.window, font=TempFont, text="검색", command=self.GetxmlFile())
        # SearchButton.pack()
        # SearchButton.place(x=330, y=110)

    def initInputLabel(self):#검색칸
        global InputLabel
        TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        InputLabel = Entry(self.window, font=TempFont, width=26, borderwidth=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=10, y=105)

    # def initSearchList(self):
    #     global SearchBox
    #     self.SearchList = Scrollbar(self.window)
    #     self.SearchList.pack()
    #     self.SearchList.place(x=150, y=0)

        # TempFont = font.Font(self.window, size=15, weight='bold')
        # self.SearchBox = Listbox(self.window, font=TempFont, activestyle='none', width= 12, height=1,borderwidth=7, yscrollcommand= self.SearchList.set)
        # self.SearchBox.insert(0, "제품 이름")  #xml에서 제품명
        # self.SearchBox.insert(1, "제품 유형")  #xml에서 유형명
        # self.SearchBox.pack()
        # self.SearchBox.place(x=0, y=0)
        # self.SearchList.config(command=self.SearchBox.yview)

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
                self.GuNmaeData=self.parseData.getElementsByTagName('MSRSTENAME')#구이름
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
        for one_tag in self.GuNmaeData:
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
        # for one_tag in self.Pm25Data:
        #     self.xmlTag = one_tag.toxml()
        #     self.xmlData = self.xmlTag.replace('<PM25>', '').replace('</PM25>', '')
        #     self.DataList[9][i] = self.xmlData
        #     i += 1
        i = 0



        rotated = list(zip(*reversed(self.DataList)))
        for i in range(10):
            print(self.DataList[i])

TermProj()