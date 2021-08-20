import movie_backend

def update_movies():
    movie_backend.update_movie_database('movies')

if __name__ == "__main__":
    update_movies()