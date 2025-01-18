class Movie:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
    def __str__(self): #toString override
        return self.name + " is a "+self.genre+" movie!"