#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#||$Scipt By : Kanad Nemade(Github: Arduino3128)                  ||                       
#||                                                               ||           
#||$Project Page: "https://arduino3128.github.io/CoronaDashboard" ||   
#||                                                               ||   
#||$Liscense: Eclipse Public License 2.0                          ||  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5 import QtWebEngineWidgets
    from PyQt5.QtCore import QThread ,pyqtSignal
    import requests
    import json
    import time
    import os
    import sys
    from sys import exit
    datanum=False
    print("Debug Terminal:")
    english=['Select Location:','Manually','Automatically','Locate Nearby:','Govt. Hospital','Food Shelters','Night Shelter','Submit','Map:','State:','Confirmed','Active','Recovered','Deaths:','District:','Zone Type:',' Detecting',' Not Found']
    lang='en'
    langopt=english
    langColor=['RED','ORANGE','YELLOW','GREEN']
    try:
        os.mkdir("temp")
    except:
        pass

    class Thrd(QThread):
        print('Thrd')
        basic=pyqtSignal(int)
        def run(self):
            print("run",lang)
            urlip="https://api.ipify.org/"
            ip=requests.get(urlip)
            ip=str(ip.content)
            ip=ip.replace('b','')
            ip=ip.replace("'","")
            urloc="https://tools.keycdn.com/geo.json?host=%s"%ip
            loca=requests.get(urloc)
            try:
                with open("temp/loc.json",'wb') as dat:
                    dat.write(loca.content)
                dat.close()
                with open("temp/loc.json",'rb') as dat:
                    loca=json.load(dat)
                dat.close()
            except:
                self.Ui_MainWindow.Serverror()
            lat=loca['data']['geo']['latitude']
            long=loca['data']['geo']['longitude']
            url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"
            querystring = {"language":"en","location_type":"APPROXIMATE","latlng":"%s,%s"%(lat,long)}
            headers = {
                'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
                'x-rapidapi-key': "YOUR RAPID_API_KEY"
                }   
            responseen = requests.request("GET", url, headers=headers, params=querystring)
            try:
                with open("temp/loc.json",'wb') as dat:
                    dat.write(responseen.content)
                dat.close()
            except:
                self.Ui_MainWindow.Serverror()
            if lang!='en':
                url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"
                querystring = {"language":lang,"location_type":"APPROXIMATE","latlng":"%s,%s"%(lat,long)}
                headers = {
                    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
                    'x-rapidapi-key': "YOUR RAPID_API_KEY"
                   }
                response = requests.request("GET", url, headers=headers, params=querystring)
                try:
                    with open("temp/loclang.json",'wb') as dat:
                        dat.write(response.content)
                    dat.close()
                except:
                    self.Ui_MainWindow.Serverror()
            print("Returning")
            self.basic.emit(1)
        
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow,langopt,lang):
            MainWindow.setObjectName("MainWindow")
            MainWindow.setEnabled(True)
            MainWindow.resize(800, 640)
            MainWindow.setWindowIcon(QtGui.QIcon("Logo.png"))
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.Submit = QtWidgets.QPushButton(self.centralwidget)
            self.Submit.setGeometry(QtCore.QRect(50, 265, 75, 28))
            self.Submit.setAutoFillBackground(False)
            font = QtGui.QFont()
            font.setPointSize(10)
            if lang=='as':
                try:
                    font.setFamily("Mitra-Mono")
                except:
                    subprocess.call("copy mitra.ttf %s\Fonts"%os.environ['WINDIR'],shell=True)
                    font.setFamily("Mitra-Mono")
            self.Submit.setFont(font)
            self.Submit.setObjectName("Submit")
            self.label1 = QtWidgets.QLabel(self.centralwidget)
            self.label1.setGeometry(QtCore.QRect(50, 40, 341, 71))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setPointSize(26)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            self.label1.setFont(font)
            self.label1.setObjectName("label1")
            self.State = QtWidgets.QLineEdit(self.centralwidget)
            self.State.setGeometry(QtCore.QRect(50, 190, 231, 20))
            self.State.setObjectName("State")
            self.Dist = QtWidgets.QLineEdit(self.centralwidget)
            self.Dist.setGeometry(QtCore.QRect(50, 230, 231, 20))
            self.Dist.setObjectName("Dist")
            self.Manually = QtWidgets.QCheckBox(self.centralwidget)
            self.Manually.setGeometry(QtCore.QRect(50, 160, 71, 21))
            self.Manually.setLayoutDirection(QtCore.Qt.RightToLeft)
            font = QtGui.QFont()
            font.setPointSize(10)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            self.Manually.setFont(font)
            self.Manually.setObjectName("Manually")
            self.Automatically = QtWidgets.QCheckBox(self.centralwidget)
            self.Automatically.setGeometry(QtCore.QRect(135, 160, 95, 21))
            self.Automatically.setLayoutDirection(QtCore.Qt.RightToLeft)
            font = QtGui.QFont()
            font.setPointSize(10)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            self.Automatically.setFont(font)
            self.Automatically.setObjectName("Automatically")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(60, 120, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.StateLab = QtWidgets.QLabel(self.centralwidget)
            self.StateLab.setGeometry(QtCore.QRect(500, 60, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(14)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.StateLab.setFont(font)
            self.StateLab.setObjectName("StateLab")
            self.state_confirmed = QtWidgets.QLabel(self.centralwidget)
            self.state_confirmed.setGeometry(QtCore.QRect(500, 110, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.state_confirmed.setFont(font)
            self.state_confirmed.setObjectName("state_confirmed")
            self.state_active = QtWidgets.QLabel(self.centralwidget)
            self.state_active.setGeometry(QtCore.QRect(500, 155, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.state_active.setFont(font)
            self.state_active.setObjectName("state_active")
            self.state_recovered = QtWidgets.QLabel(self.centralwidget)
            self.state_recovered.setGeometry(QtCore.QRect(500, 200, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.state_recovered.setFont(font)
            self.state_recovered.setObjectName("state_recovered")
            self.SRecoveredLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.SRecoveredLCD.setGeometry(QtCore.QRect(613, 200, 80, 30))
            self.SRecoveredLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.SRecoveredLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SRecoveredLCD.setDigitCount(6)
            self.SRecoveredLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.SRecoveredLCD.setProperty("intValue", 0)
            self.SRecoveredLCD.setObjectName("SRecoveredLCD")
            self.state_deaths = QtWidgets.QLabel(self.centralwidget)
            self.state_deaths.setGeometry(QtCore.QRect(500, 245, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.state_deaths.setFont(font)
            self.state_deaths.setObjectName("state_deaths")
            self.dist_zone = QtWidgets.QLabel(self.centralwidget)
            self.dist_zone.setGeometry(QtCore.QRect(500, 495, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.dist_zone.setFont(font)
            self.dist_zone.setObjectName("dist_zone")
            self.dist_deaths = QtWidgets.QLabel(self.centralwidget)
            self.dist_deaths.setGeometry(QtCore.QRect(500, 450, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.dist_deaths.setFont(font)
            self.dist_deaths.setObjectName("dist_deaths")
            self.dist_confirmed = QtWidgets.QLabel(self.centralwidget)
            self.dist_confirmed.setGeometry(QtCore.QRect(500, 360, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.dist_confirmed.setFont(font)
            self.dist_confirmed.setObjectName("dist_confirmed")
            self.DistLab = QtWidgets.QLabel(self.centralwidget)
            self.DistLab.setGeometry(QtCore.QRect(500, 300, 151, 31))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(14)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.DistLab.setFont(font)
            self.DistLab.setObjectName("DistLab")
            self.dist_recovered = QtWidgets.QLabel(self.centralwidget)
            self.dist_recovered.setGeometry(QtCore.QRect(500, 405, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.dist_recovered.setFont(font)
            self.dist_recovered.setObjectName("dist_recovered")
            self.ZoneColor = QtWidgets.QLabel(self.centralwidget)
            self.ZoneColor.setEnabled(True)
            self.ZoneColor.setGeometry(QtCore.QRect(0, 0, 800, 600))
            self.ZoneColor.setText("")
            self.ZoneColor.setPixmap(QtGui.QPixmap("Blue.png"))
            self.ZoneColor.setObjectName("ZoneColor")
            self.dist_active_2 = QtWidgets.QLabel(self.centralwidget)
            self.dist_active_2.setGeometry(QtCore.QRect(613, 495, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(False)
            font.setWeight(50)
            self.dist_active_2.setFont(font)
            self.dist_active_2.setObjectName("dist_active_2")
            self.GovtHosp = QtWidgets.QPushButton(self.centralwidget)
            self.GovtHosp.setGeometry(QtCore.QRect(310, 160, 100, 31))
            font = QtGui.QFont()
            font.setPointSize(10)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            self.GovtHosp.setFont(font)
            self.GovtHosp.setObjectName("GovtHosp")
            self.LocShow = QtWidgets.QLabel(self.centralwidget)
            self.LocShow.setGeometry(QtCore.QRect(290, 130, 141, 20))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.LocShow.setFont(font)
            self.LocShow.setObjectName("LocShow")
            self.FoodShel = QtWidgets.QPushButton(self.centralwidget)
            self.FoodShel.setGeometry(QtCore.QRect(310, 200, 100, 31))
            font = QtGui.QFont()
            font.setPointSize(10)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(False)
            self.FoodShel.setFont(font)
            self.FoodShel.setObjectName("FoodShel")
            self.NightShel = QtWidgets.QPushButton(self.centralwidget)
            self.NightShel.setGeometry(QtCore.QRect(310, 240, 100, 31))
            font = QtGui.QFont()
            font.setPointSize(10)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            self.NightShel.setFont(font)
            self.NightShel.setObjectName("NightShel")
            self.Browser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
            self.Browser.setGeometry(QtCore.QRect(50, 300, 441, 261))
            self.Browser.setObjectName("Browser")
            self.Browser.setUrl(QtCore.QUrl("https://arduino3128.github.io/CoronaDashboard/"))
            self.Browser.show()
            self.line = QtWidgets.QFrame(self.Browser)
            self.line.setGeometry(QtCore.QRect(-17, 220, 20, 21))
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.line_2 = QtWidgets.QFrame(self.centralwidget)
            self.line_2.setGeometry(QtCore.QRect(50, 290, 441, 16))
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            self.line_2.setFont(font)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
            self.line_2.setLineWidth(2)
            self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_2.setObjectName("line_2")
            self.line_3 = QtWidgets.QFrame(self.centralwidget)
            self.line_3.setGeometry(QtCore.QRect(50, 551, 441, 20))
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            self.line_3.setFont(font)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
            self.line_3.setLineWidth(2)
            self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_3.setObjectName("line_3")
            self.line_4 = QtWidgets.QFrame(self.centralwidget)
            self.line_4.setGeometry(QtCore.QRect(470, 299, 41, 261))
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            self.line_4.setFont(font)
            self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
            self.line_4.setLineWidth(2)
            self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_4.setObjectName("line_4")
            self.line_5 = QtWidgets.QFrame(self.centralwidget)
            self.line_5.setGeometry(QtCore.QRect(31, 299, 41, 261))
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            self.line_5.setFont(font)
            self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
            self.line_5.setLineWidth(2)
            self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_5.setObjectName("line_5")
            self.Map = QtWidgets.QLabel(self.centralwidget)
            self.Map.setGeometry(QtCore.QRect(210, 270, 61, 20))
            font = QtGui.QFont()
            font.setFamily("Quicksand")
            font.setPointSize(12)
            if lang=='as':
                font.setFamily("Mitra-Mono")
            font.setBold(True)
            font.setWeight(75)
            self.Map.setFont(font)
            self.Map.setObjectName("Map")
            self.SConfirmedLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.SConfirmedLCD.setGeometry(QtCore.QRect(613, 110, 80, 30))
            self.SConfirmedLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.SConfirmedLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SConfirmedLCD.setDigitCount(6)
            self.SConfirmedLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.SConfirmedLCD.setProperty("intValue", 0)
            self.SConfirmedLCD.setObjectName("SConfirmedLCD")
            self.SActiveLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.SActiveLCD.setGeometry(QtCore.QRect(613, 155, 80, 30))
            self.SActiveLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.SActiveLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SActiveLCD.setDigitCount(6)
            self.SActiveLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.SActiveLCD.setProperty("intValue", 0)
            self.SActiveLCD.setObjectName("SActiveLCD")
            self.SDeathsLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.SDeathsLCD.setGeometry(QtCore.QRect(613, 245, 80, 30))
            self.SDeathsLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.SDeathsLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.SDeathsLCD.setDigitCount(6)
            self.SDeathsLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.SDeathsLCD.setProperty("intValue", 0)
            self.SDeathsLCD.setObjectName("SDeathsLCD")
            self.DConfirmedLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.DConfirmedLCD.setGeometry(QtCore.QRect(613, 360, 80, 30))
            self.DConfirmedLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.DConfirmedLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.DConfirmedLCD.setDigitCount(6)
            self.DConfirmedLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.DConfirmedLCD.setProperty("intValue", 0)
            self.DConfirmedLCD.setObjectName("DConfirmedLCD")
            self.DRecoveredLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.DRecoveredLCD.setGeometry(QtCore.QRect(613, 405, 80, 30))
            self.DRecoveredLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.DRecoveredLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.DRecoveredLCD.setDigitCount(6)
            self.DRecoveredLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.DRecoveredLCD.setProperty("intValue", 0)
            self.DRecoveredLCD.setObjectName("DRecoveredLCD")
            self.DDeathsLCD = QtWidgets.QLCDNumber(self.centralwidget)
            self.DDeathsLCD.setGeometry(QtCore.QRect(613, 450, 80, 30))
            self.DDeathsLCD.setStyleSheet("QLCDNumber{color:rgb(0, 0, 0);background-color:rgb(255,255, 255);}")
            self.DDeathsLCD.setFrameShadow(QtWidgets.QFrame.Raised)
            self.DDeathsLCD.setDigitCount(6)
            self.DDeathsLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
            self.DDeathsLCD.setProperty("intValue", 0)
            self.DDeathsLCD.setObjectName("DDeathsLCD")
            self.comboBox = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox.setGeometry(QtCore.QRect(680, 540, 69, 22))
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.LangSel = QtWidgets.QLabel(self.centralwidget)
            self.LangSel.setGeometry(QtCore.QRect(530, 540, 121, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setFamily("Arial")
            self.LangSel.setFont(font)
            self.LangSel.setObjectName("LangSel")
            self.ZoneColor.raise_()
            self.Submit.raise_()
            self.label1.raise_()
            self.State.raise_()
            self.Dist.raise_()
            self.Manually.raise_()
            self.Automatically.raise_()
            self.label.raise_()
            self.StateLab.raise_()
            self.state_confirmed.raise_()
            self.state_active.raise_()
            self.state_recovered.raise_()
            self.SRecoveredLCD.raise_()
            self.state_deaths.raise_()
            self.dist_zone.raise_()
            self.dist_deaths.raise_()
            self.dist_confirmed.raise_()
            self.DistLab.raise_()
            self.dist_recovered.raise_()
            self.dist_active_2.raise_()
            self.GovtHosp.raise_()
            self.LocShow.raise_()
            self.FoodShel.raise_()
            self.NightShel.raise_()
            self.Browser.raise_()
            self.line_2.raise_()
            self.line_3.raise_()
            self.line_4.raise_()
            self.line_5.raise_()
            self.Map.raise_()
            self.comboBox.raise_()
            self.LangSel.raise_()
            self.SConfirmedLCD.raise_()
            self.SActiveLCD.raise_()
            self.SDeathsLCD.raise_()
            self.DConfirmedLCD.raise_()
            self.DRecoveredLCD.raise_()
            self.DDeathsLCD.raise_()
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
            self.menubar.setObjectName("menubar")
            self.menuHelp = QtWidgets.QMenu(self.menubar)
            self.menuHelp.setObjectName("menuHelp")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            self.actionExit = QtWidgets.QAction(MainWindow)
            self.actionExit.setObjectName("actionExit")
            self.actionAbout = QtWidgets.QAction(MainWindow)
            self.actionAbout.setObjectName("actionAbout")
            self.actionDeveloper = QtWidgets.QAction(MainWindow)
            self.actionDeveloper.setObjectName("actionDeveloper")
            self.actionCredits = QtWidgets.QAction(MainWindow)
            self.actionCredits.setObjectName("actionCredits")
            self.menuHelp.addAction(self.actionExit)
            self.menuHelp.addAction(self.actionAbout)
            self.menuHelp.addAction(self.actionDeveloper)
            self.menuHelp.addAction(self.actionCredits)
            self.menubar.addAction(self.menuHelp.menuAction())
            self.actionExit.triggered.connect(exit)
            self.actionDeveloper.triggered.connect(lambda:self.Browser.setUrl(QtCore.QUrl("http://arduino3128.github.io")))
            self.actionAbout.triggered.connect(lambda:self.Browser.setUrl(QtCore.QUrl("https://arduino3128.github.io/CoronaDashboard/")))
            self.actionCredits.triggered.connect(lambda:self.Browser.setUrl(QtCore.QUrl("https://pastebin.com/raw/d6fHyq5s")))
            self.Manually.toggled.connect(lambda:self.checktoggle(self.Manually,langopt))
            self.Automatically.toggled.connect(lambda:self.checktoggle(self.Automatically,langopt))
            self.retranslateUi(MainWindow,langopt)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
            if datanum==False:
                self.datdown()
            else:
                pass
        def datdown(self):
            global datanum
            try:
                with open("temp/data.json",'wb') as f:
                    url = "https://api.covidindiatracker.com/state_data.json"
                    response = requests.get(url)
                    f.write(response.content)
                f.close()
                datanum=True
            except:
                os.remove('temp/data.json')
                self.Serverror()
        def checktoggle(self,But,langopt):
            if But.text()==langopt[1] :
                if self.Manually.isChecked()==True:
                    print("Manual")
                    self.Submit.clicked.connect(lambda:self.SubData())
            elif But.text()==langopt[2]:
                if self.Automatically.isChecked()==True:
                    print("Auto")
                    self.StateLab.setText(langopt[9]+langopt[16]+'.....')
                    self.StateLab.adjustSize()
                    self.DistLab.setText(langopt[14]+langopt[16]+'.....')
                    self.DistLab.adjustSize()
                    self.start_Thrd(lang,langColor)
        def retranslateUi(self, MainWindow,langopt):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "CoronaDashboard"))
            self.Submit.setText(_translate("MainWindow", langopt[7]))
            self.label1.setText(_translate("MainWindow", "CoronaDashboard"))
            self.State.setPlaceholderText(_translate("MainWindow", "Enter State"))
            self.Dist.setPlaceholderText(_translate("MainWindow", "Enter District"))
            self.Manually.setText(_translate("MainWindow", langopt[1]))
            self.Automatically.setText(_translate("MainWindow", langopt[2]))
            self.label.setText(_translate("MainWindow", langopt[0]))
            self.StateLab.setText(_translate("MainWindow", langopt[9]))
            self.state_confirmed.setText(_translate("MainWindow", langopt[10]))
            self.state_active.setText(_translate("MainWindow", langopt[11]))
            self.state_recovered.setText(_translate("MainWindow", langopt[12]))
            self.state_deaths.setText(_translate("MainWindow", langopt[13]))
            self.dist_zone.setText(_translate("MainWindow", langopt[15]))
            self.dist_deaths.setText(_translate("MainWindow", langopt[13]))
            self.dist_confirmed.setText(_translate("MainWindow", langopt[10]))
            self.DistLab.setText(_translate("MainWindow", langopt[14]))
            self.dist_recovered.setText(_translate("MainWindow", langopt[12]))
            self.dist_active_2.setText(_translate("MainWindow", "N/A"))
            self.GovtHosp.setText(_translate("MainWindow", langopt[4]))
            self.LocShow.setText(_translate("MainWindow", langopt[3]))
            self.FoodShel.setText(_translate("MainWindow", langopt[5]))
            self.NightShel.setText(_translate("MainWindow", langopt[6]))
            self.Map.setText(_translate("MainWindow", langopt[8]))
            self.Map.adjustSize()
            self.menuHelp.setTitle(_translate("MainWindow", "Help"))
            self.actionExit.setText(_translate("MainWindow", "Exit"))
            self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
            self.actionAbout.setText(_translate("MainWindow", "About"))
            self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
            self.actionCredits.setText(_translate("MainWindow", "Credits"))
            self.comboBox.setItemText(0, _translate("MainWindow", "English"))
            self.comboBox.setItemText(1, _translate("MainWindow", "हिन्दी"))
            self.comboBox.setItemText(2, _translate("MainWindow", "অসমীয়া"))
            self.comboBox.setItemText(3, _translate("MainWindow", "मराठी"))
            self.LangSel.setText(_translate("MainWindow", "Language/ भाषा :"))
            self.comboBox.activated.connect(lambda:self.Lang(self.comboBox.currentIndex()))
        def Lang(self,lng):
            print(lng)
            global lang
            global langopt
            global langColor
            english=['Select Location:','Manually','Automatically','Locate Nearby:','Govt. Hospital','Food Shelters','Night Shelter','Submit','Map:','State:','Confirmed','Active','Recovered','Deaths','District:','Zone Type ',' Detecting',' Not Found']
            englishColors=['RED','ORANGE','YELLOW','GREEN']
            hindi=['स्थान चुनें :','मैन्युअल','स्वचालित','     पास के :','सर.अस्पताल','खाद्य आश्रय','रैन बसेरा','सबमिट','नक्शा :','राज्य :','पुष्टीकृत','सक्रिय','स्वस्थ होनेवाले','मौतें','जिला :','जोन टाइप :',' सर्चिंग',' नहीं मिला']
            hindiColors=['लाल', 'नारंगी', 'पीला', 'हरा']
            assamese=['স্থান নিৰ্বাচন :','হাতে কৰা','স্বয়ংক্ৰিয়','ওচৰতে থকা :','চৰকাৰি চিকিৎসালয়','খাদ্য আশ্ৰয়','ৰাতিৰ আশ্ৰয় স্থল','জমা কৰা','মানচিত্ৰ :','ৰাজ্য :','নিশ্চিত','সক্ৰিয়','আৰোগ্য','মৃত্যু','জিলা :','মঙ্গলৰ প্ৰকাৰ :',' ',' ']
            assameseColors=['ৰঙা','কমলা','হালধীয়া',' সেউজীয়া']
            marathi=['स्थान निवडा :','स्वतः','स्वयंचलितपणे','जवळपास शोधा :','सर.रुग्णालय','अन्न निवारा','रात्री निवारा','जमा','नकाशा :','राज्य :','निश्चीत','सक्रिय','पुनर्प्राप्त','मृतांची संख्या','जिल्हा :','झोन प्रकार :',' शोधत आहे',' सापडले नाही']
            marathiColors=['लाल','नारिंग','पिवळा','हिरवा']
            if lng==0:
                lang='en'
                langopt=english
                langColor=englishColors
                self.setupUi(MainWindow,english,lang)
            elif lng==1:
                lang='hi'
                langColor=hindiColors
                langopt=hindi
                self.setupUi(MainWindow,hindi,lang)
            elif lng==2:
                lang='as'
                langColor=assameseColors
                langopt=assamese
                self.setupUi(MainWindow,assamese,lang)
            elif lng==3:
                lang='mr'
                langColor=marathiColors
                langopt=marathi
                self.setupUi(MainWindow,marathi,lang)
            print(lang)
        def Flocation(self,dist):
            self.Browser.setUrl(QtCore.QUrl("http://google.com/maps/search/Food+Shelter+in+%s"%dist))
        def Nlocation(self,dist):
            self.Browser.setUrl(QtCore.QUrl("http://google.com/maps/search/Night+Shelter+in+%s"%dist))
        def GHlocation(self,dist):
            self.Browser.setUrl(QtCore.QUrl("http://google.com/maps/search/Goverment+Hospitals+in+%s"%dist))
        def SubData(self):
            state=self.State.text()
            dist=self.Dist.text()
            self.FoodShel.clicked.connect(lambda:self.Flocation(dist))
            self.NightShel.clicked.connect(lambda:self.Nlocation(dist))
            self.GovtHosp.clicked.connect(lambda:self.GHlocation(dist))
            self.StateLab.setText("State: %s"%state)
            self.StateLab.adjustSize()
            self.DistLab.setText("Dist: %s"%dist)
            self.DistLab.adjustSize()
            self.Vdata(state,dist,langColor)
        def Serverror(self):
            self.StateLab.setText("Something went wrong!")
            self.StateLab.adjustSize()
            self.StateLab.show()
            self.SRecoveredLCD.display(0)
            self.SDeathsLCD.display(0)   
            self.SConfirmedLCD.display(0)   
            self.SActiveLCD.display(0)
            self.DistLab.setText("Restart CoronaDashboard!")
            self.DistLab.adjustSize()
            self.DistLab.show()
            self.DRecoveredLCD.display(0)
            self.DConfirmedLCD.display(0)
            self.DDeathsLCD.display(0)
            self.dist_active_2.setText("N/A")
            self.ZoneColor.setPixmap(QtGui.QPixmap("Blue.png"))
        def start_Thrd(self,lang,langColor):
            self.thread=Thrd()
            self.thread.basic.connect(lambda:self.process(lang,langColor))
            self.thread.start()
        def process(self,lang,langColor):
            try:
                try:
                    with open("temp/loc.json",'rb') as dat:
                        loca=json.load(dat)
                    dat.close()
                except:
                    self.Serverror()
                if lang!='en':
                    try:
                        with open("temp/loclang.json",'rb') as dat:
                            localang=json.load(dat)
                        dat.close()
                    except:
                        self.Serverror()
                else:
                    localang=loca               
                
            except:
                self.Serverror()
            locaen=loca['results'][-3]['formatted_address']
            locaen=locaen.split(', ')
            state=locaen[1]
            dist=locaen[0]
            localang=localang['results'][-3]['formatted_address']
            localang=localang.split(', ')
            self.FoodShel.clicked.connect(lambda:self.Flocation(dist))
            self.NightShel.clicked.connect(lambda:self.Nlocation(dist))
            self.GovtHosp.clicked.connect(lambda:self.GHlocation(dist))
            if lang!='en':
                statelang=langopt[9]+localang[1]
                distlang=langopt[14]+localang[0]
                print(statelang)
                self.StateLab.setText(statelang)
                self.StateLab.adjustSize()
                self.DistLab.setText(distlang)
                self.DistLab.adjustSize()
            else:
                self.StateLab.setText("State: %s"%state)
                self.StateLab.adjustSize()
                self.DistLab.setText("Dist: %s"%dist)
                self.DistLab.adjustSize()
            self.Vdata(state,dist,langColor)
        def Vdata(self,state,dist,langColor):
            print(langColor)
            print(langopt)
            print(state)
            print(dist)
            sucess=0
            try:
                with open("temp/data.json",'rb') as f:
                    data=json.load(f)
                f.close()
            except:
                self.Serverror()
            for i in range(len(data)):
                sucess=0
                if state == (data[i]['state']) and state!='':
                    print(langopt)
                    self.SActiveLCD.display(data[i]['active'])
                    self.SConfirmedLCD.display(data[i]['confirmed'])
                    self.SRecoveredLCD.display(data[i]['recovered'])
                    self.SDeathsLCD.display(data[i]['deaths'])
                    sucess=1
                    for j in range(len(data[i]['districtData'])):
                        if dist == (data[i]["districtData"][j]['name']) and dist!='' and sucess==1:
                            self.DConfirmedLCD.display(data[i]["districtData"][j]['confirmed'])
                            if data[i]["districtData"][j]['recovered'] ==None:
                                self.DRecoveredLCD.display("D.E")
                            else:
                                self.DRecoveredLCD.display(data[i]["districtData"][j]['recovered'])
                            if data[i]["districtData"][j]['deaths'] ==None:
                                self.DDeathsLCD.display("D.E")
                            else:
                                self.DDeathsLCD.display(data[i]["districtData"][j]['deaths'])
                            zone=data[i]["districtData"][j]['zone']
                            print(zone)
                            if zone=="GREEN":
                                self.dist_active_2.setText(langColor[3])
                                self.ZoneColor.setPixmap(QtGui.QPixmap("Green.png"))
                            elif zone=="ORANGE":
                                self.dist_active_2.setText(langColor[1])
                                self.ZoneColor.setPixmap(QtGui.QPixmap("Orange.png"))
                            elif zone=='RED':
                                self.dist_active_2.setText(langColor[0])
                                self.ZoneColor.setPixmap(QtGui.QPixmap("Red.png"))
                            elif zone=="YELLOW":
                                self.dist_active_2.setText(langColor[2])
                                self.ZoneColor.setPixmap(QtGui.QPixmap("Yellow.png"))
                            else:
                                self.ZoneColor.setPixmap(QtGui.QPixmap("Blue.png"))
                            break
                    else:
                        self.DistLab.setText(langopt[14]+langopt[17])
                        self.DistLab.show()
                        self.DistLab.adjustSize()
                        self.DRecoveredLCD.display(0)
                        self.DConfirmedLCD.display(0)
                        self.DDeathsLCD.display(0)
                        self.dist_active_2.setText("N/A")
                        self.ZoneColor.setPixmap(QtGui.QPixmap("Blue.png"))
                        sucess=0
                    break
            else:
                sucess=0
                self.StateLab.setText(langopt[9]+langopt[17])
                self.StateLab.adjustSize()
                self.SRecoveredLCD.display(0)
                self.SDeathsLCD.display(0)   
                self.SConfirmedLCD.display(0)   
                self.SActiveLCD.display(0)
                self.DistLab.setText(langopt[14]+langopt[17])
                self.DistLab.adjustSize()
                self.DRecoveredLCD.display(0)
                self.DConfirmedLCD.display(0)
                self.DDeathsLCD.display(0)
                self.dist_active_2.setText("N/A")
                self.ZoneColor.setPixmap(QtGui.QPixmap("Blue.png"))

                
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow,langopt,lang)
        MainWindow.show()
        sys.exit(app.exec_())
except Exception as error:
    print(error)
    
