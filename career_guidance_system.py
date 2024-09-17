import requests
import json

# Define the Gemini API endpoint and your API key (replace 'YOUR_API_KEY' with your actual key)
api_url = 'https://generativelanguage.googleapis.com/v1beta/models/*:generateContent'
api_key = 'YOUR_API_KEY'

def get_user_profile():
    """Function to collect user data for career recommendations"""
    user_profile = {
        "name": "John Doe",
        "aptitudes": ["problem-solving", "critical thinking"],
        "aspirations": ["leadership", "technology"],
        "abilities": ["Python programming", "data analysis"],
        "experiences": ["internship in AI", "project management"]
    }
    return user_profile

def generate_career_recommendations(user_profile):
    """Function to generate personalized career recommendations using Gemini API"""
    prompt = (
        f"Based on the following user profile: Aptitudes: {', '.join(user_profile['aptitudes'])}, "
        f"Aspirations: {', '.join(user_profile['aspirations'])}, "
        f"Abilities: {', '.join(user_profile['abilities'])}, "
        f"and Experiences: {', '.join(user_profile['experiences'])}, "
        "please provide personalized career recommendations."
    )
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    request_body = {
        "model": "models/career-recommender",
        "prompt": prompt
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(request_body))
    
    if response.status_code == 200:
        result = response.json()
        return result.get('content', 'No recommendation available')
    else:
        return f"Error: {response.status_code} - {response.text}"

def display_recommendations(recommendations):
    """Function to display recommendations"""
    print("Personalized Career Recommendations:")
    print(recommendations)

if __name__ == "__main__":
    user_profile = get_user_profile()
    recommendations = generate_career_recommendations(user_profile)
    display_recommendations(recommendations)
