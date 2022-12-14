# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 743)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.btn_page_home = QPushButton(self.frame_3)
        self.btn_page_home.setObjectName(u"btn_page_home")
        self.btn_page_home.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_page_home.sizePolicy().hasHeightForWidth())
        self.btn_page_home.setSizePolicy(sizePolicy1)
        self.btn_page_home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(185, 0, 3);\n"
"	border-radius: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_home.setIcon(icon)
        self.btn_page_home.setCheckable(False)
        self.btn_page_home.setAutoRepeatDelay(300)

        self.horizontalLayout_5.addWidget(self.btn_page_home)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	font-size: 20px;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	font-size: 40px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy3)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.main_body_contents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.learn_page = QWidget()
        self.learn_page.setObjectName(u"learn_page")
        self.learn_page.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	font-size: 40px;\n"
"}")
        self.gridLayout = QGridLayout(self.learn_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.learn_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1098, 687))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.one_learn = QPushButton(self.scrollAreaWidgetContents)
        self.one_learn.setObjectName(u"one_learn")
        self.one_learn.setLayoutDirection(Qt.RightToLeft)
        self.one_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.one_learn)

        self.two_learn = QPushButton(self.scrollAreaWidgetContents)
        self.two_learn.setObjectName(u"two_learn")
        self.two_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.two_learn)

        self.three_learn = QPushButton(self.scrollAreaWidgetContents)
        self.three_learn.setObjectName(u"three_learn")
        self.three_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.three_learn)

        self.four_learn = QPushButton(self.scrollAreaWidgetContents)
        self.four_learn.setObjectName(u"four_learn")
        self.four_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.four_learn)

        self.five_learn = QPushButton(self.scrollAreaWidgetContents)
        self.five_learn.setObjectName(u"five_learn")
        self.five_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.five_learn)

        self.six_learn = QPushButton(self.scrollAreaWidgetContents)
        self.six_learn.setObjectName(u"six_learn")
        self.six_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.six_learn)

        self.seven_learn = QPushButton(self.scrollAreaWidgetContents)
        self.seven_learn.setObjectName(u"seven_learn")
        self.seven_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.seven_learn)

        self.eight_learn = QPushButton(self.scrollAreaWidgetContents)
        self.eight_learn.setObjectName(u"eight_learn")
        self.eight_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.eight_learn)

        self.nine_learn = QPushButton(self.scrollAreaWidgetContents)
        self.nine_learn.setObjectName(u"nine_learn")
        self.nine_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.nine_learn)

        self.ten_learn = QPushButton(self.scrollAreaWidgetContents)
        self.ten_learn.setObjectName(u"ten_learn")
        self.ten_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.ten_learn)

        self.eleven_learn = QPushButton(self.scrollAreaWidgetContents)
        self.eleven_learn.setObjectName(u"eleven_learn")
        self.eleven_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.eleven_learn)

        self.twelve_learn = QPushButton(self.scrollAreaWidgetContents)
        self.twelve_learn.setObjectName(u"twelve_learn")
        self.twelve_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.twelve_learn)

        self.theerteen_learn = QPushButton(self.scrollAreaWidgetContents)
        self.theerteen_learn.setObjectName(u"theerteen_learn")
        self.theerteen_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.theerteen_learn)

        self.fourteen_learn = QPushButton(self.scrollAreaWidgetContents)
        self.fourteen_learn.setObjectName(u"fourteen_learn")
        self.fourteen_learn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.fourteen_learn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.learn_page)
        self.home_2 = QWidget()
        self.home_2.setObjectName(u"home_2")
        self.home_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background:rgb(85, 170, 255);\n"
