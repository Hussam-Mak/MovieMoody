
# auth.py - Simulated GitHub OAuth (for CLI simplicity)

def authenticate():
    print("Please log in with your GitHub username.")
    username = input("GitHub Username: ").strip()
    return username
