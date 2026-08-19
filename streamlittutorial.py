import streamlit as st
import pandas as pd
import numpy as np
st.title("Helllo GPT")
name = st.text_input("Ask your question")
st.write("This is my first streamlit app")
st.text("let's get started")
name = st.text_input("enter your name")
if st.button("greet"):
    st.success(f"Hello,{name}")
    
upload_file = st.file_uploader("upload a csv",type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)
    st.header("thismis header")
    st.subheader("this is sub header")
    st.markdown("[Link](https://streamlit.io/)")
    st.text_area("write your message")
    st.number_input('pick a number', min_value=0, max_value=10)
    st.slider("choose a range", 0, 100)
    st.selectbox("select a fruit", ["apple", "banana", "chicku"])
    st.multiselect("select language", ["java", "python", "c"])
    st.radio("pick one", ["option A", "option B"])
    st.checkbox("i agree terms & conditions")
if st.checkbox("show details"):
    st.info("here")
    
with st.form("login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    submitted = st.form_submit_button("Login")

    if submitted:
        st.success("Login submitted!") 
        
df = pd.DataFrame(np.random.randn(20, 3),columns=["A", "B", "C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)        

st.video("https://youtu.be/2gcsgfzqN8k?si=21Kr7e-9_Aum9wEc")
st.image("https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1200&q=80",caption="sample image")