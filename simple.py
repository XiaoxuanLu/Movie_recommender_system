import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    if 'poster_path' in data:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2FEmpty-869097799815349%2Fcommunity&psig=AOvVaw0kHjUuSVKKZjHExWck38lW&ust=1653517580829000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCOjj75GX-fcCFQAAAAAdAAAAABAD"
    return full_path


st.title("Movie Recommender Simple System")

category = st.selectbox(
    "What's your favorite movie category",
    ('Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Family', 'Fantasy', 'Drama', 'Documentary', 'History', 'Horror', 'Mystery', 'Romance', 'Science Fiction', 'Thriller', 'War'))

language = st.radio(label='Language', options=[
                    'English', 'French', 'Italian', 'German', 'Japanese', 'Others'])
st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
year = st.slider('The year of the movie', 1874, 2017, 2017)

runtime = st.slider('The runtime of the movie in minutes', 60, 240, 90)

if st.button('Recommend!'):
    st.write('Hello')
