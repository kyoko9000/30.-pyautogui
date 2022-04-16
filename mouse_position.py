import pyautogui
import keyboard
import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_start.clicked.connect(self.print_position)
        keyboard.add_hotkey('a', self.print_position)

    def print_position(self):
        y = pyautogui.position()
        self.uic.label.setText(str(y))
        print(y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
