#using numpy and pandas to generate a digram of the data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest

date = pd.date_range('1/1/2000', periods=100, freq='D') #create a date range
data = pd.DataFrame(np.random.randn(100, 4), index=date, columns=list('ABCD')) #create a dataframe

class TestData(unittest.TestCase):
    def test_shape(self):
        # test that the data has the correct shape
        self.assertEqual(data.shape, (100, 4))

    def test_column_names(self):
        # test that the data has the correct column names
        self.assertEqual(list(data.columns), list('ABCD'))

data.plot(kind='bar') #plot the data
plt.show() #show the plot
