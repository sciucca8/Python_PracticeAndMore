"""import imdb
 
def actor_role_dict(movie_code):
    actor_role = {}
    moviesDB = imdb.IMDb()
    movie = moviesDB.get_movie(movie_code)
    for actor in movie["cast"]:
        actor_role[actor] = actor.currentRole
    return actor_role

result = actor_role_dict("7631058")
print(result)"""





import imdb

moviesDB = imdb.IMDb()
movies = moviesDB.search_movie("The lord of the rings")

for movie in movies:
    title = movie["title"]
    year = movie["year"]
    print(f"{title} - {year}")


"""
movie = moviesDB.get_movie("7631058")
a1 = movie["cast"][0]
print(a1)
print(type(a1))
dir(a1)
a1.items()
print(a1['canonical name'])
a1.name
"""


import imdb
act_char = {}
ia =  imdb.Cinemagoer()
movies = ia.search_movie('Harry Potter')
print(type(movies[0]))

#print(ia.get_movie_infoset())
#print(movies[0])
#for x in movies:
#    print(x)

movie = ia.get_movie('0133093')
#print(movie['cast'])
#print(type(movie))
#print(movie.infoset2keys)
#print(movie['year'], movie['rating'])
#print(movie['title'])
#print(movie.current_info)
#print(movie['cast'])
for y in movie['cast']:
    #print(y)
    #print(type(y.currentRole['name']))
    #print(type(y.currentRole))
    act_char[y['name']] = y.currentRole['name']
    #print(act_char)
print(act_char)
#print(dir(y))
print(y.myName)

keanu = ia.get_person('0000206')
print(type(keanu))
print(keanu.infoset2keys)
print(keanu['main'])



import imdb

ia = imdb.Cinemagoer()
actor = ia.get_person('0000206')
movie = ia.get_movie('0133093')
print(dir(movie))
print(dir(actor))
print(actor._Container_role())
ia.update(actor, info = ['awards',  'main'])
print(actor.current_info)
print(actor['main'])
#print(actor.infoset2keys)
#print(actor['filmography']['actor'])
#print(actor['filmography'].keys())




import imdb

ia = imdb.Cinemagoer()
print(ia.get_movie_infoset())
print(ia.get_person_infoset())
print(ia.get_company_infoset())






