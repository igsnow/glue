import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self._init_ui()

    def _init_ui(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Window with Button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
