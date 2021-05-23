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

np.random.seed(1)

class logModel:
    def __init__(self):
        self.seed=0 #seed for train test split. still needs to be implemented
        self.__dataSetRaw=None #raw unnormalizzed dataset
        self.__dataSetTrain = None #training data
        self.__dataSetTest=None#test data
        self.__model=None # fitted model from pickles
        self.__userInput={} #users input format: dictionary
        self.__userOutput=0 #users result

    def __prepare(self,userinput):
        """a pseudo fit function. the model is already fitted but the data is passed
        in RAW so it needs to be adjusted ny splitting it then adding the user input then normalizing it
        this is so the user input can be normalized against the data"""
        try:
            self.__dataSetTrain, self.__dataSetTest = train_test_split(self.__dataSetRaw, train_size=0.7)
            scale = MinMaxScaler()
            leng= len(self.__dataSetTrain)
            self.__dataSetTrain = self.__dataSetTrain.append(userinput, ignore_index=True)
            if leng +1 != len(self.__dataSetTrain):
                raise Exception('failed', 'append')
            self.__dataSetTrain = scale.fit_transform(self.__dataSetTrain)
            self.__dataSetTest = scale.fit_transform(self.__dataSetTest)
        except:
            print("Preparation ERROR")
            return -1

    def readModel(self,filename):
        """ read in the model from a pickle file. this model is already fitted"""
        try:
            loaded_model = pickle.load(open(filename, 'rb'))
            self.__model=loaded_model
            return 0
        except:
            print("Model Read ERROR")
            return -1

    def readDataSet(self,filename):
        """Read in dataset. the dataset is RAW so it will need adjustment"""
        try:
            self.__dataSetRaw = pd.read_csv(filename)
            return 0
        except:
            print("Dataset Read ERROR")
            return -1

    def makePrediction(self, userinput=None):
        """Predict user output. this function takes the user input, prepares the dataset then predicts
        what the user will get as an output and returns it"""
        try:
            self.__prepare(userinput)
            self.__userInput = self.__dataSetTrain.iloc[-1:]
            predict = self.__model.predict([self.__userInput])
            self.__userOutput=predict
            self.__dataSetTrain=self.__dataSetTrain[:-1]
            return predict
        except:
            print("Prediction ERROR")
            return -1

    def writeGraphs(self,plt,key):
        """This function writes the graphs to a file based on the graphs name
         FIXME this function is far from finished
        """
        try:
            filename="Graph"+"_"+key+".png"
            plt.savefig(filename, format="PNG")
            return 0
        except:
            print("Graph write ERROR")
            return -1

    def generateGraph(self):
        """This function generates all the graphs in a loop while writing them to a file
            FIXME this function is far from finished"""

        try:
            to_graph = ['age', 'trestbps', 'thalach', 'oldpeak', 'chol']
            for feature in to_graph:
                sns.boxplot(y=self.__dataSetRaw[feature]).set_title(("User's " + feature))
                plt.axhline(y=user_input[feature], color='red')
                self.writeGraphs(plt, feature)
                plt.clf()
                return 0
        except:
            print("Graph generation ERROR")
            return -1



myModel=logModel()
myModel.readDataSet("dataset/heart.csv")
myModel.readModel("model.file")
myModel.makePrediction()
myModel.generateGraph()

