from PyQt5.QtGui import *
from Mydemo import *
from DataClass import *
from PyQt5.QtWidgets import *
import os
from PyQt5 import QtCore
from SonFig import SonFigspot,SonFigbar
class MainUI(QWidget):
    def __init__(self,statusBar,progressBar,datalist,selectfilename,figuremain,figureson,figureinf,selectfileComboBox,parent=None):
        super(MainUI, self).__init__(parent)
        self.selectfileComboBox=selectfileComboBox
        self.colorlist=["blue","red","green","black","yellow"]
        self.singleplot=1
        self.datatype=3
        self.singlefilename=""
        self.openfile_path=""
        self.filename=""
        self.figureinf=figureinf
        self.figure=figuremain
        self.figureson=figureson
        self.selectfilename=selectfilename
        self.statusBar = statusBar
        self.progressBar=progressBar
        self.datalist=datalist
        self.splitter = QSplitter(Qt.Vertical)
        self.hbox = QVBoxLayout(self)
        self.grid1 = QGridLayout(self)
        self.grid2 = QGridLayout(self)
        self.grid1.setSpacing(10)
        self.grid2.setSpacing(10)
        self.complete=0
        # self.figure["双曲线拟合"] = Mydemo(width=5, height=3, dpi=100)
        self.grid1.addWidget(self.figure["双曲线拟合"], 0, 0, 1, 15)

        # self.figure["指数拟合"] = Mydemo(width=5, height=3, dpi=100)
        self.grid1.addWidget(self.figure["指数拟合"], 0, 15, 1, 15)

        # self.figure["双曲线积分形式拟合"] = Mydemo(width=5, height=3, dpi=100)
        self.grid1.addWidget(self.figure["双曲线积分形式拟合"], 1, 0, 1, 15)

        # self.figure["指数积分形式拟合"] = Mydemo(width=5, height=3, dpi=100)
        self.grid1.addWidget(self.figure["指数积分形式拟合"], 1, 15, 1, 15)

        self.label_1 = QLabel("数据文件列表：")
        self.grid2.addWidget(self.label_1, 0, 0, 1, 5)
        self.label_2 = QLabel("可拟合的函数类型：")
        self.grid2.addWidget(self.label_2, 0, 5, 1, 5)

        self.listwidget1 = QListWidget(self)
        self.listwidget1.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.listwidget1.customContextMenuRequested.connect(self.generateMenu1)
        self.listwidget1.setAlternatingRowColors(True)
        self.grid2.addWidget(self.listwidget1, 1, 0, 8, 5)
        self.listwidget1.clicked.connect(lambda: self.listwidget1_clicked())

        self.listwidget2 = QListWidget(self)
        self.listwidget2.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.listwidget2.customContextMenuRequested.connect(self.generateMenu2)
        self.listwidget2.setAlternatingRowColors(True)
        self.grid2.addWidget(self.listwidget2, 1, 5, 3, 5)
        self.listwidget2.clicked.connect(lambda: self.listwidget2_clicked())

        self.label_3 = QLabel("选中的文件列表及对应的参数拟合序号：(默认使用第一组参数进行拟合，若更改为其他参数则高亮显示)")
        self.grid2.addWidget(self.label_3, 4, 5, 1, 10)

        self.listwidget3 = QTableWidget(0,0)
        self.listwidget3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listwidget3.customContextMenuRequested.connect(self.generateMenu3)
        # self.listwidget3.customContextMenuRequested.connect(lambda:self.generateMenu3)
        self.listwidget3.setAlternatingRowColors(True)
        self.listwidget3.setHorizontalHeaderLabels(['文件名称', '双曲线参数序号', '指数参数序号', '双曲线积分参数序号', '指数积分参数序号'])
        # self.listwidget3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.listwidget3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listwidget3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.listwidget3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.listwidget3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.listwidget3.horizontalHeader().setStretchLastSection(True)
        self.grid2.addWidget(self.listwidget3, 1, 10, 3, 10)
        self.listwidget3.clicked.connect(lambda: self.listwidget3_clicked())

        self.label_4 = QLabel("参数列表：(右键复制数据，默认使用第一组参数进行拟合，若更改为其他参数则高亮显示)")
        self.grid2.addWidget(self.label_4, 0, 10, 1, 10)

        self.tableWidget = QTableWidget(0,5)
        self.tableWidget.itemChanged.connect(lambda:self.changetableWidget())
        # self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tableWidget.customContextMenuRequested.connect(self.generateMenu4)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalHeaderLabels(['文件名称', '双曲线参数序号', '指数参数序号', '双曲线积分参数序号', '指数积分参数序号'])
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.grid2.addWidget(self.tableWidget, 5, 5, 4, 15)



        self.loadfileButton = QPushButton("添加文件夹", self)
        self.loadfileButton.clicked.connect(lambda:self.openfile())
        self.grid2.addWidget(self.loadfileButton, 9, 0, 1, 2)

        self.saveImageButton = QPushButton("保存图片", self)
        self.saveImageButton.clicked.connect(lambda:self.SaveImage())
        self.grid2.addWidget(self.saveImageButton, 9, 2, 1,2)

        self.deleteselectfileButton = QPushButton("删除对比文件", self)
        self.deleteselectfileButton.clicked.connect(lambda:self.deletefile())
        self.grid2.addWidget(self.deleteselectfileButton, 9, 5, 1, 2)

        self.clearfileButton = QPushButton("清空对比文件", self)
        self.clearfileButton.clicked.connect(lambda:self.clearfile())
        self.grid2.addWidget(self.clearfileButton, 9, 7, 1, 2)

        self.deleteselectfileButton.blockSignals(True)
        self.clearfileButton.blockSignals(True)
        self.saveImageButton.blockSignals(True)

        self.singleComboBox = QComboBox()
        self.singleComboBox.addItems(
            ["单文件分析","多文件分析"])
        self.singleComboBox.setCurrentIndex(0)
        self.singleComboBox.currentIndexChanged.connect(lambda:self.ChangedsingleComboBox())
        self.grid2.addWidget(self.singleComboBox, 9, 9, 1, 2)

        self.datatypeComboBox = QComboBox()
        self.datatypeComboBox.addItems(
            ["原数据+拟合数据","只显示原数据","只显示拟合数据"])
        self.datatypeComboBox.setCurrentIndex(0)
        self.datatypeComboBox.currentIndexChanged.connect(lambda:self.ChangeddatatypeComboBox())
        self.grid2.addWidget(self.datatypeComboBox, 9, 11, 1, 2)

        Q1 = QtWidgets.QWidget()
        Q2 = QtWidgets.QWidget()
        Q1.setLayout(self.grid1)
        Q2.setLayout(self.grid2)
        self.hbox.addWidget(Q1)
        self.hbox.addWidget(Q2)
        self.setLayout(self.hbox)

    def SaveImage(self):
        if(self.singleplot==1):
            filename , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
            # print("保存位置",self.openfile_path+"/"+filename1+"双曲线拟合图"+".jpg")
            for fig in self.figure:
                self.figure[fig].axes.get_figure().savefig(self.openfile_path+"/"+filename+str(fig)+".png")
        else:

            for fig in self.figure:
                filename=self.openfile_path+"/"
                for i in range(self.tableWidget.rowCount()):
                    filenametemp,_=os.path.splitext(self.tableWidget.item(i, 0).text())
                    filename+=filenametemp
                filename+="文件"+fig+"对比图片.png"
                try:
                    print(filename)
                    self.figure[fig].axes.get_figure().savefig(filename)
                except Exception as a:
                    print(a)
    def openfile(self):
        self.statusBar().showMessage("正在选择文件...")

        path="C:/Users/ENERGY/Desktop/工作文件/lhy"
        # path= QFileDialog.getExistingDirectory(self, "请选择数据文件的根目录")
        self.statusBar().showMessage("数据加载中...")
        self.progressBar.setVisible(True)
        if(path!=""):
            # self.listwidget1.clear()
            if(os.path.exists(path+ "/处理后的原始数据/")):
                # self.label_1.setText('"'+path+'"路径下的数据文件：')
                self.openfile_path=path
                files=self.FileRead(self.openfile_path+ "/处理后的原始数据")
                for file in files:
                    data=DataClass()
                    data.filename=file
                    data.filename=file
                    data.setaxisLabel(file)
                    data.filepath=self.openfile_path+ "/处理后的原始数据"
                    data.rootpath=self.openfile_path
                    ordata = np.loadtxt(self.openfile_path + "/处理后的原始数据/" + file)
                    data.Setordata(ordata[:,0],ordata[:,1],ordata[0,2])
                    if (os.path.exists(self.openfile_path + "\双曲线拟合\\" + file)):
                        data.plotinf["双曲线拟合"].paranum= 0
                        data.plotinf["双曲线拟合"].fun=1
                        # self.listwidget2.addItem("双曲线拟合")
                        paraslist = self.DataRead(self.openfile_path + "\双曲线拟合\\" + file)
                        for para in paraslist:
                            paras = [float(i) for i in para.split()]
                            # self.plot(paras)
                            data.plotinf["双曲线拟合"].paras.append(paras)
                        # print("单击结束1")
                    self.progressBar.setValue(25)
                    if (os.path.exists(self.openfile_path + "\指数拟合\\" + file)):
                        data.plotinf["指数拟合"].paranum= 0
                        data.plotinf["指数拟合"].fun = 1
                        self.statusBar().showMessage("正在加载图片2/4")
                        # self.listwidget2.addItem("指数拟合")
                        paraslist = self.DataRead(self.openfile_path + "\指数拟合\\" + file)
                        for para in paraslist:
                            paras = [float(i) for i in para.split()]
                            # self.plot(paras)
                            data.plotinf["指数拟合"].paras.append(paras)
                            # print("单击结束2")
                    self.progressBar.setValue(50)
                    if (os.path.exists(self.openfile_path + "\双曲线积分形式拟合\\" + file)):
                        data.plotinf["双曲线积分形式拟合"].paranum= 0
                        data.plotinf["双曲线积分形式拟合"].fun = 1
                        self.statusBar().showMessage("正在加载图片3/4")
                        # self.listwidget2.addItem("双曲线积分形式拟合")
                        paraslist = self.DataRead(self.openfile_path + "\双曲线积分形式拟合\\" + file)
                        for para in paraslist:
                            paras = [float(i) for i in para.split()]
                            # self.plot(paras)
                            data.plotinf["双曲线积分形式拟合"].paras.append(paras)
                            # print("单击结束3")
                    self.progressBar.setValue(75)
                    if (os.path.exists(self.openfile_path + "\指数积分形式拟合\\" + file)):
                        data.plotinf["指数积分形式拟合"].paranum= 0
                        data.plotinf["指数积分形式拟合"].fun= 1
                        self.statusBar().showMessage("正在加载图片4/4")
                        # self.listwidget2.addItem("指数积分形式拟合")
                        paraslist = self.DataRead(self.openfile_path + "\指数积分形式拟合\\" + file)
                        for para in paraslist:
                            paras = [float(i) for i in para.split()]
                            # self.plot(paras)
                            data.plotinf["指数积分形式拟合"].paras.append(paras)
                            # print("单击结束4")
                    self.progressBar.setValue(100)
                    self.datalist[file]=data
                # self.listwidget1.clear()
                self.listwidget1.clear()
                for filename in self.datalist:
                    self.listwidget1.addItem(filename)
                self.statusBar().showMessage("数据文件加载完成，请选择数据文件")
                # self.statusBar().showMessage("请选择一组数据文件，默认使用第一组参数进行拟合。")
                # print(self.datalist)
            else:
                self.statusBar().showMessage("文件夹错误！(此文件夹内没有数据文件或文件夹内数据格式错误)")
        elif(self.openfile_path!=""):
            self.statusBar().showMessage("未更新数据文件！")
        else:
            self.statusBar().showMessage("请点击'Load File'按钮选择文数据目录...")
        self.progressBar.setVisible(False)

    def listwidget1_clicked(self):
        # if(self.singleplot==1):
        self.statusBar().showMessage("正在加载数据...")
        # self.progressBar.setVisible(True)
        self.listwidget3.clear()
        self.listwidget3.setRowCount(0)
        self.listwidget3.setColumnCount(0)
        # self.label2.setVisible(True)
        item = QListWidgetItem(self.listwidget1.currentItem()).text()
        self.singlefilename = item

        # self.label_2.setText("("+item+"）文件可拟合的数据类型：")
        # self.ordata=np.loadtxt(self.openfile_path + "/处理后的原始数据/"+item)
        filename=QListWidgetItem(self.listwidget1.currentItem()).text()


        find = self.tableWidget.findItems(filename, QtCore.Qt.MatchExactly)
        if (self.singleplot == 1):
            # self.selectfilename.clear()
            # self.selectfilename.append(item)
            # for box in self.selectfileComboBox:
            #     self.selectfileComboBox.clear()
            #     self.selectfileComboBox.addItem(item)
            self.selectfilename.clear()
            self.selectfilename.append(item)
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            if item not in self.selectfilename:
                self.selectfilename.append(item)

            if (not find):
                # self.selectfileComboBox.addItem(item)
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                print(self.tableWidget.rowCount())
                row=self.datalist.get(item).select()
                try:
                    for i in range(len(row)):
                        self.tableWidget.setItem(self.tableWidget.rowCount()-1,i,QTableWidgetItem(row[i]))
                        if(str.isdigit(row[i])):
                            if(int(row[i])!=1):
                                self.tableWidget.item(self.tableWidget.rowCount()-1, i).setBackground(QBrush(QColor(240, 125, 80)))
                except Exception as a:
                    print("20196:")
                    print(a)



        elif(self.singleplot==0):
            if item not in self.selectfilename:
                self.selectfilename.append(item)
            if (not find):
                # self.selectfileComboBox.addItem(item)
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                row=self.datalist.get(item).select()
                print(self.tableWidget.rowCount())
                try:
                    for i in range(len(row)):
                        self.tableWidget.setItem(self.tableWidget.rowCount()-1,i,QTableWidgetItem(row[i]))
                        if(str.isdigit(row[i])):
                            if(int(row[i])!=1):
                                self.tableWidget.item(self.tableWidget.rowCount()-1, i).setBackground(QBrush(QColor(240, 125, 80)))
                except Exception as a:
                    print("20196:")
                    print(a)
        self.listwidget2.clear()
        if(self.datalist[item].plotinf["双曲线拟合"].fun==1):
            self.listwidget2.addItem("双曲线拟合")
        if(self.datalist[item].plotinf["指数拟合"].fun==1):
            self.listwidget2.addItem("指数拟合")
        if(self.datalist[item].plotinf["指数积分形式拟合"].fun==1):
            self.listwidget2.addItem("指数积分形式拟合")
        if(self.datalist[item].plotinf["双曲线积分形式拟合"].fun==1):
            self.listwidget2.addItem("双曲线积分形式拟合")
        # self.statusBar().showMessage("默认使用第一组参数进行拟合，如需更换参数组合，请先选择要修改拟合类型!")
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)
        self.statusBar().showMessage("正在生成拟合曲线...")
        self.datalist[filename].calculatefit()
        self.progressBar.setValue(50)
        self.statusBar().showMessage("正在绘图...")
        self.plotall()
        self.progressBar.setVisible(False)
        self.statusBar().showMessage('已加载"'+item+'"数据文件的四种拟合曲线！(默认使用第一组参数)')

    def listwidget2_clicked(self):
        item = QListWidgetItem(self.listwidget2.currentItem()).text()
        paras=self.datalist[QListWidgetItem(self.listwidget1.currentItem()).text()].plotinf[item].paras
        self.listwidget3.clear()
        self.listwidget3.setRowCount(len(paras))
        if(item=="双曲线拟合"):
            self.listwidget3.setColumnCount(len(paras[0]) - 3)
            self.listwidget3.setHorizontalHeaderLabels([r"I_0", "τ", "Γ", "D", "R2","RS"])
        elif(item=="指数拟合"):
            self.listwidget3.setColumnCount(len(paras[0]) - 2)
            self.listwidget3.setHorizontalHeaderLabels([r"I_0", "τ", "D", "R^2","RS"])
        elif (item == "双曲线积分形式拟合"):
            self.listwidget3.setColumnCount(len(paras[0]) - 3)
            self.listwidget3.setHorizontalHeaderLabels([r"I_0", "τ", "Γ", "D", "R^2","RS"])
        elif (item == "指数积分形式拟合"):
            self.listwidget3.setColumnCount(len(paras[0]) - 2)
            self.listwidget3.setHorizontalHeaderLabels([r"I_0", "τ", "D", "R^2","RS"])
        if(item=="双曲线拟合"or item == "双曲线积分形式拟合"):
            for i in range(len(paras)):
                self.listwidget3.setItem(i, 0, QTableWidgetItem(str(paras[i][0])))
                self.listwidget3.setItem(i, 1, QTableWidgetItem(str(paras[i][2])))
                self.listwidget3.setItem(i, 2, QTableWidgetItem(str(paras[i][3])))
                self.listwidget3.setItem(i, 3, QTableWidgetItem(str(paras[i][4])))
                self.listwidget3.setItem(i, 4, QTableWidgetItem(str(paras[i][5])))
                self.listwidget3.setItem(i, 5, QTableWidgetItem(str(paras[i][6])))
        else:
            for i in range(len(paras)):
                for j in range(len(paras[0])-2):
                    print(paras[i][j])
                    self.listwidget3.setItem(i,j,QTableWidgetItem(str(paras[i][j])))
        self.statusBar().showMessage("请选择要更换的参数组合!")

    def listwidget3_clicked(self):
        fittype=QListWidgetItem(self.listwidget2.currentItem()).text()
        filename=QListWidgetItem(self.listwidget1.currentItem()).text()
        index=self.listwidget3.currentRow()
        find=self.tableWidget.findItems(filename,QtCore.Qt.MatchExactly)
        self.datalist[filename].plotinf[fittype].paranum = index
        if(self.singleplot==0):
            #多文件
            if find:
                #存在
                if (fittype == "双曲线拟合"):
                    self.tableWidget.setItem(find[0].row(), 1, QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(find[0].row(), 1).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(find[0].row(), 1).setBackground(QBrush(QColor(255, 255, 255)))
                if (fittype == "指数拟合"):
                    self.tableWidget.setItem(find[0].row(), 2, QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(find[0].row(), 2).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(find[0].row(), 2).setBackground(QBrush(QColor(255, 255, 255)))
                if (fittype == "双曲线积分形式拟合"):
                    self.tableWidget.setItem(find[0].row(), 3, QTableWidgetItem(str(index+1)))
                    if(index!=0):
                        self.tableWidget.item(find[0].row(), 3).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(find[0].row(), 3).setBackground(QBrush(QColor(255, 255, 255)))
                if (fittype == "指数积分形式拟合"):
                    self.tableWidget.setItem(find[0].row(), 4, QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(find[0].row(), 4).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(find[0].row(), 4).setBackground(QBrush(QColor(255, 255, 255)))
                self.plot(fittype)
                print("多文件 存在",self.selectfilename)
            else:  #不存在
                # self.selectfilename.append(filename)
                self.tableWidget.insertRow(self.tableWidget.rowCount()) #增加table行
                self.tableWidget.setItem(self.tableWidget.rowCount()-1,0,QTableWidgetItem(str(filename)))   #加入新行的0列

                # 加入1列
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(self.datalist[filename].plotinf["双曲线拟合"].paranum+1)))
                #是否为0组参数 否则高亮
                if(self.datalist[filename].plotinf["双曲线拟合"].paranum!=0):
                    self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setBackground(QBrush(QColor(240, 125, 80)))

                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2,QTableWidgetItem(str(self.datalist[filename].plotinf["指数拟合"].paranum+1)))
                if (self.datalist[filename].plotinf["指数拟合"].paranum != 0):
                    self.tableWidget.item(self.tableWidget.rowCount() - 1, 2).setBackground(QBrush(QColor(240, 125, 80)))

                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3,QTableWidgetItem(str(self.datalist[filename].plotinf["双曲线积分形式拟合"].paranum+1)))
                if (self.datalist[filename].plotinf["双曲线积分形式拟合"].paranum != 0):
                    self.tableWidget.item(self.tableWidget.rowCount() - 1, 3).setBackground(QBrush(QColor(240, 125, 80)))

                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4,QTableWidgetItem(str(self.datalist[filename].plotinf["指数积分形式拟合"].paranum+1)))
                if (self.datalist[filename].plotinf["指数积分形式拟合"].paranum != 0):
                    self.tableWidget.item(self.tableWidget.rowCount() - 1, 4).setBackground(QBrush(QColor(240, 125, 80)))

                #更改选中函数参数序号
                if(fittype=="双曲线拟合"):
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1,1,QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setBackground(QBrush(QColor(255, 255, 255)))
                if (fittype=="指数拟合"):
                    self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 2).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 2).setBackground(QBrush(QColor(255, 255, 255)))
                if (fittype=="双曲线积分形式拟合"):
                    self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 3).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 3).setBackground(QBrush(QColor(255, 255, 255)))
                if (fittype=="指数积分形式拟合"):
                    self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4, QTableWidgetItem(str(index+1)))
                    if (index != 0):
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 4).setBackground(QBrush(QColor(240, 125, 80)))
                    else:
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 4).setBackground(QBrush(QColor(255, 255, 255)))
                print("多文件 不存在", self.selectfilename)
            if(filename not in self.selectfilename):
                self.selectfilename.append(filename)
            self.datalist[filename].calculatefit(fittype)
            self.plotall()
        else:
            # self.selectfileComboBox.clear()
            # self.selectfileComboBox.addItem(filename)
            if (fittype == "双曲线拟合"):
                self.tableWidget.setItem(find[0].row(), 1, QTableWidgetItem(str(index + 1)))
                if (index != 0):
                    self.tableWidget.item(find[0].row(), 1).setBackground(QBrush(QColor(240, 125, 80)))
                else:
                    self.tableWidget.item(find[0].row(), 1).setBackground(QBrush(QColor(255, 255, 255)))
            if (fittype == "指数拟合"):
                self.tableWidget.setItem(find[0].row(), 2, QTableWidgetItem(str(index + 1)))
                if (index != 0):
                    self.tableWidget.item(find[0].row(), 2).setBackground(QBrush(QColor(240, 125, 80)))
                else:
                    self.tableWidget.item(find[0].row(), 2).setBackground(QBrush(QColor(255, 255, 255)))
            if (fittype == "双曲线积分形式拟合"):
                self.tableWidget.setItem(find[0].row(), 3, QTableWidgetItem(str(index + 1)))
                if (index != 0):
                    self.tableWidget.item(find[0].row(), 3).setBackground(QBrush(QColor(240, 125, 80)))
                else:
                    self.tableWidget.item(find[0].row(), 3).setBackground(QBrush(QColor(255, 255, 255)))
            if (fittype == "指数积分形式拟合"):
                self.tableWidget.setItem(find[0].row(), 4, QTableWidgetItem(str(index + 1)))
                if (index != 0):
                    self.tableWidget.item(find[0].row(), 4).setBackground(QBrush(QColor(240, 125, 80)))
                else:
                    self.tableWidget.item(find[0].row(), 4).setBackground(QBrush(QColor(255, 255, 255)))


            self.datalist[filename].calculatefit(fittype)
            self.plot(fittype)



        self.statusBar().showMessage('已将"'+filename+'"文件的'+fittype+"参数更改为第"+str(index+1)+"组")


    def generateMenu1(self, pos):
        row_num = -1
        for i in self.listWidget.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction(u"选项一")
            item2 = menu.addAction(u"选项二")
            item3 = menu.addAction(u"选项三")
            action = menu.exec_(self.tableWidget1.mapToGlobal(pos))
            if action == item1:
                print('您选了选项一，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())

            elif action == item2:
                print('您选了选项二，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())

            elif action == item3:
                print('您选了选项三，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
            else:
                return

    def generateMenu4(self, pos):
        # rint( pos)
        row_num = -1
        for i in self.listwidget3.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction(u"选项一")
            item2 = menu.addAction(u"选项二")
            item3 = menu.addAction(u"选项三")
            action = menu.exec_(self.listwidget3.mapToGlobal(pos))
            if action == item1:
                print('您选了选项一，当前行文字内容是：')

            elif action == item2:
                print('您选了选项二，当前行文字内容是：')

            elif action == item3:
                print('您选了选项三，当前行文字内容是：')
            else:
                return

    def generateMenu3(self, pos):
        row_num = -1
        fittype=QListWidgetItem(self.listwidget2.currentItem()).text()
        filename=QListWidgetItem(self.listwidget1.currentItem()).text()
        rowlabel=str(self.listwidget3.currentIndex().row()+1)
        collabel=str(self.listwidget3.horizontalHeaderItem(self.listwidget3.currentIndex().column()).text())
        # collabel=self.listwidget3.takeHorizontalHeaderItem(self.listwidget3.currentIndex().column()).text()
        currtext=self.listwidget3.currentItem().text()

        for i in self.listwidget3.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num < self.listwidget3.rowCount():
            menu = QMenu()
            # item1 = menu.addAction("复制单元格["+rowlabel+","+collabel+"]"+currtext)
            item1 = menu.addAction("复制单元格["+rowlabel+","+collabel+"]->"+currtext)
            item2 = menu.addAction("复制第"+rowlabel+"组参数")
            item3 = menu.addAction("提取每组参数中的"+collabel)
            action = menu.exec_(self.listwidget3.mapToGlobal(pos))
            if action == item1:
                clipboard = QApplication.clipboard()
                clipboard.setText(self.listwidget3.currentItem().text())
                self.statusBar().showMessage('已复制："'+currtext+'" （'+filename+"文件-"+fittype+"-第"+rowlabel+"组参数-"+collabel+"）")
            elif action == item2:
                clipboard = QApplication.clipboard()
                text=""
                ind=self.listwidget3.currentIndex().row()
                for j in range(self.listwidget3.columnCount()):
                    text+=self.listwidget3.item(ind,j).text()+","
                clipboard.setText(text)
                self.statusBar().showMessage('已复制:"'+text+'" （'+filename+"文件-第"+rowlabel+"组参数）")

            elif action == item3:
                clipboard = QApplication.clipboard()
                text = ""
                ind = self.listwidget3.currentIndex().column()
                for i in range(self.listwidget3.rowCount()):
                    text += self.listwidget3.item(i, ind).text() + ","
                clipboard.setText(text)
                self.statusBar().showMessage("已复制:"+text+" （已提取每组参数中的"+collabel+"）")
            else:
                return
    # def generateMenu4(self, pos):
    #     # rint( pos)
    #     row_num = -1
    #     for i in self.tableWidget.selectionModel().selection().indexes():
    #         row_num = i.row()
    #
    #     if row_num < 2:
    #         menu = QMenu()
    #         item1 = menu.addAction(u"选项一")
    #         item2 = menu.addAction(u"选项二")
    #         item3 = menu.addAction(u"选项三")
    #         action = menu.exec_(self.tableWidget.mapToGlobal(pos))
    #         if action == item1:
    #             print('您选了选项一，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
    #                   self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
    #
    #         elif action == item2:
    #             print('您选了选项二，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
    #                   self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
    #
    #         elif action == item3:
    #             print('您选了选项三，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
    #                   self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
    #         else:
    #             return

    def ChangedsingleComboBox(self):
        if(self.singleComboBox.currentText()=="单文件分析"):
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.deleteselectfileButton.blockSignals(True)
            self.clearfileButton.blockSignals(True)
            self.selectfilename.clear()
            self.singleplot = 1
            self.statusBar().showMessage("正在清空画板")
            i=1
            for key in self.figure:
                self.progressBar.setValue(int(i/len(self.figure)*100))
                try:
                    self.figure[key].fig.canvas.draw_idle()
                    self.figure[key].axes.clear()
                    self.figureson[key].figure.fig.canvas.draw_idle()
                    self.figureson[key].figure.axes.clear()
                except Exception as a:
                    print("异常")
                    print(a)
                i=i+1
            self.statusBar().showMessage("已进入单文件分析模式")
        else:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.deleteselectfileButton.blockSignals(False)
            self.clearfileButton.blockSignals(False)
            self.singleplot = 0
            self.selectfilename.clear()
            self.statusBar().showMessage("正在清空画板")
            i=1
            for key in self.figure:
                self.progressBar.setValue(int(i / len(self.figure) * 100))
                self.figure[key].fig.canvas.draw_idle()
                self.figure[key].axes.clear()
                self.figureson[key].figure.fig.canvas.draw_idle()
                self.figureson[key].figure.axes.clear()
                i=i+1
            self.statusBar().showMessage("已进入多文件分析模式")
        # if (self.listwidget1.count()!= 0):
        #     self.plotall()




    def ChangeddatatypeComboBox(self):
        if(self.datatypeComboBox.currentText()=="原数据+拟合数据"):
            self.datatype = 3
        elif(self.datatypeComboBox.currentText()=="只显示原数据"):
            self.datatype = 1
        elif(self.datatypeComboBox.currentText()=="只显示拟合数据"):
            self.datatype = 2
        if(self.listwidget1.count()!=0):
            self.plotall()

        if(self.datatypeComboBox.currentText()=="原数据+拟合数据"):
            self.statusBar().showMessage("图片已更新为：原数据+拟合数据")
        elif(self.datatypeComboBox.currentText()=="只显示原数据"):
            self.statusBar().showMessage("图片已更新为：只显示原数据")
        elif(self.datatypeComboBox.currentText()=="只显示拟合数据"):
            self.statusBar().showMessage("图片已更新为：只显示拟合数据")

    def changetableWidget(self):
        fittype=QListWidgetItem(self.listwidget2.currentItem()).text()
        filename=QListWidgetItem(self.listwidget1.currentItem()).text()
        rowlabel=str(self.listwidget3.currentIndex().row()+1)
        collabel=str(self.listwidget3.horizontalHeaderItem(self.listwidget3.currentIndex().column()))
        try:
            self.selectfileComboBox["双曲线拟合"].clear()
            self.selectfileComboBox["双曲线积分形式拟合"].clear()
            self.selectfileComboBox["指数拟合"].clear()
            self.selectfileComboBox["指数积分形式拟合"].clear()
        except Exception as a:
            print("clear:")
            print(a)
        for row in range(self.tableWidget.rowCount()):
            # try:

            print(self.tableWidget.item(row, 0).text())
            if(self.datalist[self.tableWidget.item(row,0).text()].plotinf["双曲线拟合"].fun==1):
                try:
                    print(self.selectfileComboBox["双曲线拟合"].count())
                    # self.selectfileComboBox["双曲线拟合"].addItem("vdsvsdvdsvsdvcs")
                    print(self.tableWidget.item(row,0).text())
                    self.selectfileComboBox["双曲线拟合"].addItem(self.tableWidget.item(row,0).text())
                except Exception as a:
                    print("ad:")
                    print(a)
            if(self.datalist[self.tableWidget.item(row,0).text()].plotinf["指数拟合"].fun==1):
                # self.selectfileComboBox["指数拟合"].addItem("vdsvsdvdsvsdvcs")
                try:
                    self.selectfileComboBox["指数拟合"].addItem(self.tableWidget.item(row,0).text())
                except Exception as a:
                    print("ad:")
                    print(a)
            if(self.datalist[self.tableWidget.item(row,0).text()].plotinf["双曲线积分形式拟合"].fun==1):
                self.selectfileComboBox["双曲线积分形式拟合"].addItem(self.tableWidget.item(row,0).text())
            if(self.datalist[self.tableWidget.item(row,0).text()].plotinf["指数积分形式拟合"].fun==1) :
                self.selectfileComboBox["指数积分形式拟合"].addItem(self.tableWidget.item(row,0).text())









                # if((self.tableWidget.item(row,1))and(self.tableWidget.item(row,1).text()!="-") ):
                # # if(self.tableWidget.item(row,1).text()!="-"):
                #     self.selectfileComboBox["双曲线拟合"].addItem(self.tableWidget.item(row,0).text())
                # if((self.tableWidget.item(row,1))and( self.tableWidget.item(row,2).text()!="-") ):
                # # if(self.tableWidget.item(row,2).text()!="-"):
                #     self.selectfileComboBox["指数拟合"].addItem(self.tableWidget.item(row,0).text())
                # if((self.tableWidget.item(row,1) )and( self.tableWidget.item(row,3).text()!="-") ):
                # # if(self.tableWidget.item(row,3).text()!="-"):
                #     self.selectfileComboBox["双曲线积分形式拟合"].addItem(self.tableWidget.item(row,0).text())
                # if((self.tableWidget.item(row,1) )and( self.tableWidget.item(row,4).text()!="-")) :
                # # if(self.tableWidget.item(row,4).text()!="-"):
                #     self.selectfileComboBox["指数积分形式拟合"].addItem(self.tableWidget.item(row,0).text())
            # except Exception as a:
            #     print("ad:")
            #     print(a)

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    def clearfile(self):###添加清空功能
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.selectfilename=[]

        for box in self.selectfileComboBox:
            self.selectfileComboBox[box].clear()
        self.statusBar().showMessage("已移除所有对比文件！")

    def deletefile(self):###添加删除功能
        row_select = self.tableWidget.selectedItems()
        print("类型：",type(row_select))
        if len(row_select) == 0:
            return
        # id = row_select[0].text()
        # print("id: {}".format(id))
        # for i in range(int(len(row_select)/self.tableWidget.columnCount()+1)):
        #     print("row:",row_select[i*5].row)
        filename=row_select[0].text()

        for box in self.selectfileComboBox:
            index=self.selectfileComboBox[box].findText(filename)
            if(index!=-1):
                self.selectfileComboBox[box].removeItem(index)
        self.tableWidget.removeRow(row_select[0].row())
        self.selectfilename.remove(filename)
        self.plotall()
        self.statusBar().showMessage("已移除对比文件："+filename)
        print(self.selectfilename)

    def FileRead(self,FilesPath):
        fileList=[]
        files = os.listdir(FilesPath)
        for f in files:
            if (os.path.isfile(FilesPath + '/' + f)):
                fileList.append(f)  #所有文件名
        return fileList

    def DataRead(self,Filepath):
        dataarray=[]
        data=open(Filepath)
        datalines=data.read().splitlines()
        return datalines

    def plot(self,funtype):
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)
        self.figure[funtype].fig.canvas.draw_idle()
        self.figure[funtype].axes.clear()
        self.figureson[funtype].figure.fig.canvas.draw_idle()
        self.figureson[funtype].figure.axes.clear()
        self.progressBar.setValue(0)
        if(self.singleplot==1):
            if (self.datalist[self.singlefilename].plotinf[funtype].fun == 1):
                plotObject = self.datalist[self.singlefilename].plotinf[funtype]
                xdata = plotObject.xdata
                ydata = plotObject.ydata
                xfit = plotObject.xfit
                yfit = plotObject.yfit
                spotwidth = plotObject.spotwidth
                spotcolor = plotObject.spotcolor
                linewidth = plotObject.linewidth
                linecolor = plotObject.linecolor
                spotalpha = plotObject.spotalpha
                orlabel = plotObject.orlabel
                fitlabel = plotObject.fitlabel+"参数("+str(plotObject.paranum+1)+")"
                dt = self.datalist[self.singlefilename].dt
                if ((funtype == "双曲线积分形式拟合") or (funtype == "指数积分形式拟合")):
                    if((self.datatype==3) or (self.datatype==1)):
                        self.figure[funtype].axes.bar(xdata, ydata, width=dt, color=spotcolor, alpha=spotalpha,label=orlabel)
                        self.figureson[funtype].figure.axes.bar(xdata, ydata, width=dt, color=spotcolor,alpha=spotalpha,label=orlabel)
                    self.progressBar.setValue(40)
                    if((self.datatype==3) or (self.datatype==2)):
                        self.figure[funtype].axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)
                        self.figureson[funtype].figure.axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)

                elif ((funtype == "双曲线拟合") or (funtype == "指数拟合")):
                    if ((self.datatype == 3) or (self.datatype == 1)):
                        self.figure[funtype].axes.scatter(xdata, ydata, s=spotwidth, c=spotcolor, alpha=spotalpha,label=orlabel)
                        self.figureson[funtype].figure.axes.scatter(xdata, ydata, s=spotwidth, c=spotcolor,alpha=spotalpha,label=orlabel)
                        self.progressBar.setValue(40)


                    if ((self.datatype == 3) or (self.datatype == 2)):
                        self.figure[funtype].axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)
                        self.figureson[funtype].figure.axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)

                self.progressBar.setValue(80)

        elif(self.singleplot==0):
            i = 1
            for file in self.selectfilename:
                if (self.datalist[file].plotinf[funtype].fun == 1):
                    plotObject = self.datalist[file].plotinf[funtype]
                    xdata = plotObject.xdata
                    ydata = plotObject.ydata
                    xfit = plotObject.xfit
                    yfit = plotObject.yfit
                    spotwidth = plotObject.spotwidth
                    # spotcolor = plotObject.spotcolor
                    # print((i-1)%len(self.colorlis))
                    plotObject.spotcolor=self.colorlist[i-1]
                    spotcolor = plotObject.spotcolor
                    print(spotcolor)
                    linewidth = plotObject.linewidth
                    # linecolor = plotObject.linecolor
                    plotObject.linecolor = self.colorlist[i-1]
                    linecolor=plotObject.linecolor

                    spotalpha = plotObject.spotalpha
                    orlabel = plotObject.orlabel
                    fitlabel = plotObject.fitlabel+"，参数("+str(plotObject.paranum+1)+")"
                    dt=self.datalist[file].dt
                    if ((funtype == "双曲线积分形式拟合") or (funtype == "指数积分形式拟合")):
                        try:
                            if (self.datatype == 3 or self.datatype == 1):
                                self.figure[funtype].axes.bar(xdata, ydata, width=dt,color=spotcolor, alpha=spotalpha,label=orlabel)
                                self.figureson[funtype].figure.axes.bar(xdata, ydata, width=dt, color=spotcolor,alpha=spotalpha,label=orlabel)
                            self.progressBar.setValue(int((i + 0.5) / len(self.selectfilename) * 80))
                            if (self.datatype == 3 or self.datatype == 2):
                                self.figure[funtype].axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)
                                self.figureson[funtype].figure.axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)
                        except Exception as a:
                            print("异常")
                            print(a)
                    elif((funtype == "双曲线拟合") or (funtype == "指数拟合")):
                        try:
                            if (self.datatype == 3 or self.datatype == 1):
                                self.figure[funtype].axes.scatter(xdata, ydata, s=spotwidth, c=spotcolor, alpha=spotalpha,label=orlabel)
                                self.figureson[funtype].figure.axes.scatter(xdata, ydata, s=spotwidth, c=spotcolor,alpha=spotalpha,label=orlabel)
                            self.progressBar.setValue(int((i+0.5) / len(self.selectfilename) *80))
                            if (self.datatype == 3 or self.datatype == 2):
                                self.figure[funtype].axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)
                                self.figureson[funtype].figure.axes.plot(xfit, yfit, markersize=linewidth, color=linecolor,label=fitlabel)
                        except Exception as a:
                            print("异常2")
                            print(a)
                self.progressBar.setValue(int(i / len(self.selectfilename)*80))
                i += 1
        self.statusBar().showMessage("正在加载坐标轴标题...")
        self.figure[funtype].axes.set_ylabel(self.figureinf[funtype].ylabel)
        self.figure[funtype].axes.set_xlabel(self.figureinf[funtype].xlabel)
        if(self.figureinf[funtype].temptitle==""):
            self.figure[funtype].axes.set_title(self.figureinf[funtype].title)
        else:
            self.figure[funtype].axes.set_title(self.figureinf[funtype].temptitle)
        self.figure[funtype].axes.legend()

        self.figureson[funtype].figure.axes.set_ylabel(self.figureinf[funtype].ylabel)
        self.figureson[funtype].figure.axes.set_xlabel(self.figureinf[funtype].xlabel)
        self.figureson[funtype].figure.axes.set_title(self.figureinf[funtype].title)
        self.figureson[funtype].figure.axes.legend()
        self.progressBar.setValue(100)
        self.progressBar.setVisible(False)

    def plotall(self):
        # if (self.singleplot==1):

        self.statusBar().showMessage("正在绘图1/4")
        self.plot("双曲线拟合")
        # self.progressBar.setValue(62)
        self.statusBar().showMessage("正在绘图2/4")
        self.plot("指数拟合")
        # self.progressBar.setValue(75)
        self.statusBar().showMessage("正在绘图3/4")
        self.plot("指数积分形式拟合")
        # self.progressBar.setValue(87)
        self.statusBar().showMessage("正在绘图4/4")
        self.plot("双曲线积分形式拟合")
        self.statusBar().showMessage("图片加载成功！")




