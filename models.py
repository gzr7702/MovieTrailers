"""The movie class"""

from imdb import IMDb
from BeautifulSoup import BeautifulSoup

class Movie:
	#self.pwd = 'notasecret'

	def __init__(self, title, trailer_url):
		self.title = title
		self.trailer_youtube_url = trailer_url
		self.get_movie_info()

	def get_movie_info(self):
		db_access = IMDb()
		first_result = db_access.search_movie(self.title)[0]
		movie_id = first_result.movieID
		movie = db_access.get_movie(movie_id)
		self.poster_image_url = movie['cover url']
		self.plot_outline = movie['plot outline']
		self.genres = ' '.join(movie['genres'])
