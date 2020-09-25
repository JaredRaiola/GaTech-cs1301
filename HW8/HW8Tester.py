import sys
import unittest
import importlib
import time


"""
Autograder for HW08 - CS1301 - Spring 2017
"""


class TestMyClass(unittest.TestCase):

    ###################################
    # GET_MOVIE_RECOMMENDATIONS TESTS #
    ###################################

    def test_get_movie_recommendations_1(self):
        movie_ids = [343668, 17473, 2493, 36968]
        ans = ['Kingsman: The Golden Circle']
        self.assertListEqual(ans, hw.get_movie_recommendations(movie_ids),
                         msg='Failed get_movie_recommendations w/' + str(
                             movie_ids) + ".")
        time.sleep(2)

    def test_get_movie_recommendations_2(self):
        movie_ids = [98329203, 29039, 33333333, 23]
        ans = []
        self.assertListEqual(ans, hw.get_movie_recommendations(movie_ids),
                         msg='Failed get_movie_recommendations w/' + str(
                             movie_ids) + ".")
        time.sleep(2)

    def test_get_movie_recommendations_3(self):
        movie_ids = []
        ans = []
        self.assertListEqual(ans, hw.get_movie_recommendations(movie_ids),
                         msg='Failed get_movie_recommendations w/' + str(
                             movie_ids) + ".")
        time.sleep(2)

    def test_get_movie_recommendations_4(self):
        movie_ids = [671, 2486, 19995, 27205]
        ans = ["Harry Potter and the Philosopher's Stone", 'Avatar',
               'Inception']
        self.assertListEqual(ans, hw.get_movie_recommendations(movie_ids),
                         msg='Failed get_movie_recommendations w/' + str(
                             movie_ids) + ".")
        time.sleep(2)

    def test_get_movie_recommendations_5(self):
        movie_ids = [60735, 1422, 640, 91745, 597]
        ans = ['Titanic']
        self.assertListEqual(ans, hw.get_movie_recommendations(movie_ids),
                         msg='Failed get_movie_recommendations w/' + str(
                             movie_ids) + ".")
        time.sleep(2)

    ###################################
    # GET_UPCOMING TESTS              #
    ###################################

    def test_get_upcoming(self):
        ans = ['A Bad Moms Christmas', 'American Assassin', 'Atomic Blonde',
               'Battle of the Sexes', 'Flatliners', 'Happy Death Day',
               'Jigsaw', 'Justice League', 'My Little Pony: The Movie',
               'Only the Brave']
        self.assertEqual(ans, hw.get_upcoming())
        time.sleep(2)

    ###################################
    # GET_CAST_MEMBERS TESTS          #
    ###################################

    def test_get_cast_members_1(self):
        movie_id = 1422
        job_title = "Director"
        section = "crew"
        ans = ['Martin Scorsese']
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)
        time.sleep(2)

    def test_get_cast_members_2(self):
        movie_id = 671
        job_title = "Actor"
        section = "cast"
        ans = ['Daniel Radcliffe', 'Rupert Grint', 'Emma Watson',
               'Richard Harris', 'Tom Felton', 'Robbie Coltrane', 'Alan Rickman'
            , 'Maggie Smith', 'Richard Griffiths', 'Ian Hart', 'Fiona Shaw',
               'John Hurt', 'David Bradley', 'Matthew Lewis', 'Sean Biggerstaff'
            , 'Warwick Davis', 'Harry Melling', 'James Phelps', 'Oliver Phelps',
               'John Cleese', 'Chris Rankin', 'Alfie Enoch', 'Devon Murray',
               'Jamie Waylett', 'Josh Herdman', 'Zoë Wanamaker', 'Julie Walters'
            , 'Bonnie Wright', 'Luke Youngblood', 'Verne Troyer',
               'Adrian Rawlins', 'Geraldine Somerville', 'Elizabeth Spriggs',
               'Nina Young', 'Terence Bayler', 'Leslie Phillips',
               'Simon Fisher-Becker', 'Derek Deadman', 'Ray Fearon',
               'Eleanor Columbus', 'Ben Borowiecki', 'Danielle Tabor',
               'Leilah Sutherland', 'Emily Dale', 'Will Theakston', 'Scot Fearn'
            , 'Saunders Triplets', 'Amy Puglia', 'David Brett', 'Leila Hoffman'
            , 'Hazel Showham', 'Christina Petrou', 'Gemma Sandzer',
               'Derek Hough', 'Julianne Hough', 'Zoe Sugg', 'Jimmy Vee',
               'Kieri Kennedy']
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)
        time.sleep(2)

    def test_get_cast_members_3(self):
        movie_id = 1422
        job_title = "Casting"
        section = "crew"
        ans = ['Ellen Lewis']
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)
        time.sleep(2)

    def test_get_cast_members_3(self):
        movie_id = 33333333
        job_title = "Casting"
        section = "crew"
        ans = []
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)
        time.sleep(2)

    def test_get_cast_members_3(self):
        movie_id = 33333333
        job_title = "Casting"
        section = "crew"
        ans = []
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)

    def test_get_cast_members_4(self):
        movie_id = 2454
        job_title = "Costume Design"
        section = "crew"
        ans = ['Isis Mussenden']
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)
        time.sleep(2)

    def test_get_cast_members_5(self):
        movie_id = 76
        job_title = "Actor"
        section = "cast"
        ans = ['Ethan Hawke', 'Julie Delpy', 'Andrea Eckert', 'Hanno Pöschl',
               'Karl Bruckschwaiger', 'Tex Rubinowitz', 'Erni Mangold',
               'Dominik Castell', 'Haymon Maria Buttinger', 'Harold Waiglein',
               'Bilge Jeschim', 'Kurti', 'Hans Weingartner', 'Liese Lyon',
               'Peter Ily Huemer', 'Otto Reiter', 'Hubert Fabian Kulterer',
               'Branko Andric', 'Constanze Schweiger', 'John Sloss',
               'Alexandra Seibel', 'Georg Schöllhammer', 'Christian Ankowitsch',
               'Wilbirg Reiter', 'Barbara Klebel', 'Wolfgang Staribacher',
               'Wolfgang Glüxam']
        error_msg = "Failed get_cast_members w/ movie_id: {}, job_title: {}, " \
                    "and section: {}".format(movie_id, job_title, section)
        self.assertEqual(ans, hw.get_cast_members(movie_id, job_title,
                        section), msg=error_msg)
        time.sleep(2)

    ###################################
    # MAP_MOVIES_TO_LANGUAGES TESTS   #
    ###################################

    def test_map_movies_to_languages_1(self):
        movie_ids = [2454, 671, 2486]
        languages = ["Serbian", "German", "Dutch"]
        error_msg = "Failed map_movies_to_languages w/ movie_id: {} and " \
                    "languages: {}.".format(movie_ids, languages)
        ans = {'Serbian': ["Harry Potter and the Philosopher's Stone"],
               'German': ['The Chronicles of Narnia: Prince Caspian',
                          "Harry Potter and the Philosopher's Stone",
                          'Eragon'], 'Dutch':
                   ['The Chronicles of Narnia: Prince Caspian',
                    "Harry Potter and the Philosopher's Stone", 'Eragon']}
        self.assertEqual(ans, hw.map_movies_to_languages(movie_ids,
                                                         languages),
                         msg=error_msg)
        time.sleep(2)

    def test_map_movies_to_languages_2(self):
        movie_ids = [77, 641, 67198, 627, 4148]
        languages = ["Serbian", "Tajiki", "Mandarin"]
        error_msg = "Failed map_movies_to_languages w/ movie_id: {} and " \
                    "languages: {}.".format(movie_ids, languages)
        ans = {'Serbian': ['Memento', 'Requiem for a Dream',
                           'Revolutionary Road'], 'Tajiki': [], 'Mandarin':
            ['Memento', 'Requiem for a Dream', 'Trainspotting',
             'Revolutionary Road']}
        self.assertEqual(ans, hw.map_movies_to_languages(movie_ids,
                                                         languages),
                         msg=error_msg)
        time.sleep(2)

    def test_map_movies_to_languages_3(self):
        movie_ids = [7859, 222935, 9952, 27850]
        languages = ["Czech", "English"]
        error_msg = "Failed map_movies_to_languages w/ movie_id: {} and " \
                    "languages: {}.".format(movie_ids, languages)
        ans = {'Czech': ['Half Nelson', 'The Fault in Our Stars', 'Rescue'
                                                                  ' Dawn'],
               'English': ['Half Nelson', 'The Fault in Our Stars', 'Rescue'
                                                                    ' Dawn',
                           'Halloweentown']}
        self.assertEqual(ans, hw.map_movies_to_languages(movie_ids,
                                                         languages),
                         msg=error_msg)
        time.sleep(2)

    def test_map_movies_to_languages_4(self):
        movie_ids = []
        languages = ["German", "Spanish", "Swedish"]
        error_msg = "Failed map_movies_to_languages w/ movie_id: {} and " \
                    "languages: {}.".format(movie_ids, languages)
        ans = {'German': [], 'Spanish': [], 'Swedish': []}
        self.assertEqual(ans, hw.map_movies_to_languages(movie_ids,
                                                         languages),
                         msg=error_msg)
        time.sleep(2)

    def test_map_movies_to_languages_5(self):
        movie_ids = []
        languages = ["German", "Spanish", "Swedish"]
        error_msg = "Failed map_movies_to_languages w/ movie_id: {} and " \
                    "languages: {}.".format(movie_ids, languages)
        ans = {'German': [], 'Spanish': [], 'Swedish': []}
        self.assertEqual(ans, hw.map_movies_to_languages(movie_ids,
                                                         languages),
                         msg=error_msg)
        time.sleep(2)

    def test_get_genre_movies_1(self):
        movie_ids = [5723, 921, 37056, 2454, 9655]
        genre = "Romance"
        start = 2000
        end = 2012
        error_msg = "Failed get_genre_movies w/ movie_ids: {}, genre: {}, " \
                    "start year: {}, end year: {}".format(movie_ids, genre,
                                                          start, end)
        ans = ['Once', 'Cinderella Man', 'Letters to Juliet', "She's the Man"]
        self.assertEqual(ans, hw.get_genre_movies(movie_ids, genre, start, end),
                         error_msg)
        time.sleep(2)

    def test_get_genre_movies_2(self):
        movie_ids = [5723, 921, 37056, 2454, 9655]
        genre = "Comedy"
        start = 2000
        end = 2012
        error_msg = "Failed get_genre_movies w/ movie_ids: {}, genre: {}, " \
                    "start year: {}, end year: {}".format(movie_ids, genre,
                                                          start, end)
        ans = ['Letters to Juliet', "She's the Man"]
        self.assertEqual(ans, hw.get_genre_movies(movie_ids, genre, start, end),
                         error_msg)
        time.sleep(2)

    def test_get_genre_movies_3(self):
        movie_ids = []
        genre = "Nothing"
        start = 1950
        end = 2012
        error_msg = "Failed get_genre_movies w/ movie_ids: {}, genre: {}, " \
                    "start year: {}, end year: {}".format(movie_ids, genre,
                                                          start, end)
        ans = []
        self.assertEqual(ans, hw.get_genre_movies(movie_ids, genre, start, end),
                         error_msg)
        time.sleep(2)

    def test_get_genre_movies_4(self):
        movie_ids = [13936, 35115, 92308732]
        genre = "Action"
        start = 1950
        end = 1960
        error_msg = "Failed get_genre_movies w/ movie_ids: {}, genre: {}, " \
                    "start year: {}, end year: {}".format(movie_ids, genre,
                                                          start, end)
        ans = ['Davy Crockett, King of the Wild Frontier']
        self.assertEqual(ans, hw.get_genre_movies(movie_ids, genre, start, end),
                         error_msg)
        time.sleep(2)

    def test_get_genre_movies_5(self):
        movie_ids = [13936, 35115, 92308732]
        genre = "Drama"
        start = 1950
        end = 1960
        error_msg = "Failed get_genre_movies w/ movie_ids: {}, genre: {}, " \
                    "start year: {}, end year: {}".format(movie_ids, genre,
                                                          start, end)
        ans = []
        self.assertEqual(ans, hw.get_genre_movies(movie_ids, genre, start, end),
                         error_msg)
        time.sleep(2)


if __name__ == '__main__':
    try:
        hw = importlib.import_module("HW8")
    except SyntaxError as e:
        print('-'*60)
        print("\nSubmission does not compile/run.\nError Message:\t {}\n".
              format(e))
        print('-'*60)
        sys.exit()
    except ModuleNotFoundError as e:
        print('-'*60)
        print("\nFilename is not named HW7.py or file is not in the same "
              "directory.\nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()
    except Exception as e:
        print('-'*60)
        print("\nUNEXPECTED ERROR! \nError Message:\t {}\n".format(e))
        print('-'*60)
        sys.exit()

    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner, exit=False)
