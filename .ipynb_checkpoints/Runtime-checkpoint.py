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




class logModel:
    def __init__(self):
        self.seed=0
        self.__dataSet=None
        self.__model=None
        self.__userInput=[]

    def readModel(self,filename):
        #read in the model
        try:
            loaded_model = pickle.load(open(filename, 'rb'))
            self.__dataSet=loaded_model
            return 0
        except:
            print("Model Read ERROR")
            return -1

    def readDataSet(self,filename):
        #read in the dataset
        try:
            self.__model = pd.read_csv(filename)
            return 0
        except:
            print("Dataset Read ERROR")
            return -1

    def makePrediction(self, userinput=[]):
        self.__userInput=userinput
        try:
            return  self.__dataSet.predict([userinput])
        except:
            print("Prediction ERROR")
            return -1

    def generateGraph(self):
        try:
            return 0
        except:
            print("Graph generation ERROR")
            return -1

    def writeGraphs(self):
        try:
            return 0
        except:
            print("Graph write ERROR")
            return -1



myModel=logModel()
myModel.readDataSet("data.csv")
myModel.readModel("model.file")
myModel.makePrediction()
myModel.generateGraph()
myModel.writeGraphs()

