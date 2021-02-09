import urllib.request
import csv
import pandas as pd

class data():

    def __init__(self):
        data.time_series=0

    def update_csv(self):
        url = 'https://raw.githubusercontent.com/Daniel-Breuss/covid-data-austria/master/austriadata.csv'
        urllib.request.urlretrieve(url, './Data/data-austria.csv')

    def create_time_series(self):
        self.time_series=pd.read_csv("./Data/data-austria.csv",usecols=["Datum","Fälle_gesamt"])
        
data_austria=data()
data_austria.create_time_series()
print(data_austria.time_series)




