

from update_movies import update_movies
from update_music import update_music, update_tracks, import_from_all_time
from update_shows import update_shows

update_movies()
update_music('all')
import_from_all_time()
update_tracks()
update_shows()