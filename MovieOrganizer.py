from Movie import Movie

class MovieOrganizer:
    def __init__(self):                         #constructor
        self.movies = {}

    def __str__(self):                          #tostring override
        s=""
        for movieObject in self.movies.values():
            s+="\n"+str(movieObject)
        return s

    def add_movie(self, title, genre):          #method to add a movie of (INPUT: title, genre).
        self.movies[title] = Movie(title,genre)

    def remove_movie(self,title):
        #self.movies[title] = None #bad practice
        del self.movies[title]  #good practice

    def list_all_movies(self):                  #method to log all movies.
        for movieObject in self.movies.values():
            print(movieObject)
    
    # implement these three methods:
	# -size
	# -isEmpty if size==0
	# -contains (string name)
     #   return bool

    def size(self):
        return len(self.movies)
    
    def isEmpty(self):
        # return self.size()==0
        currentSize = self.size()
        if currentSize == 0:
            return True
        else:
            return False