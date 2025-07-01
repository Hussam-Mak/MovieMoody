import unittest
from unittest.mock import patch, MagicMock
import os

from gemini_api import get_movie_recommendation, GeminiAPIError


class TestGeminiAPI(unittest.TestCase):
    def setUp(self):
        os.environ['GEMINI_API_KEY'] = 'dummy_key'

    @patch('gemini_api.requests.post')
    def test_get_movie_recommendation_success(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            'recommendations': ['Inception', 'The Matrix', 'Interstellar']
        }
        mock_post.return_value = fake_response

        recs = get_movie_recommendation('sci-fi classics')

        self.assertIsInstance(recs, list)
        self.assertEqual(recs, ['Inception', 'The Matrix', 'Interstellar'])
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertIn('headers', kwargs)
        self.assertIn('json', kwargs)

    @patch('gemini_api.requests.post')
    def test_get_movie_recommendation_api_error(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 500
        fake_response.text = 'Server error'
        mock_post.return_value = fake_response

        with self.assertRaises(GeminiAPIError) as cm:
            get_movie_recommendation('anything')

        self.assertIn('500', str(cm.exception))

    @patch('gemini_api.requests.post')
    def test_get_movie_recommendation_malformed_json(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.side_effect = ValueError('No JSON')
        mock_post.return_value = fake_response

        with self.assertRaises(GeminiAPIError):
            get_movie_recommendation('broken')

os.environ['TMDB_API_KEY'] = 'dummy_key'

from tmdb_api import get_movie_details

class TestTMDBAPI(unittest.TestCase):
    @patch('tmdb_api.requests.get')
    def test_get_movie_details_success_with_poster(self, mock_get):
        # Arrange: fake a successful TMDB response with a poster_path
        fake_resp = MagicMock()
        fake_resp.status_code = 200
        fake_resp.json.return_value = {
            'results': [
                {
                    'title': 'The Matrix',
                    'release_date': '1999-03-30',
                    'vote_average': 8.7,
                    'overview': 'A computer hacker learns about the true nature of reality.',
                    'poster_path': '/poster.jpg'
                }
            ]
        }
        mock_get.return_value = fake_resp

        details = get_movie_details('The Matrix')

        self.assertEqual(details['title'], 'The Matrix')
        self.assertEqual(details['release_date'], '1999-03-30')
        self.assertAlmostEqual(details['rating'], 8.7)
        self.assertIn('true nature of reality', details['overview'])
        self.assertTrue(details['poster_url'].endswith('/w500/poster.jpg'))
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn('params', kwargs)
        self.assertEqual(kwargs['params']['query'], 'The Matrix')

    @patch('tmdb_api.requests.get')
    def test_get_movie_details_success_no_poster(self, mock_get):
        fake_resp = MagicMock()
        fake_resp.status_code = 200
        fake_resp.json.return_value = {
            'results': [
                {
                    'title': 'Unknown Indie',
                    'release_date': '2020-01-01',
                    'vote_average': 5.0,
                    'overview': 'Indie film.',
                    'poster_path': None
                }
            ]
        }
        mock_get.return_value = fake_resp

        details = get_movie_details('Unknown Indie')

        self.assertEqual(details['poster_url'], 'No poster available')
        self.assertEqual(details['title'], 'Unknown Indie')

    @patch('tmdb_api.requests.get')
    def test_get_movie_details_no_results(self, mock_get):
        fake_resp = MagicMock()
        fake_resp.status_code = 200
        fake_resp.json.return_value = {'results': []}
        mock_get.return_value = fake_resp

        details = get_movie_details('Nonexistent Movie')

        self.assertIn('error', details)
        self.assertEqual(details['error'], 'Movie not found on TMDB.')

    @patch('tmdb_api.requests.get')
    def test_get_movie_details_error_status(self, mock_get):
        fake_resp = MagicMock()
        fake_resp.status_code = 500
        fake_resp.json.return_value = {} 
        mock_get.return_value = fake_resp

        details = get_movie_details('Server Error')

        self.assertIn('error', details)
        self.assertEqual(details['error'], 'Movie not found on TMDB.')

if __name__ == '__main__':
    unittest.main()
