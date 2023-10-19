import streamlit as st

st.set_page_config(page_title="Globalize Email",page_icon=":robot:")
st.header("My Header")

col1,col2,col3=st.columns(3)

with col1:
    st.write("col1")

with col2:
    st.write("col2")

with col3:
    st.write("col3")
    st.markdown("## Column 3")

st.write(1+2)
input_text=st.text_area(label="",placeholder="Your Email...",key="email_input")
if input_text:
    st.write("Now there is user input text:")
    st.write(input_text)