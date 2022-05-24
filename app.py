import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


cv = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
cv_matrix = cv.fit_transform(movies['meta'])
alter = cosine_similarity(cv_matrix, cv_matrix)

movies = movies.reset_index()
titles = pd.Series(movies.index, index=movies['title'])



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    if 'poster_path' in data:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path ="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2FEmpty-869097799815349%2Fcommunity&psig=AOvVaw0kHjUuSVKKZjHExWck38lW&ust=1653517580829000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCOjj75GX-fcCFQAAAAAdAAAAABAD"
    return full_path

# recommend function
def recommend(title, n=5, vote = 0):
    idx = titles[title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
    scores = list(enumerate(alter[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    indices = [i[0] for i in scores]
    votes = list(movies['vote_average'].iloc[indices])
    qualified_scores = []
    for i in range(len(votes)):
        if votes[i] >= vote:
            qualified_scores.append(scores[i])
    qualified_scores = qualified_scores[1:n + 1]
    recommended_movies = []
    posters = []
    for i in qualified_scores:
        movie_id = movies.iloc[i[0]].imdb_id
        posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, posters

# app


st.title("Movie Recommender System")

selected_name = st.selectbox(
"Type or select a movie from the dropdown",
movies['title'])

# number = st.number_input('Insert the number of movies of recommendation', step=1)
score = st.number_input('Insert the the minimum score of the movies', min_value=0.0, max_value=10.0)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_name, n=5, vote=score)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
