
# test_project.py - Basic Unit Tests

import unittest
from gemini_api import get_movie_recommendation
from tmdb_api import get_movie_details
from database import init_db, add_movie, get_watchlist
from utelly import get_movie_provider


class TestMovieMoody(unittest.TestCase):

    def test_gemini_api(self):
        result = get_movie_recommendation('happy')
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_tmdb_api(self):
        movie = get_movie_details('The Pursuit of Happyness')
        self.assertIn('title', movie)

    def test_database(self):
        init_db()
        test_movie = {'title': 'Test Movie', 'release_date': '2024-01-01', 'rating': 9.0, 'overview': 'Test movie description'}
        add_movie('testuser', test_movie, get_movie_provider(test_movie))
        watchlist = get_watchlist('testuser')
        self.assertGreater(len(watchlist), 0)

    def test_get_movie_provider(self):
        providers = get_movie_provider('The Pursuit of Happyness')
        self.assertIn('provider', providers)

if __name__ == '__main__':
    unittest.main()
