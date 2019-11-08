from MainUI import*
from SonFig import*
import Mydemo
import DataClass
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class main(QMainWindow):
    def __init__(self,parent=None):
        super(main, self).__init__(parent)

        self.datalist=[]

        self.tabWidget = QTabWidget()
        self.setFont(QFont("Microsoft YaHei", 10.5))
        self.setWindowTitle('人体延迟发光数据画图软件 V1.0')
        self.setWindowIcon(QIcon('xyjk.png'))
        self.openfile_path = ""
        self.tab1=MainUI(self.statusBar(),self.datalist)
        self.tab2=SonFig(4,self.statusBar(),self.datalist)
        self.tab3=SonFig(2,self.statusBar(),self.datalist)
        self.tab4=SonFig(6,self.statusBar(),self.datalist)
        self.tab5=SonFig(5,self.statusBar(),self.datalist)

        # 将三个选项卡添加到顶层窗口中
        self.tabWidget.addTab(self.tab1, "主界面")
        self.tabWidget.addTab(self.tab2, "双曲线图片编辑")
        self.tabWidget.addTab(self.tab3, "指数图片编辑")
        self.tabWidget.addTab(self.tab4, "双曲积分图片编辑")
        self.tabWidget.addTab(self.tab5, "指数积分图片编辑")
        self.setCentralWidget(self.tabWidget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main()
    ui.show()
    sys.exit(app.exec_())