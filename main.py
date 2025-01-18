from MovieOrganizer import MovieOrganizer

organizer = MovieOrganizer()
organizer.add_movie("Movie 1", "Mystery")
organizer.add_movie("Movie 2", "Crime")
organizer.add_movie("Movie 3", "Action")
organizer.add_movie("Movie 4", "Drama")
organizer.add_movie("Movie 5", "Sci-Fi")
organizer.remove_movie("Movie 4")

print("All movies:")
organizer.list_all_movies()

# print("\nMovies by genre:")
# user_genre = input("Enter a genre: ")
# organizer.list_movies_by_genre(user_genre)
