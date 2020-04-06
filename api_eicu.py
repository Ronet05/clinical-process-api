import pandas as pd
import numpy as np
import csv
import json


class eicu_parser:

    def vitals_vars(self):
        df = pd.read_csv("vitalPeriodic.csv")
        cols = df.columns
        cols = cols[3:]
        del df
        return cols



    '''def blood_gases(self, value):
        df= pd.read_csv("")'''

    def labs(self):
        df = pd.read_csv("lab.csv")
        cols = df['labname'].unique()
        return cols

        

    def nurse_e(self):
        df = pd.read_csv("nurseCharting.csv")
        cols = df['nursingchartcelltypevallabel'].unique()
        return cols

    #def chart_e(self, value):

    def medication(self):
        df = pd.read_csv("medication.csv")
        cols = df['drugname'].unique()
        return cols

    #def patient_details(self, value):

    def show_vars(self, list_of_values):
        #list of values can be updated by just updating the number
        #no need to hard code stuff
        #dt will store all the cols mapped to one table, and convert to json for javascript compat
        
        dt = {}
        for value in list_of_values:
            if value == 1:
                dt["vitals"] = vitals_vars()
            
            elif value == 3:
                dt["labs"] = labs()
            elif value == 4:
                dt["nurseeve"] = nurse_e()
          
            elif value == 6:
                dt["med"] = medication()
           
            
            return json.dumps(dt)

