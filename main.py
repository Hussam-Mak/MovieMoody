
# main.py - CLI Controller with improved CLI output

from auth import authenticate
from gemini_api import get_movie_recommendation
from tmdb_api import get_movie_details
from database import init_db, add_movie, get_watchlist, delete_watchlist

def display_movie(movie):
    print("=" * 50)
    print(f"Title: {movie['title']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Rating: {movie['rating']}")
    print(f"Overview: {movie['overview']}")
    print(f"Poster: {movie['poster_url']}")
    print("=" * 50 + "\n")

def main():
    init_db()
    print("=" * 50)
    print("🎬 Welcome to MovieMoody CLI! 🎬")
    print("=" * 50)
    username = authenticate()

    while True:
        print("\nMain Menu:")
        print("1. Get Movie Recommendation")
        print("2. View Watchlist")
        print("3. Clear Watchlist")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            feeling = input("How are you feeling today? ").strip()
            print("\n🔍 Fetching recommendation...")
            recommendation = get_movie_recommendation(feeling)
            print(f"\nGemini recommends: {recommendation}")

            movie_title = recommendation.split('\n')[0].strip()
            movie_details = get_movie_details(movie_title)

            if 'error' not in movie_details:
                display_movie(movie_details)

                save = input("Save this movie to your watchlist? (y/n): ").strip().lower()
                if save == 'y':
                    add_movie(username, movie_details)
                    print("✅ Movie saved to watchlist!")
            else:
                print("❌ Could not find additional movie details on TMDB.")

        elif choice == '2':
            watchlist = get_watchlist(username)
            if watchlist:
                print("\n🎥 Your Watchlist:")
                for idx, movie in enumerate(watchlist, 1):
                    print(f"\nMovie {idx}:")
                    print("=" * 50)
                    print(f"Title: {movie[0]}")
                    print(f"Release Date: {movie[1]}")
                    print(f"Rating: {movie[2]}")
                    print(f"Overview: {movie[3]}")
                    print("=" * 50)
            else:
                print("\nYour watchlist is empty.")

        elif choice == '3':
            delete_watchlist(username)
            print("🗑️ Your watchlist has been cleared.")

        elif choice == '4':
            print("👋 Goodbye! Thanks for using MovieMoody CLI!")
            break
        else:
            print("⚠️ Invalid choice, please select 1-4.")

if __name__ == "__main__":
    main()
