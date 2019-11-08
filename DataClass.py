class DataClass():
    def __init__(self,parent=None):
        self.change=0
        self.linecolor="blue"
        self.spotcolor="blue"
        self.linewidth=1
        self.spotwidth=26
        self.spotalpha=0.3
        self.spotalpha = 26
        #原始数据
        self.xdata1=[]
        self.xdata2=[]
        self.ydata1=[]
        self.ydata2=[]
        #拟合数据
        self.xfit=[]
        self.ydata2=[]  #指数拟合数据
        self.ydata4=[]  #双曲拟合数据
        self.ydata5=[]  #指数积分拟合数据
        self.ydata6=[]  #双曲积分拟合数据

        self.dt= 0      #derT
        self.filepath=""        #文件路径
        self.filename=""        #文件名称
        self.paranum=0          #文件参数数量
        self.parasstr2=""        #文件参数字符串
        self.parasstr4=""        #文件参数字符串
        self.parasstr5=""        #文件参数字符串
        self.parasstr6=""        #文件参数字符串
        self.title="null"
