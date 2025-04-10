import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c993db1b5ee753d94409214b6e9e36b4'.format(movie_id))
    data= response.json()
    return 'https://image.tmdb.org/t/p/w500'+ data['poster_path']


def recommended(movie_name):
    movie_index = movies_list[movies_list["title"]== movie_name].index[0]
    distances= similarity[movie_index]
    top_movies= sorted(list(enumerate(distances)),reverse= True, key= lambda x:x[1])[1:6]

    recommended_movies_names= []
    recommended_movie_posters = []

    for i in top_movies:
        movie_id= movies_list.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies_list.iloc[i[0]].title)
    return recommended_movies_names,recommended_movie_posters


movies_list= pickle.load(open('movies.pkl','rb'))
movies = movies_list["title"].values

similarity= pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")
selected_movie = st.selectbox(
"Select or Type a Movie From Dropdown",
(movies),
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommended(selected_movie)
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
