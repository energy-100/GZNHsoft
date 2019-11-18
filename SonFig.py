import sys
import matplotlib
import os
matplotlib.use("Qt5Agg")
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Mydemo import *
class SonFigspot(QWidget):
    def __init__(self, funtype, statusBar,progressBar, datalist,selectfilename,figuremain,figureinf,selectfileComboBox, parent=None):
        super(SonFigspot, self).__init__(parent)
        self.figuremain=figuremain
        self.figureinf=figureinf
        self.selectfilename=selectfilename
        self.selectfileComboBox=selectfileComboBox
        self.progressBar=progressBar
        self.funtype=funtype
        self.setFont(QFont("Microsoft YaHei",12))
        self.statusBar=statusBar
        self.datalist=datalist
        self.currentedit=0


        # 添加控件
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.figure = Mydemo(width=10, height=10, dpi=100)
        self.grid.addWidget(self.figure, 0, 0, 1, 20)

        #文件选择列表
        self.selectfileComboBox.currentIndexChanged.connect(lambda: self.ChangeselectfileComboBox())
        self.grid.addWidget(self.selectfileComboBox, 1, 0, 1, 2)

        # 保存按钮
        self.SaveImageButton = QPushButton("保存图片")
        self.SaveImageButton.clicked.connect(self.SaveImage)
        self.grid.addWidget(self.SaveImageButton, 1, 2, 1, 1)
        # 线颜色
        self.LineColorButton = QPushButton("曲线颜色")
        self.LineColorButton.clicked.connect(lambda: self.LineColor())
        self.grid.addWidget(self.LineColorButton, 1, 3, 1, 1)
        # 线宽度标签
        self.LineWidthlabel = QLabel("线宽")
        self.LineWidthlabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.LineWidthlabel, 1, 5, 1, 1)

        # 线列表
        self.LineWidthComboBox = QComboBox()
        self.LineWidthComboBox.addItems(
            ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4",
             "1.5",
             "1.6", "1.7", "1.8,", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
             "3.0"])
        self.LineWidthComboBox.setCurrentIndex(9)
        self.LineWidthComboBox.currentIndexChanged.connect(lambda: self.LineWidth())
        self.grid.addWidget(self.LineWidthComboBox, 1, 6, 1, 1)

        # 点颜色
        self.spotColorButton = QPushButton("点颜色")
        self.spotColorButton.clicked.connect(lambda: self.SpotColor())
        self.grid.addWidget(self.spotColorButton, 1, 4, 1, 1)

        # 点宽度标签
        self.SpotWidthLabel = QLabel("点宽")
        self.SpotWidthLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.SpotWidthLabel, 1, 7, 1, 1)

        # 点宽度滑块
        self.SpotWidthComboBox = QComboBox()
        self.SpotWidthComboBox.addItems(
            ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4",
             "1.5",
             "1.6", "1.7", "1.8", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
             "3.0"])
        self.SpotWidthComboBox.setCurrentIndex(9)
        self.SpotWidthComboBox.currentIndexChanged.connect(lambda: self.SpotWidth())
        self.grid.addWidget(self.SpotWidthComboBox, 1, 8, 1, 1)

        # 添加标题标签
        self.titlelabel = QLabel("图标题")
        self.titlelabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.titlelabel, 1, 9, 1, 1)

        # 添加标题输入框
        self.titleLineEdit = QLineEdit(self)
        self.titleLineEdit.setPlaceholderText("默认显示函数公式")
        self.titleLineEdit.returnPressed.connect(lambda: self.TitleLineEdit())
        self.grid.addWidget(self.titleLineEdit, 1, 10, 1, 1)
        self.setLayout(self.grid)

    def LineColor(self):
        col = QColorDialog.getColor()
        # try:
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linecolor=col.name()
        # self.linecolor = col.name()
        self.plot()
        try:
            self.statusBar().showMessage("更新拟合曲线颜色为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linecolor))
        except Exception as a:
            print(a)

    def LineWidth(self):
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth = self.LineWidthComboBox.currentIndex() / 10 + 0.1
        # self.linewidth = self.LineWidthComboBox.currentIndex() / 10 + 0.1
        self.plot()
        try:
            self.statusBar().showMessage("更新拟合曲线线宽为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth))
        except Exception as a:
            print(a)
    def SpotWidth(self):
        # self.spotwidth = self.SpotWidthComboBox.currentIndex() * 3 + 3
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth = self.SpotWidthComboBox.currentIndex() * 3 + 3
        self.plot()
        try:
            self.statusBar().showMessage("更新原始数据散点大小为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth))
        except Exception as a:
            print(a)
    def SpotColor(self):
        col = QColorDialog.getColor()
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotcolor = col.name()
        # self.spotcolor = col.name()
        self.plot()
        try:
            self.statusBar().showMessage("更新原始数据颜色为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotcolor))
        except Exception as a:
            print(a)
    def SpotAlpha(self):
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha = self.BarAlphaComboBox.currentIndex()/10+0.1
        print(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha/10+0.1)
        # self.spotalpha = self.BarAlphaComboBox.currentIndex() / 10 + 0.1
        self.plot()
        try:
            self.statusBar().showMessage("更新原始数据透明度为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha))
        except Exception as a:
            print(a)
    def TitleLineEdit(self):
        print(self.titleLineEdit.text())
        print(type(self.titleLineEdit.text()))
        # self.figureinf.title= self.titleLineEdit.text()
        self.figureinf.temptitle = self.titleLineEdit.text()
        self.plot()
        try:
            if(self.figureinf.temptitle==""):
                self.statusBar().showMessage(self.funtype+"的图片标题更新为默认标题")
            else:
                self.statusBar().showMessage(self.funtype+"的图片标题更新为：" + str(self.figureinf.temptitle))
        except Exception as a:
            print(a)


    def ChangeselectfileComboBox(self):     #子图选取文件变化
        if(self.selectfileComboBox.count()!=0):
            print("开始")
            print(self.LineWidthComboBox.count())
            print(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth-0.1)*10))
            print(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth-3)/3))
            print(int(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha ))
            print("开始2")
            self.LineWidthComboBox.setCurrentIndex(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth-0.1)*10))
            print(self.SpotWidthComboBox.count())
            try:
                print("点宽度",self.SpotWidthComboBox.count())
                self.SpotWidthComboBox.blockSignals(True)
                self.SpotWidthComboBox.setCurrentIndex(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth-3)/3))
                self.SpotWidthComboBox.blockSignals(False)
            except Exception as a:
                print(a)
            print("结束2")

    def plot(self):
        print("this:")
        print(self.selectfilename)
        self.figure.fig.canvas.draw_idle()
        self.figure.axes.clear()
        if ((self.funtype == "双曲线拟合" )or (self.funtype == "指数拟合")):  # 双曲线画图
            for filename in self.selectfilename:
                if(self.datalist[filename].plotinf[self.funtype].paranum!="-"):
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
        elif ((self.funtype == "双曲线积分形式拟合")or(self.funtype == "指数积分形式拟合")):  # 双曲线画图
            for filename in self.selectfilename:
                if (self.datalist[filename].plotinf[self.funtype].paranum != "-"):
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
                    self.figure.axes.bar(xdata, ydata, width=dt,color=spotcolor, alpha=spotalpha,
                                             label=orlabel)
                    self.figure.axes.plot(xfit, yfit, linewidth=linewidth, color=linecolor,
                                          label=fitlabel)
        self.figure.axes.set_ylabel(self.figureinf.ylabel)
        self.figure.axes.set_xlabel(self.figureinf.xlabel)
        if(self.figureinf.temptitle==""):
            self.figure.axes.set_title(self.figureinf.title, color=self.figureinf.titlecolor)
        else:
            self.figure.axes.set_title(self.figureinf.temptitle, color=self.figureinf.titlecolor)
        self.figure.axes.legend()

    def SetPara(self,datalist):
        self.datalist=datalist

    def SaveImage(self):
        filename = ""
        print(self.selectfileComboBox.itemText(0))
        if (self.selectfileComboBox.count() == 0):
            return
        elif (self.selectfileComboBox.count() == 1):
            filename = self.selectfileComboBox.itemText(0).split(".")[0] + self.funtype + "(参数" + str(
                self.datalist[self.selectfileComboBox.itemText(0)].plotinf[self.funtype].paranum) + ").png"
        else:
            for i in range(self.selectfileComboBox.count()):
                filename += self.selectfileComboBox.itemText(i).split(".")[0] + "(参数" + str(
                    self.datalist[self.selectfileComboBox.itemText(i)].plotinf[self.funtype].paranum) + ")-"
            filename += self.funtype + "对比图片.png"

        print(self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/")
        print("图片成功保存到" + self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/" + filename)
        self.figure.axes.get_figure().savefig(
            self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/" + filename)
        self.statusBar().showMessage(
            "图片成功保存到" + self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/" + filename)
        print("cdcdc")


class SonFigbar(QWidget):
    def __init__(self, funtype, statusBar,progressBar, datalist,selectfilename,figuremain,figureinf,selectfileComboBox, parent=None):
        super(SonFigbar, self).__init__(parent)
        self.figuremain=figuremain
        self.figureinf=figureinf
        self.selectfilename=selectfilename
        self.selectfileComboBox=selectfileComboBox
        self.progressBar=progressBar
        self.funtype=funtype
        self.setFont(QFont("Microsoft YaHei",12))
        self.statusBar=statusBar
        self.datalist=datalist
        self.currentedit=0
        # 添加公共控件
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.figure = Mydemo(width=10, height=10, dpi=100)
        self.grid.addWidget(self.figure, 0, 0, 1, 20)

        #文件选择列表
        self.selectfileComboBox.currentIndexChanged.connect(lambda: self.ChangeselectfileComboBox())
        self.grid.addWidget(self.selectfileComboBox, 1, 0, 1, 2)

        # 保存按钮
        self.SaveImageButton = QPushButton("保存图片")
        self.SaveImageButton.clicked.connect(self.SaveImage)
        self.grid.addWidget(self.SaveImageButton, 1, 2, 1, 1)
        # 线颜色
        self.LineColorButton = QPushButton("曲线颜色")
        self.LineColorButton.clicked.connect(lambda: self.LineColor())
        self.grid.addWidget(self.LineColorButton, 1, 3, 1, 1)
        # 线宽度标签
        self.LineWidthlabel = QLabel("线宽")
        self.LineWidthlabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.LineWidthlabel, 1, 5, 1, 1)

        # 线列表
        self.LineWidthComboBox = QComboBox()
        self.LineWidthComboBox.addItems(
            ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4",
             "1.5",
             "1.6", "1.7", "1.8,", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
             "3.0"])
        self.LineWidthComboBox.setCurrentIndex(9)
        self.LineWidthComboBox.currentIndexChanged.connect(lambda: self.LineWidth())
        self.grid.addWidget(self.LineWidthComboBox, 1, 6, 1, 1)

        # bar颜色按钮
        self.BarColorButton = QPushButton("柱状图颜色")
        self.BarColorButton.clicked.connect(lambda: self.SpotColor())
        self.grid.addWidget(self.BarColorButton, 1, 4, 1, 1)

        # bar透明度标签
        self.BarAlphaLabel = QLabel("柱状图透明度")
        self.BarAlphaLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.BarAlphaLabel, 1, 7, 1, 1)


        # bar透明度列表
        self.BarAlphaComboBox = QComboBox()
        self.BarAlphaComboBox.addItems(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
        self.BarAlphaComboBox.setCurrentIndex(2)
        self.BarAlphaComboBox.currentIndexChanged.connect(lambda: self.SpotAlpha())
        self.grid.addWidget(self.BarAlphaComboBox, 1, 8, 1, 1)

        # 添加标题标签
        self.titlelabel = QLabel("图标题")
        self.titlelabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.grid.addWidget(self.titlelabel, 1, 9, 1, 1)

        # 添加标题输入框
        self.titleLineEdit = QLineEdit(self)
        self.titleLineEdit.setPlaceholderText("默认显示函数公式")
        self.titleLineEdit.returnPressed.connect(lambda: self.TitleLineEdit())
        self.grid.addWidget(self.titleLineEdit, 1, 10, 1, 1)
        self.setLayout(self.grid)

    def LineColor(self):
        col = QColorDialog.getColor()
        # try:
        if(col.isValid()and(self.selectfileComboBox.count()!=0)):
            self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linecolor=col.name()
            # self.linecolor = col.name()
            self.plot()
            try:
                self.statusBar().showMessage("更新拟合曲线颜色为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linecolor))
            except Exception as a:
                print(a)

    def LineWidth(self):
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth = self.LineWidthComboBox.currentIndex() / 10 + 0.1
        # self.linewidth = self.LineWidthComboBox.currentIndex() / 10 + 0.1
        self.plot()
        try:
            self.statusBar().showMessage("更新拟合曲线线宽为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth))
        except Exception as a:
            print(a)
    def SpotWidth(self):
        # self.spotwidth = self.SpotWidthComboBox.currentIndex() * 3 + 3
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth = self.SpotWidthComboBox.currentIndex() * 3 + 3
        self.plot()
        try:
            self.statusBar().showMessage("更新原始数据散点大小为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth))
        except Exception as a:
            print(a)
    def SpotColor(self):
        col = QColorDialog.getColor()
        if (col.isValid()and(self.selectfileComboBox.count()!=0)):
            self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotcolor = col.name()
            # self.spotcolor = col.name()
            self.plot()
            try:
                self.statusBar().showMessage("更新原始数据颜色为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotcolor))
            except Exception as a:
                print(a)
    def SpotAlpha(self):
        self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha = self.BarAlphaComboBox.currentIndex()/10+0.1
        print("透明度：")
        print(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha)
        # self.spotalpha = self.BarAlphaComboBox.currentIndex() / 10 + 0.1
        self.plot()
        try:
            self.statusBar().showMessage("更新原始数据透明度为" + str(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha))
        except Exception as a:
            print(a)
    def TitleLineEdit(self):
        print(self.titleLineEdit.text())
        print(type(self.titleLineEdit.text()))
        # self.figureinf.title= self.titleLineEdit.text()
        self.figureinf.temptitle = self.titleLineEdit.text()
        self.plot()
        try:
            if(self.figureinf.temptitle==""):
                self.statusBar().showMessage(self.funtype+"的图片标题更新为默认标题")
            else:
                self.statusBar().showMessage(self.funtype+"的图片标题更新为：" + str(self.figureinf.temptitle))
        except Exception as a:
            print(a)
    def ChangeselectfileComboBox(self):     #子图选取文件变化
        if(self.selectfileComboBox.count()!=0):
            print("开始")
            print(self.LineWidthComboBox.count())
            print(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth-0.1)*10))
            print(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotwidth-3)/3))
            print(int(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha ))
            print("开始2")
            self.LineWidthComboBox.blockSignals(True)
            self.LineWidthComboBox.setCurrentIndex(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].linewidth-0.1)*10))
            self.LineWidthComboBox.blockSignals(False)

            print("块透明度",self.BarAlphaComboBox.count())


            self.BarAlphaComboBox.blockSignals(True)
            self.BarAlphaComboBox.setCurrentIndex(int(((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha)-0.1)*10))
            print("最终透明度：")
            print(self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha)
            print(int((self.datalist[self.selectfileComboBox.currentText()].plotinf[self.funtype].spotalpha)-0.1*10))
            self.BarAlphaComboBox.blockSignals(False)
            print("结束2")

    def plot(self):
        print("this:")
        print(self.selectfilename)
        self.figure.fig.canvas.draw_idle()
        self.figure.axes.clear()
        if ((self.funtype == "双曲线拟合" )or (self.funtype == "指数拟合")):  # 双曲线画图
            for filename in self.selectfilename:
                if(self.datalist[filename].plotinf[self.funtype].paranum!="-"):
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
        elif ((self.funtype == "双曲线积分形式拟合")or(self.funtype == "指数积分形式拟合")):  # 双曲线画图
            for filename in self.selectfilename:
                if (self.datalist[filename].plotinf[self.funtype].paranum != "-"):
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
                    self.figure.axes.bar(xdata, ydata, width=dt,color=spotcolor, alpha=spotalpha,
                                             label=orlabel)
                    self.figure.axes.plot(xfit, yfit, linewidth=linewidth, color=linecolor,
                                          label=fitlabel)
        self.figure.axes.set_ylabel(self.figureinf.ylabel)
        self.figure.axes.set_xlabel(self.figureinf.xlabel)
        if(self.figureinf.temptitle==""):
            self.figure.axes.set_title(self.figureinf.title, color=self.figureinf.titlecolor)
        else:
            self.figure.axes.set_title(self.figureinf.temptitle, color=self.figureinf.titlecolor)
        self.figure.axes.legend()

    def SetPara(self,datalist):
        self.datalist=datalist

    def SaveImage(self):
        filename=""
        print(self.selectfileComboBox.itemText(0))
        if(self.selectfileComboBox.count()==0):
            return
        elif(self.selectfileComboBox.count()==1):
            filename=self.selectfileComboBox.itemText(0).split(".")[0]+self.funtype+"(参数"+str(self.datalist[self.selectfileComboBox.itemText(0)].plotinf[self.funtype].paranum)+").png"
        else:
            for i in range(self.selectfileComboBox.count()):
                filename += self.selectfileComboBox.itemText(i).split(".")[0] +"(参数"+str(self.datalist[self.selectfileComboBox.itemText(i)].plotinf[self.funtype].paranum)+")-"
            filename += self.funtype + "对比图片.png"


        print(self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/")
        print("图片成功保存到" + self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/"+filename)
        self.figure.axes.get_figure().savefig(self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/" + filename)
        self.statusBar().showMessage("图片成功保存到" + self.datalist[self.selectfileComboBox.itemText(0)].rootpath + "/"+filename)
        print("cdcdc")