"	height: 35px;\n"
" 	border-radius:10px;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	font-size: 40px;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.home_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget = QWidget(self.home_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_learn = QPushButton(self.widget_2)
        self.btn_learn.setObjectName(u"btn_learn")

        self.horizontalLayout_7.addWidget(self.btn_learn)

        self.btn_test = QPushButton(self.widget_2)
        self.btn_test.setObjectName(u"btn_test")

        self.horizontalLayout_7.addWidget(self.btn_test)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.home_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.main_body_contents)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_page_home, self.minimize_window_button)
        QWidget.setTabOrder(self.minimize_window_button, self.restore_window_button)
        QWidget.setTabOrder(self.restore_window_button, self.close_window_button)
        QWidget.setTabOrder(self.close_window_button, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.one_learn)
        QWidget.setTabOrder(self.one_learn, self.two_learn)
        QWidget.setTabOrder(self.two_learn, self.three_learn)
        QWidget.setTabOrder(self.three_learn, self.four_learn)
        QWidget.setTabOrder(self.four_learn, self.five_learn)
        QWidget.setTabOrder(self.five_learn, self.six_learn)
        QWidget.setTabOrder(self.six_learn, self.seven_learn)
        QWidget.setTabOrder(self.seven_learn, self.eight_learn)
        QWidget.setTabOrder(self.eight_learn, self.nine_learn)
        QWidget.setTabOrder(self.nine_learn, self.ten_learn)
        QWidget.setTabOrder(self.ten_learn, self.eleven_learn)
        QWidget.setTabOrder(self.eleven_learn, self.twelve_learn)
        QWidget.setTabOrder(self.twelve_learn, self.theerteen_learn)
        QWidget.setTabOrder(self.theerteen_learn, self.fourteen_learn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_page_home.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0443\u043c", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.one_learn.setText(QCoreApplication.translate("MainWindow", u"1. \u041f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0433\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u043a\u0438. \u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u044b \u0433\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u043a\u0438. \u0413\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u044b. \u0412\u0438\u0434\u044b \u0438 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u0433\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0435\u0439.", None))
        self.two_learn.setText(QCoreApplication.translate("MainWindow", u"2.\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u043e\u0431\u044a\u0435\u043c\u043d\u043e\u0433\u043e \u043d\u0435\u0440\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u0435\u043c\u043e\u0433\u043e \u043d\u0430\u0441\u043e\u0441\u0430.", None))
        self.three_learn.setText(QCoreApplication.translate("MainWindow", u"3. \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0433\u0438\u0434\u0440\u043e\u0446\u0438\u043b\u0438\u043d\u0434\u0440\u0430 \u0441 \u043e\u0434\u043d\u043e\u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u043c \u0448\u0442\u043e\u043a\u043e\u043c. \u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435.", None))
        self.four_learn.setText(QCoreApplication.translate("MainWindow", u"4. \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0433\u0438\u0434\u0440\u043e\u0446\u0438\u043b\u0438\u043d\u0434\u0440\u0430 \u0441 \u043e\u0434\u043d\u043e\u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u043c \u0448\u0442\u043e\u043a\u043e\u043c. \u041e\u0431\u044a\u0435\u043c\u043d\u044b\u0439 \u0440\u0430\u0441\u0445\u043e\u0434.", None))
        self.five_learn.setText(QCoreApplication.translate("MainWindow", u"5. \u041e\u0431\u044a\u0435\u043c\u043d\u044b\u0439 \u0433\u0438\u0434\u0440\u043e\u043c\u043e\u0442\u043e\u0440", None))
        self.six_learn.setText(QCoreApplication.translate("MainWindow", u"6. \u0413\u0438\u0434\u0440\u043e\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0438", None))
        self.seven_learn.setText(QCoreApplication.translate("MainWindow", u"7. \u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0433\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0434\u0440\u043e\u0441\u0441\u0435\u043b\u044c.", None))
        self.eight_learn.setText(QCoreApplication.translate("MainWindow", u"8. \u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0433\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0434\u0440\u043e\u0441\u0441\u0435\u043b\u044c \u0441 \u043e\u0431\u0440\u0430\u0442\u043d\u044b\u043c \u043a\u043b\u0430\u043f\u0430\u043d\u043e\u043c.", None))
        self.nine_learn.setText(QCoreApplication.translate("MainWindow", u"9. \u0420\u0435\u0433\u0443\u043b\u044f\u0442\u043e\u0440 \u0440\u0430\u0441\u0445\u043e\u0434\u0430.", None))
        self.ten_learn.setText(QCoreApplication.translate("MainWindow", u"10. \u041f\u0440\u0435\u0434\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u043b\u0430\u043f\u0430\u043d \u043f\u0440\u044f\u043c\u043e\u0433\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f.", None))
        self.eleven_learn.setText(QCoreApplication.translate("MainWindow", u"11. \u0420\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432 \u0433\u0438\u0434\u0440\u043e\u0441\u0438\u0441\u0442\u0435\u043c\u0435 \u043f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u043f\u0440\u0435\u0434\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043a\u043b\u0430\u043f\u0430\u043d\u043e\u0432.", None))
        self.twelve_learn.setText(QCoreApplication.translate("MainWindow", u"12. \u0420\u0435\u0434\u0443\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u043b\u0430\u043f\u0430\u043d.", None))
        self.theerteen_learn.setText(QCoreApplication.translate("MainWindow", u"13. \u041a\u043e\u043c\u043f\u043e\u043d\u043e\u0432\u043a\u0430 \u0438 \u0440\u0430\u0431\u043e\u0442\u0430 \u0434\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0445\u0435\u043c\u044b.", None))
        self.fourteen_learn.setText(QCoreApplication.translate("MainWindow", u"14. \u0423\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u043c\u044b\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u044b\u0435 \u043a\u043b\u0430\u043f\u0430\u043d\u0430.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0438\u0439 \u0432\u0430\u0441 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.btn_learn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

