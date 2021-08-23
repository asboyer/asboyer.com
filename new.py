import json
import imdb

ia = imdb.IMDb()

with open('data/movies.json', 'r') as db:
    movies = json.load(db)

for movie in movies:
    print(movie)
    # movies[movie]['rating'] = ia.get_movie(movies[movie]['id']).data['rating']
    movies[movie]['title'] = movie


with open(f'data/movies.json', 'w') as json_file: 
    json.dump(movies, json_file, indent=4)