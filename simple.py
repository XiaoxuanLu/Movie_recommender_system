import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


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


def get_recommendation_chart(genre, language='en', year='2017', runtime=90):
    df = gen_md[gen_md['genre'] == genre]
    df = df[df['original_language'] == language]
    df = df[df['year'] == year]
    C = df['vote_average'].mean()
    m = df['vote_count'].quantile(0.85)

    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull())][[
        'id', 'title', 'original_language', 'year', 'runtime', 'vote_count', 'vote_average', 'imdb_id']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['runtime'] = qualified['runtime'].astype('int')
    qualified['time_diff'] = abs(qualified['runtime']-runtime)

    qualified['IMDB_rating'] = qualified.apply(lambda x: (
        x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified['IMDB_rating'] = qualified['IMDB_rating'].round(decimals=1)
    chart = qualified.sort_values(
        ['IMDB_rating', 'time_diff'], ascending=[False, True]).head(10)

    return chart['title']


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