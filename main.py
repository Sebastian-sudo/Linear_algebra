import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from sympy import *
import matplotlib.pyplot as plt
import seaborn as sns

class Symbolic:

   def __init__(self):
      pass

class Graph:

   def __init__(self):
      pass

class gui:

   def __init__(self):
      self.width = 640
      self.height = 480
      self.equation = ""

      self.app = QApplication(sys.argv)
      self.win = QWidget()
      self.win.setGeometry(300, 200, self.width, self.height)
      self.win.setWindowTitle("Symbolic calculator")

      self.mainLabel()

   def mainLabel(self):
      self.mainLabel = QLineEdit(self.win)
      self.mainLabel.move(0, 5)
      self.mainLabel.resize(self.width, 50)

      self.calculateButton = QPushButton(self.win)
      self.calculateButton.move(self.width / 2 - 75, 65)
      self.calculateButton.resize(150, 50)
      self.calculateButton.setText("Calculate")
      self.calculateButton.clicked.connect(self.Button)

      self.chooseButton = QComboBox(self.win)
      self.chooseButton.move(self.width / 2 - 150, 80)
      self.chooseButton.addItem("solve")
      self.chooseButton.addItem("lim")
      self.chooseButton.addItem("matrix")

      self.chooseButton.activated[str].connect(self.options)

   def Button(self):
      self.equation = self.mainLabel.text()
      print(self.equation)

   def options(self, text):
      print(text)

   def run(self):
      self.win.show()
      sys.exit(self.app.exec_())


if __name__ == '__main__': 
   window = gui()
   window.run()