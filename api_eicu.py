import pandas as pd
import numpy as np
import csv
import json


class eicu_parser:

    def show_vars(seld, list_of_values):
        #list of values can be updated by just updating the number
        #no need to hard code stuff
        #dt will store all the cols mapped to one table, and convert to json for javascript compat
        
        dt = {}
        for i in list_of_values:
            if(value == 1):
                dt["vitals"] = vitals()
            elif (value == 2):
                dt["bg"] = blood_gases()
            elif value == 3:
                dt["labs"] = labs()
            elif value == 4:
                dt["nurseeve"] = nurse_e()
            elif value == 5:
                dt["charteve"] = chart_e()
            elif value == 6:
                dt["med"] = medication()
            else:
                dt["patient"] = patient_details()
            
            return json.dump(dt)


    def vitals_vars(self, value):
        df = pd.read_csv("vitalPeriodic.csv")
        cols = df.columns
        cols = cols[3:]
        del df
        return cols



    def blood_gases(self, value):

    def labs(self, value):
        df = pd.read_csv("lab.csv")
        cols = df['labname'].unique()
        return cols

        

    def nurse_e(self, value):

    def chart_e(self, value):

    def medication(self, value):
        df = pd.read_csv("medication.csv")
        cols = df['drugname'].unique()
        return cols

    def patient_details(self, value):
