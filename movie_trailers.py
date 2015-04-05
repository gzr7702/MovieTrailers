"""This is the main module of the application. We create a dict w/titles and
	trailer links, create all the movie objects, then pass them off to the web 
	server. 
"""

import web_server 
from models import Movie

def movie_trailer():
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

	web_server.open_movies_page(movies)


if __name__ == '__main__':
	movie_trailer()