
import pandas as pd
import difflib
import h5py

# Load artist data
artist_data = pd.read_csv('artists.csv')
artists_data = artist_data.iloc[0:20000]
artists_data = artists_data.drop_duplicates(subset='artist_mb', keep='first')

# Selected features
selected_features = ['artist_mb', 'tags_lastfm', 'country_mb', 'tags_mb']

# Load similarity matrix from HDF5 file
with h5py.File('similarityscores.h5', 'r') as hf:
    similarity11 = hf['similarity'][:]

def recommend(artist):
    artist_name = artist
    list_of_artist_name = artists_data['artist_mb'].tolist()
    find_close_match = difflib.get_close_matches(artist_name, list_of_artist_name)

    if find_close_match:
        close_match = find_close_match[0]
        print(close_match)
        artist_index = artists_data[artists_data['artist_mb'] == close_match].index[0]
        distances = similarity11[artist_index]
        artists_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:30]

        recommended_artists = [close_match] + [artists_data.iloc[i[0]].artist_mb for i in artists_list]
        return recommended_artists
    else:
        print(f"No close match found for {artist_name}")
        return []

# Example usage
print("Machine Ready...")
recommended_artists = recommend('arctic monkeys')
print(recommended_artists)

