import PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys

app = QApplication(sys.argv)
window = QMainWindow()

window.statusBar().showMessage("欢迎来到PyQT6课程")  # 只有QMainWindow才能创建
window.menuBar().addMenu("File")  # 只有QMainWindow才能创建

window.show()
sys.exit(app.exec())