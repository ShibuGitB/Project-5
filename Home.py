import streamlit as st 
from PIL import Image 

def app1() : 
    
    image=Image.open("netflix logo.webp") 
    st.image(image) 
    st.caption("Enjoy The Time Mate!!!"":sparkles:")