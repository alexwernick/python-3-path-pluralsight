current_movies = {"The Grinch": "11:00am",
                  "Rudolph": "1:00pm",
                  "Frosty the Snowman": "3:00pm",
                  "Christmas Vacation": "5:00pm"}

print("We are currently showing the following movies:")

for key in current_movies:
    print(key)

movie = input("What moview do you want the time for?")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie is not playing")
else:
    print(movie, "is showing at", showtime)