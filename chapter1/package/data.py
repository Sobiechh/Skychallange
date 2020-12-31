import os
import pandas as pd
import hashlib

class Task:
    def __init__(self, valuesDict):
        self.valuesDict = valuesDict

        #data class
        self.data = Data()
        self.df = self.data.read_data()
        self.columns = self.df.columns.values

        self.valuesDict['deadline'] = self.parseTime()


    def operation_control(self):
        if self.valuesDict['operation'] == 'add':
            self.add()

        if self.valuesDict['operation'] == 'update':
            self.update()

    def add(self):
        if self.valuesDict['name'] == None:
            print('Add at least name of the task!')
        else:
            self.data.insert_data([ self.valuesDict[value] for value in self.columns ])

    def update(self):
        for col in self.columns[:-1]:
            if self.valuesDict[col] != None:
                self.data.update_data(self.valuesDict['hash'], col, self.valuesDict[col])
        

    def parseTime(self):
        if self.valuesDict['deadline'] != None:
            return self.valuesDict['deadline'].strftime("%Y-%m-%d")
        else:
            return None
    
    def __del__(self): 
        self.data.save_data()



class Data:
    def __init__(self):
        self.df = self.read_data()
        self.dataLength = self.df.shape[0]
    
    def hash_task(self, rowIndex):
        listItems = self.df.iloc[[rowIndex]].values
        task = ''.join([str(x) for x in listItems[0]])
        hash_ = hashlib.md5(task.strip().encode()).hexdigest()

        self.df.iloc[rowIndex, -1] = hash_

    def get_index(self, hashValue):
        index_table = self.df.loc[self.df['hash'] == hashValue].index
        if len(index_table) > 0:
            return index_table[0]
        else:
            return None

    def read_data(self):
        if os.path.isfile('data.csv'):
            df = pd.read_csv('data.csv')
        else:
            df = pd.DataFrame(columns = ['name', 'description',  'deadline', 'hash'])

        return df
    
    def insert_data(self, values):
        self.df.loc[self.dataLength] = values
        self.hash_task(self.dataLength)

    def update_data(self, hashValue, colName, value):
        if len(self.df.loc[self.df['hash'] == hashValue].values) > 0:
            self.df.loc[self.df['hash'] == hashValue, colName] = value

            index = self.get_index(hashValue)
            self.hash_task(index)
        else:
            print("No task meets hash criteria")


    def remove_data(self, hashCode):
        self.df = self.df[self.df['Hash'] != hashCode]

    def save_data(self):
        self.df.to_csv('data.csv', index=False)