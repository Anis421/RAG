import streamlit as st
from search import omdb, youtube_trailer

st.title("RAG")

query = st.text_input("Enter a TV show or movie name: ")

if st.button("Search"):
    movie_info = omdb(query)
    trailer_link = youtube_trailer(query)

    st.write("Movie Info")
    st.json(movie_info)

    st.write("Trailer")
    st.markdown(f"[Watch Trailer]({trailer_link})")

