import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('simple_dict.pkl', 'rb'))
dataset = pd.DataFrame(movies_dict)


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


def recommend(genre, language, str_year, end_year, runtime):
    dic = {"English": "en", "French": "fr",
           "Italian": "it", "German": "de", "Japanese": "ja"}
    df = dataset[dataset['genre'] == genre]
    if language != 'None':
        df = df[df['original_language'] == dic[language]]
    df = df[df['year'] <= end_year]
    df = df[df['year'] >= str_year]
    df['time_diff'] = abs(df['runtime']-runtime)

    chart = df.sort_values(
        ['IMDB_rating', 'time_diff'], ascending=[False, True]).head(10)
    posters = []
    for i in list(chart['imdb_id']):
        posters.append(fetch_poster(i))

    return list(chart['title']), posters


st.title("Simple Movie Recommender System")

category = st.selectbox(
    "Select your favorite genre",
    ('Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Family', 'Fantasy', 'Drama', 'Documentary', 'History', 'Horror', 'Mystery', 'Romance', 'Science Fiction', 'Thriller', 'War'))

language = st.radio(label='Language', options=[
                    'English', 'French', 'Italian', 'German', 'Japanese', 'None'])
st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
optionslst = list(range(1874, 2018))
options = [str(x) for x in optionslst]
range = st.select_slider('Provide a range for release times', options=options, value=('1874','2017'))
str_year = range[0]
end_year = range[1]
# year = str(year)

runtime = st.slider('Set the minimal movie runtime in minutes', 60, 240, 90)

if st.button('Recommend!'):
    # st.write('Hi')
    recommended_movie_names, recommended_movie_posters = recommend(
        category, language, str_year, end_year, runtime)
    print(recommended_movie_names)
    if recommended_movie_names == []:
        st.write('There is no movie, and please try again!')
    else:
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

        col6, col7, col8, col9, col10 = st.columns(5)
        with col6:
            st.text(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
        with col7:
            st.text(recommended_movie_names[6])
            st.image(recommended_movie_posters[6])

        with col8:
            st.text(recommended_movie_names[7])
            st.image(recommended_movie_posters[7])
        with col9:
            st.text(recommended_movie_names[8])
            st.image(recommended_movie_posters[8])
        with col10:
            st.text(recommended_movie_names[9])
            st.image(recommended_movie_posters[9])
