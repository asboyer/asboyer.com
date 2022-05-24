import movie_backend
# import movie_cleanup

def update_movies():
    movie_backend.update_movie_database('movies')
    movie_backend.update_movie_database('to_watch')
    # movie_cleanup.update_movie_database('movies')

if __name__ == "__main__":
    update_movies()