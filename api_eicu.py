import pandas as pd
import numpy as np
import csv
import json


class eicu_parser:

    def vitals_vars(self):
        df = pd.read_csv("vitalPeriodic.csv")
        cols = df.columns.tolist()
        cols = cols[3:]
        del df
        return cols

    def labs(self):
        df = pd.read_csv("lab.csv")
        cols = df['labname'].unique()
        cols = cols.tolist()
        return cols

    def nurse_e(self):
        df = pd.read_csv("nurseCharting.csv")
        cols = df['nursingchartcelltypevallabel'].unique()
        cols = cols.tolist()
        return cols

    # def chart_e(self, value):

    def medication(self):
        df = pd.read_csv("medication.csv")
        cols = df['drugname'].unique()
        cols = cols.tolist()
        return cols

    # def patient_details(self, value):

    def show_vars(self, list_of_values):
        # list of values can be updated by just updating the number
        # no need to hard code stuff
        # dt will store all the cols mapped to one table, and convert to json for javascript compat

        dt = {}
        for value in list_of_values:
            if value == 1:
                dt["vitals"] = self.vitals_vars()

            elif value == 3:
                dt["labs"] = self.labs()
            elif value == 4:
                dt["nurseeve"] = self.nurse_e()

            elif value == 6:
                dt["med"] = self.medication()

        return dt
