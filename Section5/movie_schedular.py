current_movies = {'Minecraft': '3:20pm',
                  'Revenge of the Sith': '4:20pm',
                  'Deadpool & Wolverine': '8:00pm',
                  'Mickey 17':    '12:00pm',
                  'Captian America': '10:00pm'  
                  }

print("We are showing the following movies:")
for key in current_movies:
    print(key)

movie = input ('What movie would you like the showtime for? \n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isnt playing")
else:
    print(movie, 'is playing at', showtime)