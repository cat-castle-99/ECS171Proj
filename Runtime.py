import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler



class logModel:
    def __init__(self):
        self.seed=0 #seed for train test split. still needs to be implemented
        self.__dataSetRaw=None #raw unnormalizzed dataset
        self.__dataSet = None #nomarlized dataset
        self.__model=None # fitted model from pickles
        self.__userInput={} #users input format: dictionary
        self.__userOutput=0 #users result

    def prepare(self):
        return 0

    def readModel(self,filename):
        #read in the model
        try:
            loaded_model = pickle.load(open(filename, 'rb'))
            self.__model=loaded_model
            return 0
        except:
            print("Model Read ERROR")
            return -1

    def readDataSet(self,filename):
        #read in the dataset
        try:
            self.__dataSetRaw = pd.read_csv(filename)
            return 0
        except:
            print("Dataset Read ERROR")
            return -1

    def makePrediction(self, userinput=None):
        self.__dataSetRaw = self.__dataSetRaw.append(userinput, ignore_index=True)
        scale=MinMaxScaler()
        self.__dataSet = scale.fit_transform(self.__dataSetRaw)
        self.__userInput=self.__dataSet.iloc[-1:]
        try:
            predict = self.__model.predict([self.__userInput])
            self.__userOutput=predict
            return predict
        except:
            print("Prediction ERROR")
            return -1

    def generateGraph(self):
        # FIXME this function is far from finished
        try:
            #generate graph then write it
            self.writegraph(plt)
            return 0
        except:
            print("Graph generation ERROR")
            return -1

    def writeGraphs(self,plt,key):
        #FIXME this function is far from finished
        try:
            filename="Graph"+"_"+key+".png"
            plt.savefig(filename, format="PNG")
            return 0
        except:
            print("Graph write ERROR")
            return -1



myModel=logModel()
myModel.readDataSet("data.csv")
myModel.readModel("model.file")
myModel.makePrediction()
myModel.generateGraph()

