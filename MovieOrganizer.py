from Movie import Movie

class MovieOrganizer:
    def __init__(self):                         #constructor
        self.movies = {}

    def add_movie(self, title, genre):          #method to add a movie of (INPUT: title, genre).
        self.movies[title] = Movie(title,genre)

    def remove_movie(self,title):
        self.movies[title] = None

    def list_all_movies(self):                  #method to log all movies.
        for movieObject in self.movies.values():
            print(movieObject)