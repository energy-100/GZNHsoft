from MainUI import*
from SonFig import SonFigspot,SonFigbar
from Mydemo import*
import DataClass
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class FigureClass():
    def __init__(self,title, parent=None):
        self.title=title
        self.titlecolor="black"
        self.xaxis=""
        self.yaxis=""
        self.xlabel="t"
        self.ylabel='cps'
        self.xlabelcolor="black"
        self.ylabelcolor="black"

class main(QMainWindow):
    def __init__(self,parent=None):
        super(main, self).__init__(parent)
        self.singleplot=0
        self.singlefilename=""
        self.selectfilename = []        #文件选择列表
        self.select=dict()      #子图列表
        self.select["双曲线拟合"]=QComboBox()
        self.select["指数拟合"]=QComboBox()
        self.select["双曲线积分形式拟合"]=QComboBox()
        self.select["指数积分形式拟合"]=QComboBox()
        self.progressBar = QProgressBar()
        self.statusBar().addPermanentWidget(self.progressBar)
        self.progressBar.setVisible(False)
        self.tabWidget = QTabWidget()
        self.setFont(QFont("Microsoft YaHei", 12))
        self.setWindowTitle('人体延迟发光数据画图软件 V2.0')
        self.setWindowIcon(QIcon('xyjk.png'))
        self.openfile_path = ""

        # 主图 Figure
        self.figuremain=dict()
        self.figuremain["双曲线拟合"]=Mydemo(width=5, height=3, dpi=100)
        self.figuremain["指数拟合"]=Mydemo(width=5, height=3, dpi=100)
        self.figuremain["双曲线积分形式拟合"]=Mydemo(width=5, height=3, dpi=100)
        self.figuremain["指数积分形式拟合"]=Mydemo(width=5, height=3, dpi=100)

        # 图片信息
        self.figureinf=dict()
        self.figureinf["双曲线拟合"]=FigureClass('双曲线拟合(${I}$ = ${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)')
        self.figureinf["指数拟合"]=FigureClass('指数拟合(${I}$ = ${I_0}$e${^{-t/\\tau}}$+D)')
        self.figureinf["双曲线积分形式拟合"]=FigureClass('双曲线积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)dt)')
        self.figureinf["指数积分形式拟合"]=FigureClass('指数积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$e${^{-t/\\tau}}$+D)dt)')

        #子图 Figure&Tab
        self.datalist=dict()
        self.figureson=dict()
        self.figureson["双曲线拟合"] = SonFigspot("双曲线拟合",self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureinf["双曲线拟合"],self.select["双曲线拟合"])
        self.figureson["指数拟合"] = SonFigspot("指数拟合",self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureinf["指数拟合"],self.select["指数拟合"])
        self.figureson["双曲线积分形式拟合"] = SonFigbar("双曲线积分形式拟合",self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureinf["双曲线积分形式拟合"],self.select["双曲线积分形式拟合"])
        self.figureson["指数积分形式拟合"] = SonFigbar("指数积分形式拟合",self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureinf["指数积分形式拟合"],self.select["指数积分形式拟合"])


        #主图tab
        self.tab1=MainUI(self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureson,self.figureinf,self.select)
        # self.tab2=SonFig(4,self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureson)
        # self.tab3=SonFig(2,self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureson)
        # self.tab4=SonFig(6,self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureson)
        # self.tab5=SonFig(5,self.statusBar,self.progressBar,self.datalist,self.selectfilename,self.figuremain,self.figureson)

        # 将三个选项卡添加到顶层窗口中
        self.tabWidget.addTab(self.tab1, "主界面")
        self.tabWidget.addTab(self.figureson["双曲线拟合"], "双曲线图片编辑")
        self.tabWidget.addTab(self.figureson["指数拟合"], "指数图片编辑")
        self.tabWidget.addTab(self.figureson["双曲线积分形式拟合"], "双曲积分图片编辑")
        self.tabWidget.addTab(self.figureson["指数积分形式拟合"], "指数积分图片编辑")
        self.setCentralWidget(self.tabWidget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main()
    ui.show()
    sys.exit(app.exec_())