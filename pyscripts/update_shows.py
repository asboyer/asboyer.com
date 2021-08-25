import movie_backend

def update_shows():
    movie_backend.update_movie_database('shows')

if __name__ == "__main__":
    update_shows()