"""The movie class"""

from imdb import IMDb
from BeautifulSoup import BeautifulSoup

class Movie:

	def __init__(self, title):
		self.title = title
		self.poster_image_url = self.get_poster(self.title)
		self.trailer_youtube_url = ''

	def get_poster(self, title):
		db_access = IMDb()
		first_result = db_access.search_movie(title)[0]
		movie_id = first_result.movieID
		movie = db_access.get_movie(movie_id)
		return movie['cover url']
