import streamlit as st

import streamlit.components.v1 as components

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('D2C15DDC-4A94-4AC5-8A6C-DF8F6D571B90_1_105_c.jpeg')    

st.title("Edficio Cruzeiro")
st.header("Plantas dos Apartamentos")
col1, col2, col3 = st.columns(3)
with col3:
   st.header("Apartamento T1 RC DTO")
   st.image("T1 RC DTO.PNG.png")

with col2:
   st.header("Apartamento T1 RC FTE")
   st.image("T1 RC FTE.png")

with col1:
   st.header("Apartamento T1 RC ESQ")
   st.image("T3 RC ESQ.png")

col1, col2, col3 = st.columns(3)
with col1:
   st.header("Apartamento T1 RC ESQ")
   st.image("T1 RC DTO.PNG.png")

with col2:
   st.header("Apartamento T1 RC Dto")
   st.image("T1 RC FTE.png")

with col3:
   st.header("Apartamento T1 RC Dto")
   st.image("T3 RC ESQ.png")


video_file = open('video4.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

col1, col2 = st.columns(2)
with col1:
   st.header("Pornenores da Construção")
   st.image("")

with col2:
   st.header("Quarto Com Suite")
   st.image("")

col1, col2 = st.columns(2)
with col1:
   st.header(" Varanda Panoramica")
   st.image("")
with col2:
   st.header("Exceentes Acabamentos")
   st.image("")

col1, col2 = st.columns(2)
with col1:
   st.header("Apartamento T1 RC ESQ")
   components.iframe("https://v3d.net/oeh", width=350, height=300)
   st.markdown(components.iframe, unsafe_allow_html=True)

with col2:
   st.header("Apartamento T1 RC Dto")
   components.iframe("https://v3d.net/oi0", width=350, height=300)
   st.markdown(components.iframe, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
   st.header("Apartamento T1 RC ESQ")
   components.iframe("https://v3d.net/o4m", width=350, height=300)
   st.markdown(components.iframe, unsafe_allow_html=True)

with col2:
   st.header("Apartamento T1 RC Dto")
   components.iframe("https://v3d.net/oei", width=350, height=300)
   st.markdown(components.iframe, unsafe_allow_html=True)





