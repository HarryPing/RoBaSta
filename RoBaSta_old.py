from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPalette, QColor
from random import randint
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1277, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_8.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.spinBox.setFont(font)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget, text="Connect", checkable=True, toggled=self.on_toggled_start)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setProperty("value", 10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget, text="Connect", checkable=True, toggled=self.on_toggled)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_8.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_4.setFont(font)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_5.addWidget(self.progressBar_4, 1, 0, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout_5.addWidget(self.lcdNumber_4, 0, 0, 1, 1)
        self.pushHit_4 = QtWidgets.QPushButton(self.widget1)
        self.pushHit_4.setObjectName("pushHit_4")
        self.gridLayout_5.addWidget(self.pushHit_4, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 3, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_3.addWidget(self.lcdNumber_2, 0, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_3.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.pushHit_2 = QtWidgets.QPushButton(self.widget1)
        self.pushHit_2.setObjectName("pushHit_2")
        self.gridLayout_3.addWidget(self.pushHit_2, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.gridLayout.addWidget(self.lcdNumber_1, 0, 0, 1, 1)
        self.progressBar_1 = QtWidgets.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_1.setFont(font)
        self.progressBar_1.setProperty("value", 24)
        self.progressBar_1.setObjectName("progressBar_1")
        self.gridLayout.addWidget(self.progressBar_1, 1, 0, 1, 1)
        self.pushHit_1 = QtWidgets.QPushButton(self.widget1)
        self.pushHit_1.setObjectName("pushHit_1")
        self.gridLayout.addWidget(self.pushHit_1, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout_6.addWidget(self.lcdNumber_5, 0, 0, 1, 1)
        self.progressBar_5 = QtWidgets.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_5.setFont(font)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout_6.addWidget(self.progressBar_5, 1, 0, 1, 1)
        self.pushHit_5 = QtWidgets.QPushButton(self.widget1)
        self.pushHit_5.setObjectName("pushHit_5")
        self.gridLayout_6.addWidget(self.pushHit_5, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 4, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_3.setFont(font)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_4.addWidget(self.progressBar_3, 1, 0, 1, 1)
        self.pushHit_3 = QtWidgets.QPushButton(self.widget1)
        self.pushHit_3.setObjectName("pushHit_3")
        self.gridLayout_4.addWidget(self.pushHit_3, 2, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout_4.addWidget(self.lcdNumber_3, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # main_palette = QPalette()
        # main_palette.setColor(QPalette.Background, QColor(43, 43, 43))
        # main_palette.setColor(QPalette.Base, QColor(43, 43, 43))
        # main_palette.setColor(QPalette.AlternateBase, QColor(43, 43, 43))
        # main_palette.setColor(QPalette.WindowText, QColor(255, 255, 250))
        #
        # line_palette = QPalette()
        # line_palette.setColor(QPalette.Background, QColor(150, 60, 60))
        # line_palette.setColor(QPalette.Base, QColor(150, 60, 60))
        # line_palette.setColor(QPalette.AlternateBase, QColor(150, 60, 60))
        # line_palette.setColor(QPalette.WindowText, QColor(255, 255, 250))
        #
        # MainWindow.setPalette(main_palette)
        # self.lineEdit.setPalette(line_palette)
        # self.lineEdit.setStyleSheet("background: transparent;")
        # self.spinBox_2.setPalette(line_palette)
        # self.spinBox_2.setStyleSheet("background: transparent;")
        #self.lcdNumber.setPalette(lcdpalette)
        #self.lcdNumber.setAutoFillBackground(True)



        self.targets = {}
        for ii in range(0, 6):
            print(ii)
            tmp_dicti = {}
            tmp_dicti.update({"Flag": False})
            tmp_dicti.update({"Timer": QTimer(self.centralwidget)})
            tmp_dicti.update({"Count": 0})
            self.targets.update({ii: tmp_dicti})


        self.targets[0].update({"LCD": self.lcdNumber})
        self.targets[1].update({"LCD": self.lcdNumber_1})
        self.targets[2].update({"LCD": self.lcdNumber_2})
        self.targets[3].update({"LCD": self.lcdNumber_3})
        self.targets[4].update({"LCD": self.lcdNumber_4})
        self.targets[5].update({"LCD": self.lcdNumber_5})

        self.targets[1].update({"Progress": self.progressBar_1})
        self.targets[2].update({"Progress": self.progressBar_2})
        self.targets[3].update({"Progress": self.progressBar_3})
        self.targets[4].update({"Progress": self.progressBar_4})
        self.targets[5].update({"Progress": self.progressBar_5})

        print(self.targets)
        self.targets[0]["Timer"].timeout.connect(self.next_target)

        self.targets[1]["Timer"].timeout.connect(lambda: self.getTime(1))
        self.targets[2]["Timer"].timeout.connect(lambda: self.getTime(2))
        self.targets[3]["Timer"].timeout.connect(lambda: self.getTime(3))
        self.targets[4]["Timer"].timeout.connect(lambda: self.getTime(4))
        self.targets[5]["Timer"].timeout.connect(lambda: self.getTime(5))

        self.last_target = 0
        self.hit_count = 0
        self.dead_time = 500

        self.teiler = 10

        self.tic = time.time()
        #self.pushButton.pressed.connect(self.Start)

        self.pushHit_1.pressed.connect(lambda: self.hit_target(1))
        self.pushHit_2.pressed.connect(lambda: self.hit_target(2))
        self.pushHit_3.pressed.connect(lambda: self.hit_target(3))
        self.pushHit_4.pressed.connect(lambda: self.hit_target(4))
        self.pushHit_5.pressed.connect(lambda: self.hit_target(5))

        self.buffer = []

        self.serial = QtSerialPort.QSerialPort('COM6', baudRate=QtSerialPort.QSerialPort.Baud9600,
                                               readyRead=(lambda: self.receive(self.buffer)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        # self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushHit_1.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_2.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_3.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_5.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_4.setText(_translate("MainWindow", "PushButton"))

    #@QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        if checked:
            self.pushButton_2.setText("Disconnect")
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.button.setChecked(False)
        else:
            self.serial.close()
            self.pushButton_2.setText("Connect")

    def receive(self, buffer: list):
        while self.serial.bytesAvailable():
            tmp = self.serial.read(5)
            buffer.extend(list(tmp))
        if 255 in buffer:
            outcome = []
            while 255 in buffer:
                outcome.append(buffer[0])
                del buffer[0]
            #print(str(outcome))
            #print(outcome)
            self.detect_hit(outcome)


    def send(self, target):
        next_target = int(target - 1)
        print(self.targets[target]["Flag"])
        if self.targets[target]["Flag"]:
            print("send", target, time.time() - self.tic)
            self.serial.writeData(next_target.to_bytes(1, 'big'))

    def detect_hit(self, outcome: list):
        for target in range(1, 6):
            if self.targets[target]["Flag"]:
                if self.targets[target]["Count"] > 100:
                    if (outcome[target - 1] % 10) > 0:
                        print("detected", target, time.time() - self.tic)
                        print(outcome)
                        print(self.targets)
                        self.hit_target(target)


    def getTime(self, target: int):
        def time_text_from_count(count):
            # getting text from count
            count = count * self.teiler
            ms = str(int(count % 1000)).zfill(3)
            seconds = str(int((count // 1000) % 60)).zfill(2)
            minutes = str(int((count // (1000 * 60)) % 60)).zfill(2)

            text = '{}:{}.{}'.format(minutes, seconds, ms)
            return text
        count = 0

        if self.targets[target]["Flag"]:
            self.targets[target]["Count"] += 1
            self.targets[0]["Count"] += 1
            count = self.targets[target]["Count"]
            self.targets[target]["LCD"].display(time_text_from_count(count))
            self.targets[0]["LCD"].display(time_text_from_count(self.targets[0]["Count"]))
            prozent = int((self.dead_time-count*self.teiler) / self.dead_time * 100)
            if prozent < 0:
                self.game_over()
            self.targets[target]["Progress"].setValue(prozent)
            self.targets[target]["Timer"].start(self.teiler)
        else:
            return

    def on_toggled_start(self, checked):
        if checked:
            self.pushButton.setText("Stop")
            #self.reset_targets()
            self.hit_count = 0
            self.dead_time = 500 + int(self.spinBox.value())*250

            self.last_target = 0

            for ii in range(0, 6):
                if ii > 0:
                    self.targets[ii]["Progress"].setValue(0)
                self.targets[ii]["LCD"].display(0)
                self.targets[ii]["Flag"] = False
                self.targets[ii]["Count"] = 0
                self.targets[ii]["Timer"].stop()
                self.targets[ii]["LCD"].display(0)

            self.lineEdit.setText("Lets Go, Dead Time ist:"+ str(self.dead_time))
            self.lcdNumber.setDigitCount(8)
            self.lcdNumber_1.setDigitCount(8)
            self.lcdNumber_2.setDigitCount(8)
            self.lcdNumber_3.setDigitCount(8)
            self.lcdNumber_4.setDigitCount(8)
            self.lcdNumber_5.setDigitCount(8)

            self.next_target()
        else:
            self.pushButton.setText("Start")
            for ii in range(1, 6):
                self.targets[ii]["Timer"].stop()
                self.targets[ii]["Flag"] = False
            if self.hit_count > 0:
                self.lineEdit.setText(
                    "Stop: " + str(self.hit_count) + " Ziele getroffen, durchschnittliche Zeit: " +
                    str(self.targets[0]["Count"] // self.hit_count * self.teiler) + " ms")
            else:
                self.lineEdit.setText("Stop: Du Mischi hast nix getroffen")


    def game_over(self):
        for ii in range(1, 6):
            self.targets[ii]["Timer"].stop()
            self.targets[ii]["Flag"] = False
        if self.hit_count > 0:
            self.lineEdit.setText("Game Over: " + str(self.hit_count) + " Ziele getroffen, durchschnittliche Zeit: " +
                                  str(self.targets[0]["Count"] // self.hit_count * self.teiler) + " ms")
        else:
            self.lineEdit.setText("Game Over: Du Mischi hast nix getroffen")

    def next_target(self):
        self.targets[0]["Timer"].stop()
        target = randint(1, 3)

        if target == self.last_target:
            return self.next_target()

        self.last_target = target

        self.targets[target]["Flag"] = True
        self.targets[target]["Count"] = 0
        self.targets[target]["Timer"].start(10)
        self.send(target)

    def hit_target(self, target: int):
        if self.targets[target]["Flag"]:
            self.hit_count += 1
            self.targets[target]["Flag"] = False
            self.targets[target]["Timer"].stop()
            self.targets[target]["Progress"].setValue(0)

            if self.hit_count == self.spinBox_2.value():
                self.game_over()
            else:
                self.lineEdit.setText(str(self.hit_count) + " Ziele getroffen, durchschnittliche Zeit: " +
                                      str(self.targets[0]["Count"] // self.hit_count *self.teiler) + " ms")
                self.targets[0]["Timer"].start(randint(0, 1500))


    def Pause(self):
        # making flag to False
        self.flag = False


    def Re_set(self):
        # making flag to false
        self.flag = False

        # reseeting the count
        self.count = 0

        # setting text to label
        self.label.setText(str(self.count))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
