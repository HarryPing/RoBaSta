import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QColor, QPalette

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setzen des dunklen Farbthemas
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

        # Erstellen der drei digitalen Anzeigen
        self.hour_lcd = QLCDNumber(self)
        self.hour_lcd.setDigitCount(2)
        self.hour_lcd.move(30, 20)

        self.minute_lcd = QLCDNumber(self)
        self.minute_lcd.setDigitCount(2)
        self.minute_lcd.move(80, 20)

        self.second_lcd = QLCDNumber(self)
        self.second_lcd.setDigitCount(2)
        self.second_lcd.move(130, 20)

        # Erstellen eines Timers, um die Anzeigen jede Sekunde zu aktualisieren
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)

        # Setzen der Größe und des Titels des Fensters
        self.setGeometry(300, 300, 200, 100)
        self.setWindowTitle('Digital Clock')
        self.show()

    def updateTime(self):
        # Abrufen der aktuellen Zeit
        current_time = QTime.currentTime()

        # Aktualisieren der digitalen Anzeigen
        self.hour_lcd.display(current_time.hour())
        self.minute_lcd.display(current_time.minute())
        self.second_lcd.display(current_time.second())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    sys.exit(app.exec_())
