import sys
import requests
import imdb 
import json

sys.path.append('./secret')
from api_keys import tmdb_key as KEY

def imdb_title_from_search(query):
    ia = imdb.IMDb()
    search = ia.search_movie(query)
    return search[0]['title']

def imdb_id_from_title(title):
    ia = imdb.IMDb()
    
    search = ia.search_movie(title)

    return search[0].movieID

def get_movie_url(imdb_id, spec):
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    
    def size_str_to_int(x):
        return float("inf") if x == 'original' else int(x[1:])

    url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(url)
    config = r.json()

    base_url = config['images']['base_url']
    sizes = config['images']['poster_sizes']
    max_size = max(sizes, key=size_str_to_int)

    IMG_PATTERN = 'https://api.themoviedb.org/3/find/tt{imdbid}?api_key={key}&external_source=imdb_id'

    r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=imdb_id))
    api_response = r.json()
    if spec == 'shows':
        rel_path = api_response['tv_results'][0]['poster_path']
    else:    
        rel_path = api_response['movie_results'][0]['poster_path']
    url = "{0}{1}{2}".format(base_url, max_size, rel_path)
    return url

def update_movie_database(spec):
    with open(f'./data/add/{spec}.txt', 'r') as f:
        movies = f.readlines()

    f = open(f'./data/add/{spec}.txt', 'w+')
    f.close()

    for i in range(len(movies)):
        print(f'adding \'{movies[i]}\'...'.replace("\n", "")) 
        movies[i] = imdb_title_from_search(movies[i])

    with open(f'./data/favorites/films/{spec}.json', 'r') as json_file:
        data = json.load(json_file)

        new_movies = {}
        ia = imdb.IMDb()

        for movie in movies:
            # movie is in the list, but not present in the dictionary
            new_movies[movie] = {}
            new_movies[movie]['id'] = imdb_id_from_title(movie)
            new_movies[movie]['title'] = movie
            new_movies[movie]['image'] = get_movie_url(new_movies[movie]['id'], spec)
            new_movies[movie]['rating'] = ia.get_movie(new_movies[movie]['id']).data['rating']
            new_movies[movie]['scorecard'] = {
                                            'screenplay': 0.0,
                                            'acting': 0.0,
                                            'score': 0.0,
                                            'cinematography': 0.0,
                                            'replay_value': 0.0
                                            }
            new_movies[movie]['asboyer_score'] = 0.0

    data.update(new_movies)        

    with open(f'./data/favorites/films/{spec}.json', 'w') as json_file: 
        json.dump(data, json_file, indent=4)
        
if __name__ == "__main__":
    print('testing...')
    update_movie_database()
# EXTRA:

# DOWNLOADING IMG

# r = requests.get(url)
# filetype = r.headers['content-type'].split('/')[-1]
# filename = 'poster_{0}.{1}'.format(1,filetype) 
# with open(filename,'wb') as w:
#     w.write(r.content)

# help from: 
# https://johannesbader.ch/blog/tutorial-download-posters-with-the-movie-database-api-in-python/
# https://www.geeksforgeeks.org/python-imdbpy-getting-movie-id-from-searched-movies/