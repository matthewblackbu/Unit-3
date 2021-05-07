import pandas as pd
import numpy as np
import math
import sys


def exampl1():
    # THIS IS A LONG COMMENT AND should be wrapped to fit within
    # a 72 character limit
    some_tuple = (1, 2, 3, 'a')
    some_variable = {"long": "LONG CODE LINES "
                     "should be wrapped"
                     "within 79 character to "
                     "prevent page cutoff stuff",
                     "other": [math.pi, 100, 200,
                               300, 9999292929292,
                               "This IS a long string"
                               "that looks gross and goes"
                               " beyond what it should"],
                     "more": {"inner": "THIS whole logical "
                              "line should be wrapped"},
                     "data": [444, 5555, 222, 3, 3, 4, 4,
                              5, 5, 5, 5, 5, 5, 5]}
    return (some_tuple, some_variable)


def example_2():
    return {"has_key() is deprecated": True}


class Example3(object):

    def __init__(self, bar):
        if bar:
            bar += 1
            bar *= bar
            return bar
        some_string = "INDENTATION IN MULTIPLE STRINGS "\
                      "SHOULD NOT BE TOUCHED"\
                      " only actual code should be reindented"\
                      ",THIS IS MORE CODE"
        return (sys.path, some_string)


class Helpers:

    def __init__(self, df):
        self.df = df

    def null_count():
        """Returns # of null values"""
        return self.df.isnull().sum().sum()

    def rm_outlier():
        """Removes outliers"""
        remove_index = []
        for i in range(len(self.df.columns)):
            self.df = self.df.sort_values(by=i, ascending=False)
            IQR_1_5 = (self.df[i].quantile(.75)-self.df[i].quantile(0.25))*1.5
            IQR_L_U = [self.df[i].quantile(0.25)-IQR_1_5,
                       self.df[i].quantile(.75)+IQR_1_5]
            for j in range(len(self.df)):
                if (self.df.loc[j][i] > IQR_L_U[1] or
                        self.df.loc[j][i] < IQR_L_U[0]):
                    remove_index.append(j)
        self.df.drop(remove_index, inplace=True)
        self.df = self.df.sort_index()
        return self.df


class Country:

    def __init__(self, country, population, sqmi):
        self.country = country
        self.population = population
        self.sqmi = sqmi

    def is_Beeg(self):
        return self.sqmi > 100000


class State(Country):

    def __init__(self, country, population, sqmi, abv):
        self.abv = abv
        super()

if __name__ == "__main__":
    # country1 = Country(country= "China",population= 123456,sqmi=1234567)
    # print(country1.is_Beeg())
    # state1 = State(country= "USA",population= 123457,sqmi=1234568,abv='MI')
    # print(state1.is_Beeg())
    pass
