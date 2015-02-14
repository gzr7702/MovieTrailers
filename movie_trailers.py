"""main"""

import fresh_tomatoes 
from models import Movie

def movie_trailer():
	titles = ["Goodfellas", "Godfather", "Big Lebowski"]
	movies = []

	for title in titles:
		movies.append(Movie(title))

	fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
	movie_trailer()