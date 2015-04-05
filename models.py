"""This is the movie class. We pass in the title and the link to the trailer, then
	get the other infor from the IMDb database. Would be nice to grab the trailer too,
	but you have to pay for that so we hardcoded it in :-).
"""

from imdb import IMDb
from BeautifulSoup import BeautifulSoup

class Movie:
	def __init__(self, title, trailer_url):
		self.title = title
		self.trailer_youtube_url = trailer_url
		self.get_movie_info()

	def get_movie_info(self):
		db_access = IMDb()
		first_result = db_access.search_movie(self.title)[0]
		movie_id = first_result.movieID
		movie = db_access.get_movie(movie_id)
		self.stars = str(movie['actors'][0]) + '/' + str(movie['actors'][1]) + '/' + str(movie['actors'][2])
		self.poster_image_url = movie['cover url']
		self.plot_outline = movie['plot outline']
