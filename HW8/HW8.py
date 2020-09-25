#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW08 - API and Requests module - due Thursday, November 2, 2017
"""
import requests

__author__ = """Jared Raiola"""
__collaboration__ = """ I worked on the homework assignment alone, using only this semester's course materials. """

"""
Get an account from themoviedb.org. Go to this link and create an account:

https://www.themoviedb.org/?_dc=1489731496

assign your API key to the variable below
"""

API_KEY = "0671b58498f2afd59aea2e66e331e5e4"
base_url = "https://api.themoviedb.org/3/movie/"

"""
Function name: get_movie_recommendations
Parameters: movie_ids (list of ints)
Returns: recommended movie titles (list of strings)
Description: Write a function that takes in a list of movie IDs. Find the
movies corresponding to the IDs. If the popularity of the movie is greater than
20, add the movie title (string) to a list. Return the list of titles.

Note: Your function should be able to handle invalid movie ids.
"""


def get_movie_recommendations(movie_ids):
    morethan = []
    for num in movie_ids:
        myurl = base_url + str(num) + "?api_key=" + API_KEY
        result = requests.get(myurl)
        moviedict = result.json()
        try:
            if moviedict["popularity"] > 20:
                morethan.append(moviedict["title"])
        except:
            continue
    return morethan
    
            


"""
Function name: get_upcoming
Parameters: None
Returns: the next 10 upcoming movies titles (list of strings)
Description: Write a function that uses an API call and returns a list of the
next ten upcoming movie titles (strings) that come first alphabetically. Only
consider the upcoming movies that are listed on page 1.

Hint: First, find the movie titles from page 1 and add them to a list. Sort
this list. Then take the first ten movies titles from this list.
"""

def get_upcoming():
    newest = []
    temp = []
    myurl = base_url + "upcoming?api_key=" + API_KEY + "&language=en-US&page=1"
    result = requests.get(myurl)
    moviedict = result.json()
    for num in range(len(moviedict["results"])):
        temp.append(moviedict["results"][num]["title"])
    temp.sort()
    for i in range(0,10):
        newest.append(temp[i])
    return newest


"""
Function name: get_cast_members
Parameters: movie_id (int), job_title (string), section (string)
Returns: names of people who worked the job specified by the job title for the
given movie (list of strings)
Description: Write a function that takes in a movie_id, a job_title, and a
section (either â€œcastâ€ or â€œcrewâ€). Find the names of every person working on
the movie who works in the specified section and has the specified job title.
Assume everything passed in is valid. Add these names to a list. Return the
list at the end of the function.

Note: Every job_title listed as â€œActorâ€ will be considered as working for the
section "cast" and every person working for the section "cast" will be
considered under the job_title "Actor". The only job_title that works in the
â€œcastâ€ section is â€œActorâ€. All other job types will be found under the â€œcrewâ€
section.

Hint: The credits endpoint will be useful for solving this function.
"""


def get_cast_members(movie_id, job_title, section):
    lineup= []
    myurl = base_url + str(movie_id) + "/credits?api_key=" + API_KEY
    result = requests.get(myurl)
    moviedict = result.json()
    try:
        for i in range(len(moviedict[section])):
            if section == "crew" and moviedict[section][i]["job"] == job_title:
                lineup.append(moviedict[section][i]["name"])
            elif section == "cast":
                lineup.append(moviedict[section][i]["name"])
        return lineup
    except:
        return lineup


"""
Function name: map_movies_to_language
Parameters: movie_ids (list of ints), languages (list of strings)
Returns: a dictionary mapping languages to the movies titles available in that
language
Description: Write a function that takes in a list of movie ids and a list of
languages. Each string in the language list passed in will be a key in a new
dictionary. For each key (language), the corresponding value should be a list
of the movie titles that are offered in that language. Each movie title should
be in the values list for a given language only once (even if there are
different dialects / versions available for the language).

Note: Your function should be able to handle invalid movie ids.
"""


def map_movies_to_languages(movie_ids, languages):
    aDict = {}
    for lang in languages:
        aList = []
        for num in movie_ids:
            myurl = base_url + str(num) + "/translations?api_key=" + API_KEY
            result = requests.get(myurl)
            moviedict = result.json()
            url = base_url + str(num) + "?api_key=" + API_KEY
            aresult = requests.get(url)
            moviedict2 = aresult.json()
            try:
                for i in range(len(moviedict["translations"])):
                    if moviedict["translations"][i]["english_name"] == lang:
                        aList.append(moviedict2["title"])
                        break
            except:
                 continue
        aDict[lang] = aList
    return aDict

"""
Function name: get_genre_movies
Parameters: movie_ids (list of ints), genre (string), start_year (int),
end_year (int)
Returns: movie titles (list of strings)
Description: Write a function that takes in a list of movie ids, a genre, and a
range of years. Find all the movie titles that are of the genre passed in and
whose release date falls between the start year and end year passed in. Return
a list of the movie titles that meet this criteria.

Note: Your function should be able to handle invalid movie ids and genres.
Years will always be valid.
"""


def get_genre_movies(movie_ids, genre, start_year, end_year):
    intime = []
    for num in movie_ids:
        myurl = base_url + str(num) + "?api_key=" + API_KEY
        result = requests.get(myurl)
        moviedict = result.json()
        try:
            for i in range(len(moviedict["genres"])):
                if int(moviedict["release_date"][0:4])<end_year and int(moviedict["release_date"][0:4])>start_year and moviedict["genres"][i]["name"]==genre:
                    intime.append(moviedict["title"])
        except:
            continue
    return intime


