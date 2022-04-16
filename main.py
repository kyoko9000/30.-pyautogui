import sys
# pip install pyqt6
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import pydirectinput
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.Button_start.clicked.connect(self.run_game)

        self.thread = {}

    def closeEvent(self, event):
        print("pressed X")
        self.thread[1].stop()
        self.thread[2].stop()

    def run_game(self):
        self.thread[1] = position_ship(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.prepare_ship)

    def prepare_ship(self, Red_location, yellow_location):
        self.thread[2] = run_ship(Red_location, yellow_location, index1=2)
        self.thread[2].start()

class run_ship(QThread):
    def __init__(self, Red_location, yellow_location, index1=0):
        super(run_ship, self).__init__()
        self.Red_location = Red_location
        self.yellow_location = yellow_location
        self.index1 = index1
        print("start threading: ", self.index1)

    def run(self):
        print("Red location: ", self.Red_location)
        print("yellow location: ", self.yellow_location)
        if self.yellow_location[1] > self.Red_location[1] and (self.yellow_location[1] - self.Red_location[1]) > 20:
            print("press: w")
            pydirectinput.keyDown('w')
            time.sleep(0.2)
            pydirectinput.keyUp('w')
        elif self.yellow_location[1] < self.Red_location[1] and (self.Red_location[1] - self.yellow_location[1]) > 20:
            print("press: s")
            pydirectinput.keyDown('s')
            time.sleep(0.2)
            pydirectinput.keyUp('s')
        elif (self.yellow_location[1] - self.Red_location[1]) < 20:
            print("fire")
            pydirectinput.press('space', presses=2, interval=0.1)

    def stop(self):
        print("stop threading: ", self.index1)
        self.terminate()

class position_ship(QThread):
    signal = pyqtSignal(list, list)
    def __init__(self, index=0):
        super(position_ship, self).__init__()
        self.a = index
        print("start threading: ", self.a)
    def run(self):
        while True:
            try:
                print("run")
                time.sleep(0.5)
                image_1 = 'red_ship.png'
                image_2 = 'yellow_ship.png'
                Red_location = pyautogui.locateOnScreen(image_1, grayscale=True, confidence=0.5)  #,grayscale=True
                yellow_location = pyautogui.locateOnScreen(image_2, grayscale=True, confidence=0.5)
                print("red ship position", Red_location)
                print("yellow ship position", yellow_location)
                self.signal.emit(Red_location, yellow_location)
            except:
                print("can't find the target")

    def stop(self):
        print("stop threading: ", self.a)
        self.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())