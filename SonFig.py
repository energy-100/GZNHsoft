import sys
import matplotlib
import os
matplotlib.use("Qt5Agg")
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Mydemo import *
class SonFig(QWidget):
    def __init__(self, funtype, statusBar,progressBar, datalist,selectfilename,figuremain,figureinf, parent=None):
        super(SonFig, self).__init__(parent)
        self.figuremain=figuremain
        self.figureinf=figureinf
        self.selectfilename=selectfilename
        self.progressBar=progressBar
        self.funtype=funtype
        self.setFont(QFont("Microsoft YaHei",10.5))
        self.statusBar=statusBar
        self.datalist=datalist
        self.currentedit=0
        # 添加公共控件
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.figure = Mydemo(width=10, height=10, dpi=100)
        self.grid.addWidget(self.figure, 0, 0, 1, 20)
        # 保存按钮
        self.SaveImageButton = QPushButton("SaveImage")
        self.SaveImageButton.clicked.connect(self.SaveImage)
        self.grid.addWidget(self.SaveImageButton, 1, 0, 1, 1)
        # 线颜色
        self.LineColorButton = QPushButton("LineColor")
        self.LineColorButton.clicked.connect(lambda: self.LineColor())
        self.grid.addWidget(self.LineColorButton, 1, 1, 1, 1)

        # 添加私有控件
        if (self.funtype == "指数积分形式拟合" or self.funtype == "双曲线积分形式拟合"):
            # bar颜色按钮
            self.BarColorButton = QPushButton("BarColor")
            self.BarColorButton.clicked.connect(lambda: self.SpotColor())
            self.grid.addWidget(self.BarColorButton, 1, 2, 1, 1)

            # 线宽度标签
            self.LineWidthlabel = QLabel("LineWidth")
            self.LineWidthlabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.grid.addWidget(self.LineWidthlabel, 1, 3, 1, 1)

            # 线列表
            self.LineWidthComboBox = QComboBox()

            self.LineWidthComboBox.addItems(
                ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4",
                 "1.5",
                 "1.6", "1.7", "1.8,", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
                 "3.0"])
            self.LineWidthComboBox.setCurrentIndex(9)
            self.LineWidthComboBox.currentIndexChanged.connect(lambda: self.LineWidth())
            self.grid.addWidget(self.LineWidthComboBox, 1, 4, 1, 1)

            # bar透明度标签
            self.BarAlphaLabel = QLabel("BarAlpha")
            self.BarAlphaLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.grid.addWidget(self.BarAlphaLabel, 1, 5, 1, 1)

            # bar透明度列表
            self.BarAlphaComboBox = QComboBox()

            self.BarAlphaComboBox.addItems(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
            self.BarAlphaComboBox.setCurrentIndex(2)
            self.BarAlphaComboBox.currentIndexChanged.connect(lambda: self.SpotAlpha())
            self.grid.addWidget(self.BarAlphaComboBox, 1, 6, 1, 1)

        elif (self.funtype == "指数拟合" or self.funtype =="双曲线拟合"):
            # 点颜色
            self.spotColorButton = QPushButton("SpotColor")
            self.spotColorButton.clicked.connect(lambda: self.SpotColor())
            self.grid.addWidget(self.spotColorButton, 1, 2, 1, 1)

            # 线宽度标签
            self.LineWidthlabel = QLabel("LineWidth")
            self.LineWidthlabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.grid.addWidget(self.LineWidthlabel, 1, 3, 1, 1)

            # 线下拉框
            self.LineWidthComboBox = QComboBox()

            self.LineWidthComboBox.addItems(
                ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4",
                 "1.5",
                 "1.6", "1.7", "1.8", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
                 "3.0"])
            self.LineWidthComboBox.setCurrentIndex(8)
            self.LineWidthComboBox.currentIndexChanged.connect(lambda: self.LineWidth())
            self.grid.addWidget(self.LineWidthComboBox, 1, 4, 1, 1)

            # 点宽度标签
            self.SpotWidthLabel = QLabel("SpotWidth")
            self.SpotWidthLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.grid.addWidget(self.SpotWidthLabel, 1, 5, 1, 1)

            # 点宽度滑块
            self.SpotWidthComboBox = QComboBox()

            self.SpotWidthComboBox.addItems(
                ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4",
                 "1.5",
                 "1.6", "1.7", "1.8", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
                 "3.0"])
            self.SpotWidthComboBox.setCurrentIndex(9)
            self.SpotWidthComboBox.currentIndexChanged.connect(lambda: self.SpotWidth())
            self.grid.addWidget(self.SpotWidthComboBox, 1, 6, 1, 1)
            # 添加公共控件

            # 添加标题标签
        self.titlelabel = QLabel("TitleText")
        self.titlelabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.titlelabel, 1, 7, 1, 1)

        # 添加标题输入框
        self.titleLineEdit = QLineEdit(self)
        self.titleLineEdit.setPlaceholderText("函数公式")
        self.titleLineEdit.returnPressed.connect(lambda: self.TitleLineEdit())
        self.grid.addWidget(self.titleLineEdit, 1, 8, 1, 1)
        self.setLayout(self.grid)

    def LineColor(self):
        col = QColorDialog.getColor()
        self.linecolor = col.name()
        self.plot()
        self.statusBar.showMessage("更新拟合曲线颜色为" + str(col.name()))

    def LineWidth(self):
        self.linewidth = self.LineWidthComboBox.currentIndex() / 10 + 0.1
        self.plot()
        self.statusBar.showMessage("更新拟合曲线线宽为" + str(self.linewidth))

    def SpotWidth(self):
        self.spotwidth = self.SpotWidthComboBox.currentIndex() * 3 + 3
        self.plot()
        self.statusBar.showMessage("更新原始数据散点大小为" + str(self.spotwidth))

    def SpotColor(self):
        col = QColorDialog.getColor()
        self.spotcolor = col.name()
        self.plot()
        self.statusBar.showMessage("更新原始数据颜色为" + str(self.spotcolor))

    def SpotAlpha(self):
        self.spotalpha = self.BarAlphaComboBox.currentIndex() / 10 + 0.1
        self.plot()
        self.statusBar.showMessage("更新原始数据透明度为" + str(self.spotalpha))

    def TitleLineEdit(self):
        print(self.titleLineEdit.text())
        print(type(self.titleLineEdit.text()))
        self.title = self.titleLineEdit.text()
        self.plot()
        self.statusBar.showMessage("图片标题更新为：" + str(self.title))

    def plot(self):
        self.figure.fig.canvas.draw_idle()
        self.figure.axes.clear()
        if (self.funtype == "双曲线拟合" or self.funtype == "指数拟合"):  # 双曲线画图
            for filename in self.selectfilename:
                file = self.datalist[filename].plotinf[self.funtype]
                xdata = file.xdata
                ydata = file.ydata
                xfit = file.xfit
                yfit = file.yfit
                spotwidth = file.spotwidth
                spotcolor = file.spotcolor
                linewidth = file.linewidth
                linecolor = file.linecolor
                spotalpha = file.spotalpha
                orlabel = file.orlabel
                fitlabel = file.fitlabel

                self.figure.axes.scatter(xdata, ydata, spotwidth, spotcolor, alpha=spotalpha,
                                         label=orlabel)
                self.figure.axes.plot(xfit, yfit, linewidth=linewidth, color=linecolor,
                                      label=fitlabel)
        elif (self.funtype == "双曲线积分拟合" or self.funtype == "指数积分拟合"):  # 双曲线画图
            for filename in self.selectfilename:
                file = self.datalist[filename].plotinf[self.funtype]
                xdata = file.xdata
                ydata = file.ydata
                xfit = file.xfit
                yfit = file.yfit
                spotwidth = file.spotwidth
                spotcolor = file.spotcolor
                linewidth = file.linewidth
                linecolor = file.linecolor
                spotalpha = file.spotalpha
                orlabel = file.orlabel
                fitlabel = file.fitlabel
                dt = self.datalist[filename].dt
                self.figure.axes.barbar(xdata, ydata, width=dt,color=spotcolor, alpha=spotalpha,
                                         label=orlabel)
                self.figure.axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,
                                      label=fitlabel)
        self.figure.axes.set_ylabel(self.figureson[self.funtype].ylabel)
        self.figure.axes.set_xlabel(self.figureson[self.funtype].xlabel)
        self.figure.axes.set_title(self.figureson[self.funtype].title, self.figureson[self.funtype].titlecolor)

    def SetPara(self,datalist):
        self.datalist=datalist

    def SaveImage(self):
        print(self.filepath + "/" + self.filename + "指数拟合图-第" + str(self.paranum) + "组参数" + ".png")
        self.figure.axes.get_figure().savefig(
            self.filepath + "/" + self.filename + "指数拟合图-第" + str(self.paranum) + "组参数" + ".png")
        self.statusBar.showMessage(
            "图片成功保存到" + self.filepath + "/" + self.filename + "指数拟合图-第" + str(self.paranum) + "组参数" + ".png")
