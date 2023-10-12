import pandas as pd
from scipy.spatial import distance

# Load the data
data = pd.read_csv('similarityData.csv')

# Extract Adolis García's statistics for the 2023 season
adolis_2023 = data[(data['Name'] == 'Adolis García') & (data['Season'] == 2023)]
numeric_cols = ['PA', 'BB%+', 'K%+', 'AVG+', 'OBP+', 'SLG+', 'wRC+', 'ISO+', 'BABIP+', 'LD%+', 'GB%+', 'FB%+', 'Pull%+', 'Cent%+', 'Oppo%+']
adolis_2023_numeric = adolis_2023[numeric_cols].values[0]  # Convert to 1-D array

# Calculate Euclidean distances between Adolis García's 2023 stats and every other player-season's stats in the dataset
data['Distance'] = data[numeric_cols].dropna().apply(lambda row: distance.euclidean(row, adolis_2023_numeric), axis=1)

# Sort the player-seasons by their distance to Adolis García's 2023 stats and get the 5 most similar player-seasons
most_similar_seasons = data.sort_values(by='Distance').iloc[1:11]

# Print the results
print(most_similar_seasons[['Name', 'Season', 'Distance']])
