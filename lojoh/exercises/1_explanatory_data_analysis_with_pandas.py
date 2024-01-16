import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 100)

# to draw pictures in jupyter notebook
# %matplotlib inline
# we don't like warnings
# you can comment the following 2 lines if you'd like to

DATA_URL = "C:/Users/ludjoh01/Git/lojoh/mlcourse.ai/data/"
data = pd.read_csv(DATA_URL + "adult.data.csv")
data.head()

# Now I understand that I need to do this in Jupyter Notebook -_-