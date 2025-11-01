import pandas as pd 
import numpy as np
import matplotlib.pyplot as py
import seaborn as sns 

df = pd.read_csv("imdb_horror_movies.csv")
print(df.head())
print(df.shape)
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

# Fill missing values in 'genre' with 'Unknown'
df['genre'].fillna('Unknown', inplace=True)

# Fill missing values in 'movie_rating' with 'Not Rated'
df['movie_rating'].fillna('Not Rated', inplace=True)

# Fill missing values in 'review_rating' with 'Not Rated'
df['review_rating'].fillna(0.00, inplace=True)

# Fill missing values in 'runtime' with the 'Unknown'
df['runtime'].fillna('Unknown', inplace=True)

# Fill missing values in 'plot' with the 'Unknown'
df['plot'].fillna('Unknown', inplace=True)

# Fill missing values in 'cast' with the 'Unknown'
df['cast'].fillna('Unknown', inplace=True)

# Fill missing values in 'language' with the 'Unknown'
df['language'].fillna('Unknown', inplace=True)

# Fill missing values in 'filming_locations' with 'Unknown'
df['filming_locations'].fillna('Unknown', inplace=True)

# Fill missing values in 'budget' with null
df['budget'].fillna('Unknown', inplace=True)

