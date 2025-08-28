import streamlit as st
from PIL import Image
st.title("Mi primera App")
image = Image.open('gumball.jpg')
st.image(image,caption= 'gumball')
