# 🎬 Movie Moody

**Movie Moody** is a Python command-line tool that recommends movies based on your mood. Powered by APIs like TMDb, Utelly, and Gemini, it curates relevant movies, helps you find where to stream them, and lets you save them to a personal watchlist.

---

## 🚀 Features

- Get personalized movie recommendations based on mood
- Find out where to stream recommended movies
- Save movies to a local watchlist using SQLite
- Clean, interactive CLI experience
- Uses TMDb, Utelly, and Gemini APIs

---

## 🛠️ Tech Stack

- **Python 3**
- **TMDb API** – for movie info
- **Utelly API** – for streaming platform availability
- **Gemini API** – for mood interpretation (optional)
- **SQLite** – for persistent watchlist storage
- **dotenv** & **requests** libraries

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/miles1744/movie-moody.git
cd movie-moody

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

Create a .env file in the project root directory with your API keys:

TMDB_API_KEY=your_tmdb_api_key
UTELLY_API_KEY=your_utelly_api_key
GEMINI_API_KEY=your_gemini_api_key

▶️ How to Run
`python main.py



movie-moody/
├── auth.py           # Loads API keys from .env
├── database.py       # Watchlist logic with SQLite
├── gemini_api.py     # Mood analysis using Gemini
├── main.py           # CLI entry point
├── test_project.py   # Unit tests (optional)
├── tmdb_api.py       # Handles movie fetching
├── utelly.py         # Fetches streaming availability
├── requirements.txt  # Required packages
├── .env              # API keys (not checked in)
├── watchlist.db      # Local SQLite database
└── README.md         # This file

