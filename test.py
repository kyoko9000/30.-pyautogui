import sys
# pip install pyqt5
import time

from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
import threading
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_start.clicked.connect(self.run_a)
    def run_a(self):
        print("runing program")
        self.uic.label.setText("program running")
        self.uic.label.repaint()
        for i in range(5):
            print(i)
            time.sleep(1)
        self.uic.label.setText("run complete")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
