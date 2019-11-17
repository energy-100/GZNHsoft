import numpy as np
class plot():
    def __init__(self, parent=None):
        self.fun=0
        self.linewidth=1
        self.change=0
        self.paranum="-"
        self.linecolor="blue"
        self.spotcolor="blue"
        self.linewidth=1
        self.spotwidth=26
        self.spotalpha=0.3
        self.paras=[]
        self.xdata=[]
        self.ydata=[]
        self.xfit=[]
        self.yfit=[]
        self.orlabel="原始数据"
        self.fitlabel="拟合数据"


class DataClass():
    def __init__(self,parent=None):
        self.plotinf=dict()
        self.plotinf["双曲线拟合"]=plot()
        self.plotinf["指数拟合"]=plot()
        self.plotinf["双曲线积分形式拟合"]=plot()
        self.plotinf["指数积分形式拟合"]=plot()
        self.filepath=""        #文件路径
        self.filename=""        #文件名称
        self.rootpath=""
        self.dt=0
    def select(self):
        ret=[self.filename,str(self.plotinf["双曲线拟合"].paranum),str(self.plotinf["指数拟合"].paranum),str(self.plotinf["双曲线积分形式拟合"].paranum),str(self.plotinf["指数积分形式拟合"].paranum)]
        for i in range(1,len(ret)):
            if(ret[i]!="-"):
                ret[i]=str(int(ret[i])+1)
        print(ret)
        return ret

    def Setordata(self,x,y,dt):
        self.dt=dt
        self.plotinf["双曲线拟合"].xdata=x
        self.plotinf["双曲线拟合"].xfit=np.linspace(x[0], x[-1] + dt, 1000)
        self.plotinf["双曲线拟合"].ydata=y

        self.plotinf["指数拟合"].xdata=x
        self.plotinf["指数拟合"].xfit=np.linspace(x[0], x[-1], 1000)
        self.plotinf["指数拟合"].ydata=y


        self.plotinf["双曲线积分形式拟合"].xdata=np.asarray(x) + (dt / 2)
        self.plotinf["双曲线积分形式拟合"].xfit=np.linspace(x[0], x[-1] + dt, 1000)
        self.plotinf["双曲线积分形式拟合"].ydata=np.asarray(y) / dt


        self.plotinf["指数积分形式拟合"].xdata=np.asarray(x) + (dt / 2)
        self.plotinf["指数积分形式拟合"].xfit=np.linspace(x[0], x[-1] + dt, 1000)
        self.plotinf["指数积分形式拟合"].ydata=np.asarray(y) / dt

    def calculatefit(self,funtype=""):
        if(funtype=="双曲线拟合" or funtype=="双曲线积分形式拟合"):
            paranum = self.plotinf[funtype].paranum
            x=self.plotinf[funtype].xfit
            s1 = self.plotinf[funtype].paras[paranum][0]
            s2 = self.plotinf[funtype].paras[paranum][1]
            s3 = self.plotinf[funtype].paras[paranum][2]
            s4 = self.plotinf[funtype].paras[paranum][3]
            s5 = self.plotinf[funtype].paras[paranum][4]
            self.plotinf[funtype].yfit = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
        elif (funtype == "指数拟合" or funtype == "指数积分形式拟合"):
            paranum = self.plotinf[funtype].paranum
            x = self.plotinf[funtype].xfit
            s1 = self.plotinf[funtype].paras[paranum][0]
            s2 = self.plotinf[funtype].paras[paranum][1]
            s3 = self.plotinf[funtype].paras[paranum][2]
            self.plotinf[funtype].yfit = s1 * (np.exp(-(x / s2))) + s3

        for key in self.plotinf:
            if (self.plotinf[key].fun == 1 and self.plotinf[key].yfit == []):
                paranum = self.plotinf[key].paranum
                if (key == "双曲线拟合" or key == "双曲线积分形式拟合"):
                    x = self.plotinf[key].xfit
                    s1 = self.plotinf[key].paras[paranum][0]
                    s2 = self.plotinf[key].paras[paranum][1]
                    s3 = self.plotinf[key].paras[paranum][2]
                    s4 = self.plotinf[key].paras[paranum][3]
                    s5 = self.plotinf[key].paras[paranum][4]
                    self.plotinf[key].yfit = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
                elif (key == "指数拟合" or key == "指数积分形式拟合"):
                    x = self.plotinf[key].xfit
                    s1 = self.plotinf[key].paras[paranum][0]
                    s2 = self.plotinf[key].paras[paranum][1]
                    s3 = self.plotinf[key].paras[paranum][2]
                    self.plotinf[key].yfit = s1 * (np.exp(-(x / s2))) + s3

    def setaxisLabel(self,filename):
        for key in self.plotinf:
            self.plotinf[key].orlabel=filename+"原始数据"
            self.plotinf[key].fitlabel=filename+key+"数据"


