"""This is the main module of the application. It contains the movie class. 
	Movie objects are creating by passing in a dict w/titles and trailer links.
	We pass a list of movie objects off to the web server. 
"""

import fresh_tomatoes
from imdb import IMDb
from BeautifulSoup import BeautifulSoup

class Movie:
	"""The trailer url and title are passed in to the constructor,
		the rest of the info pulled from the IMDb database."""
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

def movie_trailer():
	""" Craetes the list of movie objects, then calls the main module
	"""
	#titles = ["Goodfellas", "Godfather", "Big Lebowski"]
	titles = {"Goodfellas":'https://www.youtube.com/watch?v=qo5jJpHtI1Y', 
			"The Godfather": 'https://www.youtube.com/watch?v=sY1S34973zA', 
			"Big Lebowski": 'https://www.youtube.com/watch?v=cd-go0oBF4Y',
			"Casablanca": 'https://www.youtube.com/watch?v=EJvlGh_FgcI',
			"State of Grace": 'https://www.youtube.com/watch?v=PN_L96iEQfQ',
			"The Girl with the Dragon Tattoo": 'https://www.youtube.com/watch?v=DqQe3OrsMKI'
			}

	movies = []

	for title, trailer in titles.items():
		movies.append(Movie(title, trailer))

	fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
	movie_trailer()