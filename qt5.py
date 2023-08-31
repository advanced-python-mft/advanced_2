from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys

def clicked():
    print("clicked")
    
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("first")
    
    
    label = QtWidgets.QLabel(win)
    label.setText("file")
    label.move(50,50)
    
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Game start")
    b1.clicked.connect(clicked)
    b1.setStyleSheet("""
                     QWidget{
                         border 2px solid aqu
                         border-radius: 8px
                     }
                     """)
    
    win.show()
    sys.exit(app.exec_())
    
window()