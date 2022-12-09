#!/usr/bin/env python
########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        self.webEngineView = QWebEngineView()
        ########################################################################

        ## PAGES
        ########################################################################
        self.ui.btn_page_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_2))
        self.ui.btn_learn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.learn_page))
        self.ui.btn_test.clicked.connect(self.OpenTest)

        # PAGE LEARN
        ########################################################################
        self.ui.one_learn.clicked.connect(self.LearnOne)

        self.ui.two_learn.clicked.connect(self.LearnTwo)

        self.ui.three_learn.clicked.connect(self.LearnThree)

        self.ui.four_learn.clicked.connect(self.LearnFour)

        self.ui.five_learn.clicked.connect(self.LearnFive)

        self.ui.six_learn.clicked.connect(self.LearnSix)

        self.ui.seven_learn.clicked.connect(self.LearnSeven)

        self.ui.eight_learn.clicked.connect(self.LearnEight)

        self.ui.nine_learn.clicked.connect(self.LearnNine)

        self.ui.ten_learn.clicked.connect(self.LearnTen)

        self.ui.eleven_learn.clicked.connect(self.LearnEleven)

        self.ui.twelve_learn.clicked.connect(self.LearnTwelve)

        self.ui.theerteen_learn.clicked.connect(self.LearnTherteen)

        self.ui.fourteen_learn.clicked.connect(self.LearnFourteen)

        self.show()

        ## SHOW ==> MAIN WINDOW
        ########################################################################     

        #OPEN PDF 
        ########################################################################
    def LearnOne(self):
        self.web1 = QWebEngineView()
        self.web1.resize(720,400)
        self.web1.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web1.load(QUrl("file:///LAB1.pdf"))
        self.web1.show()

    def LearnTwo(self):
        self.web2 = QWebEngineView()
        self.web2.resize(720,400)
        self.web2.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web2.load(QUrl("file:///LAB/2.pdf"))
        self.web2.show()

    def LearnThree(self):
        self.web3 = QWebEngineView()
        self.web3.resize(720,400)
        self.web3.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web3.load(QUrl("file:///LAB/3.pdf"))
        self.web3.show()

    def LearnFour(self):
        self.web4 = QWebEngineView()
        self.web4.resize(720,400)
        self.web4.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web4.load(QUrl("file:///LAB/4.pdf"))
        self.web4.show()

    def LearnFive(self):
        self.web5 = QWebEngineView()
        self.web5.resize(720,400)
        self.web5.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web5.load(QUrl("file:///LAB/5.pdf"))
        self.web5.show()
    
    def LearnSix(self):
        self.web6 = QWebEngineView()
        self.web6.resize(720,400)
        self.web6.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web6.load(QUrl("file:///LAB/6.pdf"))
        self.web6.show()

    def LearnSeven(self):
        self.web7 = QWebEngineView()
        self.web7.resize(720,400)
        self.web7.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web7.load(QUrl("file:///LAB/7.pdf"))
        self.web7.show()

    def LearnEight(self):
        self.web8 = QWebEngineView()
        self.web8.resize(720,400)
        self.web8.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web8.load(QUrl("file:///LAB/8.pdf"))
        self.web8.show()

    def LearnNine(self):
        self.web9 = QWebEngineView()
        self.web9.resize(720,400)
        self.web9.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web9.load(QUrl("file:///LAB/9.pdf"))
        self.web9.show()

    def LearnTen(self):
        self.web10 = QWebEngineView()
        self.web10.resize(720,400)
        self.web10.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web10.load(QUrl("file:///LAB/10.pdf"))
        self.web10.show()

    def LearnEleven(self):
        self.web11 = QWebEngineView()
        self.web11.resize(720,400)
        self.web11.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web11.load(QUrl("file:///LAB/11.pdf"))
        self.web11.show()

    def LearnTwelve(self):
        self.web12 = QWebEngineView()
        self.web12.resize(720,400)
        self.web12.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web12.load(QUrl("file:///LAB/12.pdf"))
        self.web12.show()

    def LearnTherteen(self):
        self.web13 = QWebEngineView()
        self.web13.resize(720,400)
        self.web13.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web13.load(QUrl("file:///LAB/13.pdf"))
        self.web13.show()

    def LearnFourteen(self):
        self.web14 = QWebEngineView()
        self.web14.resize(720,400)
        self.web14.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web14.load(QUrl("file:///LAB/14.pdf"))
        self.web14.show()
        ########################################################################

        ##OPEN PROGRAMM TEST
        ########################################################################
    def OpenTest(self):
        self.close()
        os.system('python test.py')
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  