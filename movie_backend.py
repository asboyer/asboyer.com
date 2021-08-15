# help from: 
# https://johannesbader.ch/blog/tutorial-download-posters-with-the-movie-database-api-in-python/
# https://www.geeksforgeeks.org/python-imdbpy-getting-movie-id-from-searched-movies/

def get_movie_url(movie_title):
    import sys, requests, urllib, imdb, json
    sys.path.append('secret')
    from api_keys import tmdb_key as KEY


    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'

    def imdb_id_from_title(title):
        ia = imdb.IMDb()
        
        search = ia.search_movie(title)

        return search[0].movieID

    def size_str_to_int(x):
        return float("inf") if x == 'original' else int(x[1:])

    imdb_id = imdb_id_from_title(movie_title)

    url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(url)
    config = r.json()

    base_url = config['images']['base_url']
    sizes = config['images']['poster_sizes']

    max_size = max(sizes, key=size_str_to_int)

    IMG_PATTERN = 'https://api.themoviedb.org/3/find/tt{imdbid}?api_key={key}&external_source=imdb_id'

    r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=imdb_id))

    api_response = r.json()

    rel_path = api_response['movie_results'][0]['poster_path']

    url = "{0}{1}{2}".format(base_url, max_size, rel_path)

    return url

# EXTRA:

# DOWNLOADING IMG

# r = requests.get(url)
# filetype = r.headers['content-type'].split('/')[-1]
# filename = 'poster_{0}.{1}'.format(1,filetype) 
# with open(filename,'wb') as w:
#     w.write(r.content)
