""" This is the main module of the application. It contains the movie class. 
	Movie objects are creating by passing in a dict w/titles and trailer links.
	We pass a list of movie objects off to the web server. """

import fresh_tomatoes
import json
import sys
import os

class Movie:
	def __init__(self, title, movie_info):
		""" The title is passed in to the constructor,
			the rest of the info is passed in as json."""

		self.title = title
		self.get_movie_info(movie_info)

	def get_movie_info(self, minfo):
		""" We load the data from a json object that's passed to the constructor. 
			If we were using a real database, we would have queries here. """

		self.trailer_youtube_url = minfo['trailer']
		self.stars = '/'.join(minfo['stars'])
		self.poster_image_url =  minfo['poster_url']
		self.plot_outline =  minfo['blurb']

def movie_trailer(args):
	""" Creates the list of movie objects, then calls the main module """

	json_file = args
	# Check if file exists, if not, exit
	if not os.path.exists(json_file):
		print("You didn't supply a valid file")
		sys.exit(1)

	# Open file and read contents into a variable
	with open(json_file) as f:
		movie_info = json.load(f)

	# List to hold movie objects
	movies = []

	# Cycle thorugh each object in the json file
	# and use it to create a movie object
	for title in movie_info:
		movies.append(Movie(title, movie_info[title]))

	# Ok. We have our movies, let's create the page
	fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
	# Check that we have the proper number of arguments
	# otherwise, exit.
	if len(sys.argv) != 2:
		print("You didn't supply the proper amount of arguments")
		print("Usage: python movies.py <path to file>")
		sys.exit(1)
	# Call our main function 
	movie_trailer(sys.argv[1])