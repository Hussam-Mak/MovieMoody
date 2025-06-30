import google.generativeai as genai


genai.configure(api_key='GEMINI_API')


model = genai.GenerativeModel('gemini-1.5-pro')

def recommend_movie(feeling):
    prompt = f"""
    I am feeling {feeling}. Please recommend me a movie that matches my mood.
    Provide the movie name and a short description of why it's a good match for this feeling.
    """
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    user_feeling = input("How are you feeling today? ")
    movie_recommendation = recommend_movie(user_feeling)
    print("\nRecommended Movie:")
    print(movie_recommendation)
