import sys, random, time, win32event, pywintypes, win32api
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QWidget, QMessageBox,
                             QHBoxLayout, QGridLayout, QVBoxLayout, QLabel, QFrame,
                             QLCDNumber, QPushButton, QToolButton)


class APP(QWidget):
    def __init__(self):
        super(APP, self).__init__()
        self.variable()
        self.Interface()
        self.center()
        self.Preset()
        self.link()

    def Preset(self):  # 打开游戏预设
        self.Randomgeneration()
        self.timer = QTimer()  # 建立计时器

    def variable(self):  # 各种变量
        self.cell = dict()  # 储存全部像素点组件
        self.cells = list()  # 储存全部像素点
        self.snake = [(12, 12)]  # 蛇所占的像素点
        self.fruit = tuple()  # 果实的位置
        self.direction = (0, 0)  # 方向键位置
        self.startsuspend = 'suspend'
        self.speed = 400  # 初始速度
        self.lock = 0  # 键盘锁，防止快速连按

    def Interface(self):  # 界面
        self.setWindowTitle('贪吃蛇')  # 标题
        self.setFixedSize(525, 325)  # 限制窗口大小
        self.grabKeyboard()  # 窗口接收键盘事件

        self.Floor = QHBoxLayout()

        self.Form1 = QFrame()
        self.Form1.setFrameShape(QFrame.Panel | QFrame.Plain)
        self.Form1.setFixedSize(293, 293)

        self.grid = QGridLayout()
        self.grid.setSpacing(1)
        self.Form1.setLayout(self.grid)

        self.Floor.addWidget(self.Form1)

        for row in range(25):
            for col in range(25):
                self.cell[(row, col)] = QLabel()
                self.cell[(row, col)].setStyleSheet(
                    'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
                self.cell[(row, col)].setFixedSize(10, 10)
                self.grid.addWidget(self.cell[(row, col)], row, col)

                self.cells.append((row, col))

        self.Form2 = QFrame()
        self.Form2.setFrameShape(QFrame.Panel | QFrame.Plain)
        self.Form2.setFixedSize(200, 293)

        self.box = QVBoxLayout()
        self.Form2.setLayout(self.box)

        self.Floor.addWidget(self.Form2)

        self.integral = QLCDNumber()
        self.integral.setFixedHeight(50)
        self.box.addWidget(self.integral)

        self.Speed = QLabel(str(int(100000 / self.speed) / 100) + '\n格/秒')
        self.Speed.setFont(QFont('宋体', 24))
        self.box.addWidget(self.Speed)

        self.Button1 = QPushButton('开始')
        self.Button1.setFixedHeight(50)
        self.Button1.setFont(QFont('宋体', 25, 75))
        self.Button1.setStyleSheet(
            "QPushButton{color:white;background:LimeGreen;border-radius:20px;border:3px solid black;}")
        self.box.addWidget(self.Button1)

        self.Button2 = QPushButton('重置')
        self.Button2.setFixedHeight(50)
        self.Button2.setFont(QFont('宋体', 25, 75))
        self.Button2.setStyleSheet(
            "QPushButton{color:white;background:Orange;border-radius:20px;border:3px solid black;}")
        self.box.addWidget(self.Button2)

        self.setLayout(self.Floor)

    def StartSuspend(self):  # 开始或暂停游戏
        if self.startsuspend == 'start':
            self.startsuspend = 'suspend'
            self.timer.stop()
            self.Button1.setText('继续')
            self.Button1.setStyleSheet(
                "QPushButton{color:white;background:LimeGreen;border-radius:20px;border:3px solid black;}")
        else:
            self.startsuspend = 'start'
            self.speed = 400 - int((len(self.snake) - 1) / 25 * 10)
            self.timer.start(self.speed)
            self.Button1.setText('暂停')
            self.Button1.setStyleSheet(
                "QPushButton{color:white;background:OrangeRed;border-radius:20px;border:3px solid black;}")

    def keyPressEvent(self, event):  # 响应键盘操作
        if event.key() == Qt.Key_Left:
            if self.direction != (0, 1) and self.lock == 0:
                self.direction = (0, -1)
        if event.key() == Qt.Key_Right:
            if self.direction != (0, -1) and self.lock == 0:
                self.direction = (0, 1)
        if event.key() == Qt.Key_Up:
            if self.direction != (1, 0) and self.lock == 0:
                self.direction = (-1, 0)
        if event.key() == Qt.Key_Down:
            if self.direction != (-1, 0) and self.lock == 0:
                self.direction = (1, 0)
        self.lock = 1

    def Randomgeneration(self):  # 随机生成果子
        tempdict = self.cells.copy()
        for cell in self.snake:
            tempdict.remove(cell)
        self.fruit = random.choice(tempdict)

    def Refresh(self):  # 刷新界面
        self.cell[self.fruit].setStyleSheet(
            'QLabel{background-color:red;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
        head = self.snake[0]
        head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.lock = 0
        self.snake.insert(0, head)

        if head == self.fruit:  # 如果吃到果子，则再次随机产生新的果子
            self.Randomgeneration()
        else:  # 如果没有吃到果子，删除尾巴的像素点
            tail = self.snake.pop()
            self.cell[tail].setStyleSheet(
                'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')

        temp = self.snake.copy()
        temp.remove(head)
        if head in temp:  # 咬到自己判负
            self.timer.stop()
            QMessageBox.warning(self, '信息', 'GAME OVER!', QMessageBox.Ok)
            self.Reset()
        elif (-1 in head) or (25 in head):  # 出边界判负
            self.timer.stop()
            QMessageBox.warning(self, '信息', 'GAME OVER!', QMessageBox.Ok)
            self.Reset()
        elif len(self.snake) == 625:  # 占满屏幕获胜
            self.timer.stop()
            QMessageBox.warning(self, '信息', 'YOU WIN!', QMessageBox.Ok)
            self.Reset()
        else:  # 未分出结果时
            self.cell[head].setStyleSheet(
                'QLabel{background-color:green;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            self.integral.display(len(self.snake) - 1)  # 显示分数

            if self.speed != 400 - int((len(self.snake) - 1) / 25 * 10):  # 根据身长改变移动速度
                self.speed = 400 - int((len(self.snake) - 1) / 25 * 10)
                self.Speed.setText(str(int(100000 / self.speed) / 100) + '\n格/秒')
                self.timer.start(self.speed)

    def Reset(self):  # 重置游戏
        self.timer.stop()
        self.snake = [(12, 12)]  # 蛇所占的像素点
        self.fruit = tuple()  # 果实的位置
        self.direction = (0, 0)  # 方向键位置
        self.startsuspend = 'suspend'
        self.Button1.setText('开始')
        self.Button1.setStyleSheet(
            "QPushButton{color:white;background:LimeGreen;border-radius:20px;border:3px solid black;}")
        self.speed = 400  # 初始速度
        self.Speed.setText(str(int(100000 / self.speed) / 100) + '\n格/秒')
        self.lock = 0  # 键盘锁，防止快速连按
        self.Randomgeneration()  # 随机产生果实
        for row in range(25):
            for col in range(25):
                self.cell[(row, col)].setStyleSheet(
                    'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')

    def center(self):  # 窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def link(self):
        self.Button1.clicked.connect(self.StartSuspend)
        self.Button2.clicked.connect(self.Reset)
        self.timer.timeout.connect(self.Refresh)

    def closeEvent(self, event):
        self.timer.stop()  # 退出时结束计时器


if __name__ == '__main__':
    ERROR_ALREADY_EXISTS = 183
    sz_mutex = "test_mutex"
    hmutex = win32event.CreateMutex(None, pywintypes.FALSE, sz_mutex)
    if win32api.GetLastError() == ERROR_ALREADY_EXISTS:
        exit(0)
    else:
        app = QApplication(sys.argv)
        xianshi = APP()
        xianshi.show()
        sys.exit(app.exec_())
