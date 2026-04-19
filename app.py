import streamlit as st
import pickle
import pandas as pd


st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="centered"
)


st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #1f4037, #99f2c8);
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
    }
    .subtitle {
        text-align: center;
        color: #eeeeee;
        font-size: 18px;
    }
    .movie-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<p class="title">🎬 Movie Recommendation System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Find movies similar to your favorite 🎥</p>', unsafe_allow_html=True)


similarity = pickle.load(open("similarity.pkl", 'rb'))
movies = pickle.load(open("movies.pkl", 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_distances = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_distances:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


selected_movie_name = st.selectbox(
    "🎥 Choose a movie you like:",
    movies['title'].values
)


if st.button("✨ Recommend Movies"):
    recommendations = recommend(selected_movie_name)

    st.subheader("🎯 Top Recommendations for You:")

    for movie in recommendations:
        st.markdown(f'<div class="movie-box">🍿 {movie}</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("💡 Built using Streamlit | By Piyush jaiswal")