from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
import time
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QPalette, QColor, QStandardItemModel, QStandardItem
from PyQt5.QtMultimedia import QSound
from random import randint
import time
import os
import json


def load_config():
    with open('./config.json') as f:
        data = json.loads(f.read())
    f.close()
    return data


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lcdNumber = QtWidgets.QLCDNumber(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(200)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.spinBox.setFont(font)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 0, 1, 1)
        self.comboBox_playername = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.comboBox_playername.setFont(font)
        self.comboBox_playername.setObjectName("comboBox_playername")
        self.comboBox_playername.addItem("Test")
        self.comboBox_playername.addItem("Andi")
        self.comboBox_playername.addItem("Jens")
        self.comboBox_playername.addItem("Fabi")
        self.comboBox_playername.addItem("Matze")
        self.comboBox_playername.addItem("Basti")
        self.comboBox_playername.addItem("Anke")
        self.gridLayout_2.addWidget(self.comboBox_playername, 0, 2, 1, 1)
        self.comboBox_GameMode = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.comboBox_GameMode.setFont(font)
        self.comboBox_GameMode.setObjectName("comboBox_GameMode")
        self.comboBox_GameMode.addItem("")
        self.comboBox_GameMode.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_GameMode, 0, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, text="Connect", checkable=True,
                                                  toggled=self.on_toggled)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, text="Start", checkable=True,
                                                toggled=self.on_toggled_start)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setProperty("value", 10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.gridLayout.addWidget(self.lcdNumber_1, 0, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 0, 1, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 0, 2, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 0, 3, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 0, 4, 1, 1)
        self.progressBar_1 = QtWidgets.QProgressBar(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_1.setFont(font)
        self.progressBar_1.setProperty("value", 24)
        self.progressBar_1.setObjectName("progressBar_1")
        self.gridLayout.addWidget(self.progressBar_1, 1, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout.addWidget(self.progressBar_2, 1, 1, 1, 1)
        self.progressBar_3 = QtWidgets.QProgressBar(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_3.setFont(font)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout.addWidget(self.progressBar_3, 1, 2, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_4.setFont(font)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout.addWidget(self.progressBar_4, 1, 3, 1, 1)
        self.progressBar_5 = QtWidgets.QProgressBar(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.progressBar_5.setFont(font)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout.addWidget(self.progressBar_5, 1, 4, 1, 1)
        self.pushHit_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushHit_1.setObjectName("pushHit_1")
        self.gridLayout.addWidget(self.pushHit_1, 2, 0, 1, 1)
        self.pushHit_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushHit_2.setObjectName("pushHit_2")
        self.gridLayout.addWidget(self.pushHit_2, 2, 1, 1, 1)
        self.pushHit_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushHit_3.setObjectName("pushHit_3")
        self.gridLayout.addWidget(self.pushHit_3, 2, 2, 1, 1)
        self.pushHit_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushHit_4.setObjectName("pushHit_4")
        self.gridLayout.addWidget(self.pushHit_4, 2, 3, 1, 1)
        self.pushHit_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushHit_5.setObjectName("pushHit_5")
        self.gridLayout.addWidget(self.pushHit_5, 2, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 2)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.dead_time = 5000000

        self.teiler = 10

        self.tic = time.time()
        self.config = load_config()

        self.hit_sound = QSound("./Sounds/Ripper/fire.wav")
        self.start_sound = QSound("./Sounds/Sniper Rifle/fire.wav")

        self.bestenliste = {}

        with open('./bestenliste.json') as f:
            data = json.loads(f.read())
        f.close()
        self.bestenliste = data

        self.bestenlistemodel = QStandardItemModel()

        self.spinBox.setValue(50)
        self.spinBox_2.setValue(5)

        self.pushHit_1.pressed.connect(lambda: self.hit_target(1))
        self.pushHit_2.pressed.connect(lambda: self.hit_target(2))
        self.pushHit_3.pressed.connect(lambda: self.hit_target(3))
        self.pushHit_4.pressed.connect(lambda: self.hit_target(4))
        self.pushHit_5.pressed.connect(lambda: self.hit_target(5))

        self.buffer = []

        self.serial = QtSerialPort.QSerialPort(self.config["com"], baudRate=QtSerialPort.QSerialPort.Baud9600,
                                               readyRead=(lambda: self.receive(self.buffer)))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        # self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        # self.comboBox_playername.setItemText(0, _translate("MainWindow", "Andi"))
        # self.comboBox_playername.setItemText(1, _translate("MainWindow", "Jens"))
        # self.comboBox_playername.setItemText(2, _translate("MainWindow", "Fabi"))
        # self.comboBox_playername.setItemText(3, _translate("MainWindow", "Basti"))
        # self.comboBox_playername.setItemText(4, _translate("MainWindow", "Matze"))
        # self.comboBox_playername.setItemText(5, _translate("MainWindow", "Benne"))
        # self.comboBox_playername.setItemText(6, _translate("MainWindow", "Anke"))
        # self.comboBox_playername.setItemText(7, _translate("MainWindow", "Gast"))
        self.pushHit_1.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_2.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_3.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_5.setText(_translate("MainWindow", "PushButton"))
        self.pushHit_4.setText(_translate("MainWindow", "PushButton"))
        self.comboBox_GameMode.setItemText(0, _translate("MainWindow", "Abraeumen"))
        self.comboBox_GameMode.setItemText(1, _translate("MainWindow", "Zufall Einzelnd"))

        # Set the style sheet
        military_style = """
        QWidget {
            background-color: #333333;
            color: #ffffff;
            font-family: Arial, sans-serif;
            font-size: 14px;
        }

        QLabel {
            color: #ffffff;
            font-size: 16px;
        }

        QGroupBox {
            border: 1px solid #aaaaaa;
            margin-top: 10px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 5px;
            color: #ffffff;
        }

        QPushButton {
            background-color: #555555;
            color: #ffffff;
            border: 1px solid #555555;
            padding: 5px;
            font-weight: bold;
            font-size: 14px;
        }

        QPushButton:hover {
            background-color: #666666;
            border: 1px solid #666666;
        }

        QLineEdit {
            background-color: #666666;
            color: #ffffff;
            border: 1px solid #aaaaaa;
            padding: 5px;
        }

        QTextEdit {
            background-color: #666666;
            color: #ffffff;
            border: 1px solid #aaaaaa;
            padding: 5px;
            font-family: Courier, monospace;
        }

        QScrollBar:vertical {
            border: 1px solid #aaaaaa;
            background: #555555;
            width: 14px;
            margin: 14px 0 14px 0;
        }

        QScrollBar::handle:vertical {
            background-color: #aaaaaa;
            min-height: 20px;
        }

        QScrollBar::add-line:vertical {
            border: none;
            background: none;
        }

        QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        """
        style = """
                    QWidget {
                        background-color: #232323;
                        color: #fff;
                        font-size: 16px;
                        font-family: 'Segoe UI', sans-serif;
                    }
                    QTableView  {
                        background-color: #232323;
                        color: #fff;
                        font-size: 32px;
                        font-family: 'Segoe UI', sans-serif;
                    }
                    QMenuBar {
                        background-color: #2c2c2c;
                        color: #fff;
                    }
                    QMenuBar::item {
                        background-color: transparent;
                        padding: 4px 10px;
                    }
                    QMenuBar::item:selected {
                        background-color: #666666;
                    }
                    QMenu {
                        background-color: #2c2c2c;
                        color: #fff;
                    }
                    QMenu::item:selected {
                        background-color: #666666;
                    }
                    QPushButton {
                        background-color: #0057a8;
                        color: #fff;
                        padding: 5px 15px;
                        border: none;
                        border-radius: 4px;
                    }
                    QPushButton:hover {
                        background-color: #0078d7;
                    }
                    QLineEdit {
                        background-color: #4d4d4d;
                        color: #fff;
                        border: none;
                        padding: 5px;
                        border-radius: 4px;
                    }
                    QComboBox {
                        background-color: #4d4d4d;
                        color: #fff;
                        border: none;
                        padding: 5px;
                        border-radius: 4px;
                    }
                    QComboBox:hover {
                        background-color: #6b6b6b;
                    }
                    QScrollBar {
                        background-color: #2c2c2c;
                        width: 8px;
                    }
                    QScrollBar::handle {
                        background-color: #666666;
                    }
                    QScrollBar::handle:hover {
                        background-color: #888888;
                    }
                """
        MainWindow.setStyleSheet(style)

    #@QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        if checked:
            self.pushButton_2.setText("Disconnect")
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    # self.button.setChecked(False)
                    print(" # self.button.setChecked(False)")

        else:
            self.serial.close()
            self.pushButton_2.setText("Connect")

    def receive(self, buffer: list):
        while self.serial.bytesAvailable():
            tmp = self.serial.read(5)
            # print(tmp)
            buffer.extend(list(tmp))
        if 255 in buffer:
            outcome = []
            while 255 in buffer:
                outcome.append(buffer[0])
                del buffer[0]
            # print(str(outcome))
            # print(outcome)
            self.detect_hit(outcome)

    def alle_aufrichten(self):
        for target in range(0, 5):
            self.serial.writeData(target.to_bytes(1, 'big'))

    def send(self, target):
        next_target = int(target - 1)
        print(self.targets[target]["Flag"])
        if self.targets[target]["Flag"]:
            print("send", target, time.time() - self.tic)
            self.serial.writeData(next_target.to_bytes(1, 'big'))

    def detect_hit(self, outcome: list):
        for target in range(1, 6):
            if self.targets[target]["Flag"]:
                if self.targets[target]["Count"] > 20:
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

    def reset_all_target_with_true(self):
        for ii in range(0, 6):
            if ii > 0:
                self.targets[ii]["Progress"].setValue(0)
                self.targets[ii]["LCD"].display(0)
            self.targets[ii]["Flag"] = True
            self.targets[ii]["Count"] = 21
            self.targets[ii]["Timer"].stop()

    def on_toggled_start(self, checked):
        # Auf Start drücken
        if checked:
            self.start_sound.play()
            self.pushButton.setText("Stop")
            #self.reset_targets()
            self.hit_count = 0
            self.last_target = 0

            for ii in range(0, 6):
                if ii > 0:
                    self.targets[ii]["Progress"].setValue(0)
                self.targets[ii]["LCD"].display(0)
                self.targets[ii]["Flag"] = False
                self.targets[ii]["Count"] = 0
                self.targets[ii]["Timer"].stop()


            if self.comboBox_GameMode.currentText() == "Abraeumen":
                self.alle_aufrichten()
                QtCore.QTimer.singleShot(5000, self.reset_all_target_with_true)

            if self.comboBox_GameMode.currentText() == "Zufall Einzelnd":
                self.last_target = 1

                self.targets[1]["Flag"] = True
                self.targets[1]["Count"] = 150
                # self.targets[1]["Timer"].start(self.teiler)
                self.send(1)
           # Stop drücken
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
        def time_text_from_count(count):
            # getting text from count
            count = count * self.teiler
            ms = str(int(count % 1000)).zfill(3)
            seconds = str(int((count // 1000) % 60)).zfill(2)
            minutes = str(int((count // (1000 * 60)) % 60)).zfill(2)

            text = '{}:{}.{}'.format(minutes, seconds, ms)
            return text

        max_count = 0
        for ii in range(1, 6):
            if max_count < self.targets[ii]["Count"]:
                max_count = self.targets[ii]["Count"]
            self.targets[ii]["Timer"].stop()
            self.targets[ii]["Flag"] = False
        if self.comboBox_GameMode.currentText() == "Abraeumen":
            self.targets[0]["LCD"].display(time_text_from_count(max_count))
            self.targets[0]["Count"] = max_count
        if self.hit_count > 0:
            self.lineEdit.setText("Game Over: " + str(self.hit_count) + " Ziele getroffen, durchschnittliche Zeit: " +
                                  str(self.targets[0]["Count"] // self.hit_count * self.teiler) + " ms")
        else:
            self.lineEdit.setText("Game Over: Du Muschi hast nix getroffen")

        if self.comboBox_GameMode.currentText() == "Abraeumen":
            self.targets[0]["LCD"].display(time_text_from_count(max_count))
            self.targets[0]["Count"] = max_count

            self.hit_count = 0
            self.last_target = 0


            # Bestenliste Darstellen
            current_player = self.comboBox_playername.currentText()
            if current_player not in self.bestenliste.keys():
                self.bestenliste.update({current_player: max_count})
            else:
                if self.bestenliste[current_player] > max_count:
                    self.bestenliste.update({current_player: max_count})

            tmp_lst = sorted(self.bestenliste.items(), key=lambda x: x[1])

            self.bestenlistemodel.clear()
            self.bestenlistemodel.setHorizontalHeaderLabels(["Key", "Value"])
            for tmp_lst_item in tmp_lst:
                key_item = QStandardItem(str(tmp_lst_item[0]))
                value_item = QStandardItem(str(tmp_lst_item[1]))
                self.bestenlistemodel.appendRow([key_item, value_item])
            self.tableView.setModel(self.bestenlistemodel)

            with open("bestenliste.json", "w") as outfile:
                json.dump(self.bestenliste, outfile)


        if self.comboBox_GameMode.currentText() == "Abraeumen":
            self.alle_aufrichten()
            QtCore.QTimer.singleShot(5000, self.reset_all_target_with_true)

    def next_target(self):
        if self.comboBox_GameMode.currentText() == "Zufall Einzelnd":
            self.targets[0]["Timer"].stop()
            target = randint(1, 5)

            if target == self.last_target:
                return self.next_target()

            self.last_target = target

            self.targets[target]["Flag"] = True
            self.targets[target]["Count"] = 0
            self.targets[target]["Timer"].start(self.teiler)
            self.send(target)

        elif self.comboBox_GameMode.currentText() == "Abraeumen":
            for ii in range(1, 6):
                self.targets[ii]["Flag"] = True
                self.targets[ii]["Count"] = 0
                self.targets[ii]["Timer"].start(self.teiler)

    def start_after_first_hit(self, target):
        print("Start after first hit")
        if self.comboBox_GameMode.currentText() == "Abraeumen":
            for ii in range(1, 6):
                if not ii == target:
                    self.targets[ii]["Flag"] = True
                    self.targets[ii]["Count"] = 0
                    self.targets[ii]["Timer"].start(self.teiler)

        self.lineEdit.setText("Lets Go, Dead Time ist:" + str(self.dead_time))

    def hit_target(self, target: int):
        if self.hit_count == 0:
            self.start_after_first_hit(target)


        if self.targets[target]["Flag"]:
            self.hit_count += 1
            self.targets[target]["Flag"] = False
            self.targets[target]["Timer"].stop()
            self.targets[target]["Progress"].setValue(0)


            # self.hit_sound.play()

            if self.hit_count == self.spinBox_2.value():
                self.game_over()
            else:
                self.lineEdit.setText(str(self.hit_count) + " Ziele getroffen, durchschnittliche Zeit: " +
                                      str(self.targets[0]["Count"] // self.hit_count *self.teiler) + " ms")
                if self.comboBox_GameMode.currentText() == "Zufall Einzelnd":
                    self.targets[0]["Timer"].start(randint(0, 1500))
                elif self.comboBox_GameMode.currentText() == "Abraeumen":
                    print("hit target abraumen")

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
