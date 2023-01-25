import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sherzod Akramov")
    content = """
Hi, I am Sherzod! I am a Python programmer, learner. I graduated in 2022 Tashkent University of 
Information Technologies with a degree bachelor of programmer-engineering. I worked at company "Digital World" LLC
in Tashkent for a several months. There I have been working as a Python and Django intern-developer, and keep 
learning Python, Django, Django Rest Framework, Sql and etc.  
"""
    st.info(content)
