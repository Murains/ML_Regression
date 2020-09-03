import numpy as np
import operator
from ICCStandard.ICCStandard import IModel
from numpy import mat
from numpy.linalg import linalg
from sklearn.linear_model import LinearRegression
import time
import datetime as dt

class Model(IModel):
    def __init__(self):
        self.load_model()
    
    '''
    加载外部模型主体, 完成模型配置
    '''
    def load_model(self):
        self.model = self.knn
    
    '''
    获取最终模型主体
    '''
    def get_model(self):
        return self.model
    
    @staticmethod
    def knn(x_train, y_train):
        # print(x_train.dtype, y_train.dtype)
        y_train = y_train.astype(np.float64)
        print(x_train.dtype, y_train.dtype)
        xMat = mat(x_train)
        yMat = mat(y_train).T
        starTime1 = dt.datetime.now()
        xTx = xMat.T * xMat
        if linalg.det(xTx) == 0:
            print('This matrix is singular, cannot do inverse')
            return
        ws = xTx.I * (xMat.T * yMat)
        endTime1 = dt.datetime.now()
        print('mytime:', (endTime1 - starTime1).microseconds)
        starTime2 = dt.datetime.now()
        linreg = LinearRegression()
        linreg.fit(x_train,y_train)
        endTime2 = dt.datetime.now()
        print('sklearntime:', (endTime2 - starTime2).microseconds)
        return ws