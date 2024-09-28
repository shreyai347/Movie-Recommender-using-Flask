from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from scipy import sparse
from fuzzywuzzy import fuzz, process
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# loading necessary data
file_path = "dataset/"
Train_Data = pd.read_pickle(file_path + "TrainData.pkl")
similarity = pd.read_pickle(file_path + "similarity.pkl")
movie_list = pd.read_csv(file_path + "movies.csv")['title'].values

def fetch_poster(movie_name):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={movie_name}&utf8=1"
    search_response = requests.get(search_url).json()
    
    try: 
        page_title = search_response['query']['search'][0]['title']
        page_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
        
        page_content_url = f"https://en.wikipedia.org/w/api.php?action=parse&page={page_title}&prop=text&format=json"
        content_response = requests.get(page_content_url).json()
        html_content = content_response['parse']['text']['*']
        
        soup = BeautifulSoup(html_content, 'html.parser')
        infobox = soup.find('table', class_='infobox')
        
        if infobox:
            img = infobox.find('img')
            if img:
                poster_path = "https:" + img['src']
                return poster_path
    except (IndexError, KeyError):
        return None
    
    return None

import os

# Add this function to your app.py file
def fetch_trailer(movie_name):
    api_key = "AIzaSyB6UOdwd0mXFKa58fFk3s7hBFgeQlW0jJc"  # Your YouTube Data API key
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie_name} trailer&key={api_key}"
    search_response = requests.get(search_url).json()
    
    if "items" in search_response and len(search_response["items"]) > 0:
        video_id = search_response["items"][0]["id"].get("videoId")
        if video_id:
            return f"https://www.youtube.com/watch?v={video_id}"
    
    return None


def get_recommendations(movie_name):
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_trailers = []
    
    movie_list_in_training = Train_Data.drop_duplicates(subset=["title"], keep="first")[["movieId", "title"]].reset_index(drop=True)
    matches = process.extract(movie_name, movie_list_in_training["title"], scorer=fuzz.partial_ratio)
    
    if len(matches) == 0:
        return ["No Match Found"], [None]
    
    movie_id = movie_list_in_training.iloc[matches[0][2]]["movieId"]
    similarity_scores = similarity[movie_id].toarray().ravel()
    similar_movie_id_list = np.argsort(-similarity_scores)[0:11]
    sm_df = movie_list_in_training[movie_list_in_training["movieId"].isin(similar_movie_id_list)]
    movie_similarity = {movie_id: similarity_scores[movie_id] for movie_id in similar_movie_id_list}
    sorted_movie_ids = sorted(movie_similarity.keys(), key=lambda x: movie_similarity[x], reverse=True)
    
    for movie_id in sorted_movie_ids[1:]:
        recommended_movie_names.append(sm_df[sm_df["movieId"] == movie_id]["title"].values[0])
        poster = fetch_poster(recommended_movie_names[-1])# Call fetch_poster here
        trailer = fetch_trailer(recommended_movie_names[-1])  # Fetch trailer
        recommended_movie_posters.append(poster if poster is not None else 'static/notfound.png')  # Handle None
        recommended_movie_trailers.append(trailer) 
        
        if len(recommended_movie_names) >= 10:
            break
    
    return recommended_movie_names, recommended_movie_posters, recommended_movie_trailers

# Home route to display the search form
@app.route('/')
def index():
    return render_template('index.html', movie_list =  movie_list)

# Route to handle the recommendation
@app.route('/recommend', methods=['POST'])
def recommend_route():
    movie_name = request.form.get('movie_name')
    recommended_movie_names, recommended_movie_posters, recommended_movie_trailers = get_recommendations(movie_name)
    
    if recommended_movie_names[0] == "No Match Found":
        return render_template('no_output.html', movie_name=movie_name)
    
    movies = zip(recommended_movie_names, recommended_movie_posters, recommended_movie_trailers)
    return render_template('recommendations.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True)