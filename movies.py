"""This is the main module of the application. It contains the movie class. 
	Movie objects are creating by passing in a dict w/titles and trailer links.
	We pass a list of movie objects off to the web server. 
"""

import fresh_tomatoes
import json

class Movie:
	"""The title is passed in to the constructor,
		the rest of the info pulled from the local database."""
	def __init__(self, title):
		self.title = title
		with open('data.json') as f:
			self.raw_movie_info = json.load(f)
		self.get_movie_info()

	def get_movie_info(self):
		"""We load the data from data.json file in the constructor. If we 
			were using a realdatabase, we would have queries here.
		"""
		self.trailer_youtube_url = self.raw_movie_info[self.title]['trailer']
		self.stars = '/'.join(self.raw_movie_info[self.title]['stars'])
		self.poster_image_url =  self.raw_movie_info[self.title]['poster_url']
		self.plot_outline =  self.raw_movie_info[self.title]['blurb']

def movie_trailer():
	""" Craetes the list of movie objects, then calls the main module
	"""
	titles = ["Goodfellas", "The Godfather", "Big Lebowski", "Casablanca",\
			"State of Grace", "The Girl with the Dragon Tattoo"]
	movies = []

	for title in titles:
		movies.append(Movie(title))

	fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
	movie_trailer()