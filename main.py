import pandas as pd 
print(pd.__version__)
import numpy as np
import matplotlib.pyplot as py
import seaborn as sns 

df = pd.read_csv("imdb_horror_movies.csv")
print(df.head())