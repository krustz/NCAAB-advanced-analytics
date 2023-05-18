#Cullen Wise
#pandas_corr.py
#building a correlation using my data with pandas
#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
import seaborn as sn
import matplotlib.pyplot as plt

# Ignore warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('compiled_stats\\cbbdata.csv')

corr_matrix = df.corr()

sn.heatmap(corr_matrix, annot=True)
plt.show()
