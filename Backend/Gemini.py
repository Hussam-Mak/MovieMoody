from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

API_KEY = 'AIzaSyC7SzopNzlQ1qUUIG7lwiLTr6SP7DaZ80A'  # Replace with your actual API key
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/recommend_movie', methods=['POST'])
def recommend_movie():
    data = request.json
    feeling = data.get('feeling')

    if not feeling:
        return jsonify({'error': 'Feeling input is required'}), 400

    prompt = f"""
    I am feeling {feeling}. Recommend me a movie that matches this mood.
    Please provide:
    - Movie title
    - A short description
    - Why it matches this feeling
    """

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_URL, json=body)

        if response.status_code == 200:
            movie = response.json()['candidates'][0]['content']['parts'][0]['text']
            return jsonify({'recommendation': movie})
        else:
            print(response.json())  # For debugging
            return jsonify({'error': 'Gemini API error', 'details': response.json()}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
