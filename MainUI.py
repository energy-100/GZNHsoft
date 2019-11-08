from PyQt5.QtGui import *
from Mydemo import *
from PyQt5.QtWidgets import *
import os
class MainUI(QWidget):
    def __init__(self,statusBar,datalist,parent=None):
        super(MainUI, self).__init__(parent)
        self.statusBar = statusBar
        self.datalist=datalist
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.figure1 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure1, 1, 0, 1, 15)

        self.figure2 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure2, 1, 15, 1, 15)

        self.figure3 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure3, 2, 0, 1, 15)

        self.figure4 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure4, 2, 15, 1, 15)

        self.label_1 = QLabel("数据文件列表：")
        self.grid.addWidget(self.label_1, 3, 0, 1, 10)
        self.label_2 = QLabel("可拟合的函数类型：")
        self.grid.addWidget(self.label_2, 3, 10, 1, 10)
        self.label_4 = QLabel("选中列表：")
        self.grid.addWidget(self.label_4, 3, 20, 1, 10)

        self.listwidget1 = QListWidget(self)
        self.grid.addWidget(self.listwidget1, 4, 0, 6, 10)
        self.listwidget1.clicked.connect(lambda: self.listwidget1_clicked())

        self.listwidget2 = QListWidget(self)
        self.grid.addWidget(self.listwidget2, 4, 10, 3, 10)
        self.listwidget2.clicked.connect(lambda: self.listwidget2_clicked())

        self.label_3 = QLabel("参数列表：")
        self.grid.addWidget(self.label_3, 7, 10, 1, 10)

        self.listwidget3 = QListWidget(self)
        self.grid.addWidget(self.listwidget3, 8, 10, 3, 10)
        self.listwidget3.clicked.connect(lambda: self.listwidget3_clicked())

        # self.listwidget4 = QListWidget(self)
        # self.grid.addWidget(self.listwidget4, 4, 20, 6, 10)
        # # self.listwidget4.clicked.connect(lambda: self.listwidget4_clicked())

        self.tableWidget = QTableWidget(3,5)
        self.tableWidget.setHorizontalHeaderLabels(['文件名称', '双曲线拟合', '指数拟合','双曲线积分拟合', '指数积分拟合'])
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.grid.addWidget(self.tableWidget, 4, 20, 6, 10)



        self.loadfileButton = QPushButton("添加文件夹", self)
        # self.loadfileButton.clicked.connect(lambda:self.openfile)
        self.grid.addWidget(self.loadfileButton, 10, 0, 1, 1)

        self.loadsinglefileButton = QPushButton("添加文件", self)
        # self.loadsinglefileButton.clicked.connect(lambda:self.opensinglefile)
        self.grid.addWidget(self.loadsinglefileButton, 10, 1, 1, 1)

        self.deleteselectfileButton = QPushButton("删除对比文件", self)
        # self.deleteselectfileButton.clicked.connect(lambda:self.deleteselectfile)
        self.grid.addWidget(self.deleteselectfileButton, 10, 20, 1, 1)

        self.clearfileButton = QPushButton("清空对比文件", self)
        # self.clearfileButton.clicked.connect(lambda:self.clearfile)
        self.grid.addWidget(self.clearfileButton, 10, 21, 1, 1)

        self.setLayout(self.grid)

    def SaveImage(self):

        filename1 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        filename2 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        filename3 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        filename4 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        # print("保存位置",self.openfile_path+"/"+filename1+"双曲线拟合图"+".jpg")
        self.figure1.axes.get_figure().savefig(self.openfile_path+"/"+filename1+"双曲线拟合图"+".png")


        self.figure2.axes.get_figure().savefig(self.openfile_path+"/"+filename2+"指数拟合图"+".png")
        self.figure3.axes.get_figure().savefig(self.openfile_path+"/"+filename3+"双曲线积分拟合图"+".png")
        self.figure4.axes.get_figure().savefig(self.openfile_path+"/"+filename4+"指数积分拟合图"+".png")

    def openfile(self):
        self.statusBar().showMessage("正在选择图片...")
        path= QFileDialog.getExistingDirectory(self, "请选择数据文件的根目录")
        if(path!=""):
            self.label_1.setText('"'+path+'"路径下的数据文件：')
            self.openfile_path=path
            files=self.FileRead(self.openfile_path+ "/处理后的原始数据")
            self.listwidget1.clear()
            self.listwidget1.addItems(files)
            self.statusBar().showMessage("文件目录："+str(self.openfile_path))
            self.tab2.filepath=self.openfile_path
            self.tab3.filepath=self.openfile_path
            self.tab4.filepath=self.openfile_path
            self.tab5.filepath=self.openfile_path

            self.tab2.filename=self.openfile_path
            self.tab3.filename=self.openfile_path
            self.tab4.filename=self.openfile_path
            self.tab5.filename=self.openfile_path
            self.statusBar().showMessage("请选择一组数据文件，默认使用第一组参数进行拟合。")
        elif(self.openfile_path!=""):
            self.statusBar().showMessage("未更新数据文件！")
        else:
            self.statusBar().showMessage("请点击'Load File'按钮选择文数据目录...")



    # def fitting(self):
    #     self.filenme=QListWidgetItem(self.listwidget1.currentItem()).text()
    #     self.paratext=QListWidgetItem(self.listwidget2.currentItem()).text()
    #     print(self.openfile_path + "/../处理后的原始数据/"+self.filenme)
    #     aaa=self.DataRead(self.openfile_path + "/../处理后的原始数据/"+self.filenme)
    #     self.ordata=np.loadtxt(self.openfile_path + "/../处理后的原始数据/"+self.filenme)
    #     self.ordata=self.ordata.astype(np.float64)
    #     print(self.ordata.dtype)
    #     self.figure1.fig.canvas.draw_idle()
    #     self.figure1.axes.clear()
    #     # self.figure1.axes1.clear()
    #     self.figure1.axes.plot(self.ordata[:, 0], self.ordata[:, 1])
    #     # self.figure1.axes1.plot(self.ordata[:, 0], self.ordata[:, 1])
    #     self.figure1.axes.set_ylabel('cps')
    #     self.figure1.axes.set_title('实验数据', color='black')



    def listwidget1_clicked(self):
        self.statusBar().showMessage("正在加载图片1/4")
        self.progressBar.setVisible(True)
        # self.label2.setVisible(True)
        self.progressBar.setValue(0)
        item = QListWidgetItem(self.listwidget1.currentItem()).text()
        self.label_2.setText("("+item+"）文件可拟合的数据类型：")
        self.ordata=np.loadtxt(self.openfile_path + "/处理后的原始数据/"+item)
        self.listwidget2.clear()
        if(os.path.exists(self.openfile_path+"\双曲线拟合\\"+item)):
            self.listwidget2.addItem("双曲线拟合")
            para=self.DataRead(self.openfile_path+"\双曲线拟合\\"+item)
            paras = [float(i) for i in para[0].split()]
            # print("进入单击")
            self.plot(paras)
            self.tab2.filename=item
            self.tab2.parasstr=paras
            # print("单击结束")
        self.progressBar.setValue(25)
        if (os.path.exists(self.openfile_path + "\指数拟合\\" + item)):
            self.statusBar().showMessage("正在加载图片2/4")
            self.listwidget2.addItem("指数拟合")
            para = self.DataRead(self.openfile_path + "\指数拟合\\" + item)
            paras = [float(i) for i in para[0].split()]
            # print("进入指数单击")
            self.plot(paras)
            self.tab3.filename = item
            self.tab3.parasstr = paras
            # print("单击结束")
        self.progressBar.setValue(50)
        if (os.path.exists(self.openfile_path + "\双曲线积分形式拟合\\" + item)):
            self.statusBar().showMessage("正在加载图片3/4")
            self.listwidget2.addItem("双曲线积分形式拟合")
            para = self.DataRead(self.openfile_path + "\双曲线积分形式拟合\\" + item)
            paras = [float(i) for i in para[0].split()]
            # print("进入双曲积分单击")
            self.plot(paras)
            self.tab4.filename = item
            self.tab4.parasstr = paras
        self.progressBar.setValue(75)
        if (os.path.exists(self.openfile_path + "\指数积分形式拟合\\" + item)):
            self.statusBar().showMessage("正在加载图片4/4")
            self.listwidget2.addItem("指数积分形式拟合")
            para = self.DataRead(self.openfile_path + "\指数积分形式拟合\\" + item)
            paras = [float(i) for i in para[0].split()]
            # print("进入指数积分单击")
            self.plot(paras)
            self.tab5.filename = item
            self.tab5.parasstr = paras
        self.progressBar.setValue(100)
        self.label2.setVisible(False)
        self.progressBar.setVisible(False)
        self.statusBar().showMessage("默认使用第一组参数进行拟合，如需更换参数组合，请先选择要修改拟合类型!")
            # print("单击结束")


    def listwidget2_clicked(self):
        item = QListWidgetItem(self.listwidget2.currentItem()).text()
        self.label_3.setText(QListWidgetItem(self.listwidget1.currentItem()).text()+"文件"+item+"下的参数列表")
        fitdata=self.DataRead(self.openfile_path+"\\"+item+"\\"+QListWidgetItem(self.listwidget1.currentItem()).text())
        # print("fitdata",fitdata)
        self.listwidget3.clear()
        self.listwidget3.addItems(fitdata)
        self.SaveImage()
        self.statusBar().showMessage("请选择要更换的参数组合!")


    def listwidget3_clicked(self):
        paras=QListWidgetItem(self.listwidget3.currentItem()).text().split()
        fittype=QListWidgetItem(self.listwidget2.currentItem()).text()
        paras = [float(i) for i in paras]
        print(type(paras))
        print(paras)
        self.plot(paras)
        print(fittype,"验证：",fittype=="双曲线拟合")
        print(fittype,"验证：",fittype=="双曲线拟合!")
        print(fittype,"验证：",fittype=="指数积分拟合")
        print(fittype,"验证：",fittype=="指数拟合")
        if(fittype=="双曲线拟合"):
            self.tab2.paranum=self.listwidget3.currentIndex()
            self.tab2.parasstr = paras
            self.tab2.parasnum=self.listwidget3.currentIndex()
            self.statusBar().showMessage("双曲线拟合图像已更新!")
        elif(fittype=="指数拟合"):
            self.tab3.paranum=self.listwidget3.currentIndex()
            self.tab3.parasstr = paras
            self.tab3.parasnum = self.listwidget3.currentIndex()
            self.statusBar().showMessage("指数拟合图像已更新!")
        elif (fittype == "双曲线积分形式拟合"):
            self.tab4.paranum = self.listwidget3.currentIndex()
            self.tab4.parasstr = paras
            self.tab4.parasnum = self.listwidget3.currentIndex()
            self.statusBar().showMessage("双曲线积分拟合图像已更新!")
        elif(fittype=="指数积分形式拟合"):
            self.tab5.paranum=self.listwidget3.currentIndex()
            self.tab5.parasstr = paras
            self.tab5.parasnum = self.listwidget3.currentIndex()
            self.statusBar().showMessage("指数积分拟合图像已更新!")
    def plot(self,para,linecolor="blue",linesize=1,spotcolor="blue",spotsize=26,baralpha=0.3):
        # print("进入plot",para)
        # print(para[-1])
        if(para[-1]==4):  #双曲线画图
            print("进入双曲线画图")
            self.figure1.fig.canvas.draw_idle()
            self.figure1.axes.clear()
            xfit = np.linspace(self.ordata[0,0],self.ordata[-1,0],1000)
            yfit = self.creatFittingata(xfit,para)
            self.figure1.axes.scatter(self.ordata[:, 0], self.ordata[:, 1], s=spotsize, c=spotcolor,alpha=baralpha)
            self.figure1.axes.plot(xfit, yfit, markersize=linesize, color=linecolor)
            self.figure1.axes.set_ylabel('cps')
            self.figure1.axes.set_xlabel('t')
            self.figure1.axes.set_title('双曲线拟合(${I}$ = ${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)', color='black')

            #子图
            self.tab2.SetPara(self.ordata[:, 0],self.ordata[:, 1],xfit,yfit)
            self.tab2.figure.fig.canvas.draw_idle()
            self.tab2.figure.axes.clear()
            self.tab2.figure.axes.scatter(self.ordata[:, 0], self.ordata[:, 1], s=spotsize, c=spotcolor,alpha=baralpha)
            self.tab2.figure.axes.plot(xfit, yfit, markersize=linesize, color=linecolor)
            self.tab2.figure.axes.set_ylabel('cps')
            self.tab2.figure.axes.set_xlabel('t')
            self.tab2.figure.axes.set_title('双曲线拟合(${I}$ = ${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)', color='black')

        elif (para[-1] == 2):  # 指数画图

            self.figure2.fig.canvas.draw_idle()
            self.figure2.axes.clear()
            xfit = np.linspace(self.ordata[0,0], self.ordata[-1,0], 1000)
            print("测试：",self.ordata[0][0],self.ordata[0][-1])
            yfit = self.creatFittingata(xfit,para)
            self.figure2.axes.scatter(self.ordata[:, 0], self.ordata[:, 1],s=spotsize, c=spotcolor,alpha=baralpha)
            self.figure2.axes.plot(xfit, yfit, markersize=linesize, color=linecolor)
            self.figure2.axes.set_ylabel('cps')
            self.figure2.axes.set_xlabel('t')
            self.figure2.axes.set_title('指数拟合(${I}$ = ${I_0}$e${^{-t/\\tau}}$+D)', color='black')
                # try:
                # except Exception as err:
                # print(err)

            # 子图
            self.tab3.SetPara(self.ordata[:, 0], self.ordata[:, 1], xfit, yfit)
            self.tab3.figure.fig.canvas.draw_idle()
            self.tab3.figure.axes.clear()

            self.tab3.figure.axes.scatter(self.ordata[:, 0], self.ordata[:, 1],s=spotsize, c=spotcolor,alpha=baralpha)
            self.tab3.figure.axes.plot(xfit, yfit,markersize=linesize, color=linecolor)

            self.tab3.figure.axes.set_ylabel('cps')
            self.tab3.figure.axes.set_xlabel('t')
            self.tab3.figure.axes.set_title('指数拟合(${I}$ = ${I_0}$e${^{-t/\\tau}}$+D)', color='black')

        elif (para[-1] == 6):  # 双曲线积分画图
            self.figure3.fig.canvas.draw_idle()
            self.figure3.axes.clear()
            dt=float(para[-2])
            xfit = np.linspace(self.ordata[0, 0], self.ordata[-1,0]+dt, 1000)
            yfit = self.creatFittingata(xfit, para)
            xbar = np.asarray(self.ordata[:, 0]) + (dt / 2)
            ybar = np.asarray(self.ordata[:, 1]) / dt
            self.figure3.axes.bar(xbar, ybar, width=dt, alpha=baralpha,color=spotcolor)
            self.figure3.axes.plot(xfit, yfit,markersize=linesize, color=linecolor)

            self.figure3.axes.set_ylabel('cps')
            self.figure3.axes.set_xlabel('t')
            self.figure3.axes.set_title('双曲线积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)dt)', color='black')

            # 子图
            self.tab4.SetPara(xbar, ybar, xfit, yfit,dt)
            self.tab4.figure.fig.canvas.draw_idle()
            self.tab4.figure.axes.clear()
            self.tab4.figure.axes.bar(xbar, ybar, width=dt, alpha=baralpha,color=spotcolor)
            self.tab4.figure.axes.plot(xfit, yfit,markersize=linesize, color=linecolor)
            self.tab4.figure.axes.set_ylabel('cps')
            self.tab4.figure.axes.set_xlabel('t')
            self.tab4.figure.axes.set_title('双曲线积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)dt)', color='black')

        elif (para[-1] == 5):  # 指数积分画图
            self.figure4.fig.canvas.draw_idle()
            self.figure4.axes.clear()
            dt = para[-2]
            xfit = np.linspace(self.ordata[0, 0], self.ordata[-1, 0] + dt, 1000)
            yfit = self.creatFittingata(xfit, para)
            xbar = np.asarray(self.ordata[:, 0]) + (dt / 2)
            ybar = np.asarray(self.ordata[:, 1]) / dt
            self.figure4.axes.bar(xbar, ybar, width=dt, alpha=baralpha,color=spotcolor)
            self.figure4.axes.plot(xfit, yfit,markersize=linesize, color=linecolor)
            self.figure4.axes.set_ylabel('cps')
            self.figure4.axes.set_xlabel('t')
            self.figure4.axes.set_title(
                '指数积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$e${^{-t/\\tau}}$+D)dt)', color='black')

            self.tab5.SetPara(xbar, ybar, xfit, yfit, dt)
            self.tab5.figure.fig.canvas.draw_idle()
            self.tab5.figure.axes.clear()
            self.tab5.figure.axes.bar(xbar, ybar, width=dt, alpha=baralpha,color=spotcolor)
            self.tab5.figure.axes.plot(xfit, yfit,markersize=linesize, color=linecolor)
            self.tab5.figure.axes.set_ylabel('cps')
            self.tab5.figure.axes.set_xlabel('t')
            self.tab5.figure.axes.set_title(
                '指数积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$e${^{-t/\\tau}}$+D)dt)', color='black')




    def creatFittingata(self,xdata,paras):
        # print(paras)
        if (paras[-1]==2 or paras[-1]==5):
            return paras[0] * (np.exp(-(xdata / paras[1]))) + paras[2]
        if (paras[-1]==4 or paras[-1]==6):
            # print(2)
            return paras[0] * ((paras[1] + (np.asarray(xdata) / paras[2])) ** (-paras[3])) + paras[4]


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