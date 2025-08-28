import streamlit as st
st.title("Mi primera App")
image = Image.open('gumball.jpg')
st.image(image,caption= 'gumball')
