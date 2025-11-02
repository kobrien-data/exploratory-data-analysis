import pandas as pd 
import numpy as np
import matplotlib.pyplot as py
import seaborn as sns 

df = pd.read_csv("imdb_horror_movies.csv")
print(df.head())
print(df.info())

#rename columns for easier access
df.rename(columns={'Title':'title', 
                   'Genres':'genre', 
                   'Release Date': 'release_date', 
                   'Release Country' : 'release_country',
                   'Movie Run Time':'runtime', 
                   'Movie Rating':'movie_rating', 
                   'Review Rating':'review_rating', 
                   'Plot':'plot', 
                   'Cast':'cast', 
                   'Language': 'language', 
                   'Filming Locations' : 'filming_locations', 
                   'Budget' : 'budget'}, inplace=True)

# Check for missing values
print(df.isnull().sum())

for column in df.columns:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == 'int' or df[column].dtype == 'float':
            df[column].fillna(0.00, inplace=True)
        else:
            df[column].fillna('Unknown', inplace=True)

print(df.isnull().sum())


