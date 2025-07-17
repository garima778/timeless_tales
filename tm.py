import streamlit as st
from streamlit.components.v1 import html
import base64

# Set page config
st.set_page_config(page_title="Timeless Tales", layout="wide")

# Function to play background music
def autoplay_bg_music(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Function to play click sound
def play_click_sound():
    with open("click.mp3", "rb") as click:
        b64 = base64.b64encode(click.read()).decode()
        sound_html = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(sound_html, unsafe_allow_html=True)

# Background music (whole bg)
autoplay_bg_music("whole bg.mp3")

# Set up session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Home Page
def show_home():
    st.image("canva_home.png", use_column_width=True)
    if st.button("Begin Your Journey"):
        play_click_sound()
        st.session_state.page = "Name"
        st.rerun()

# Name Page
def show_name():
    st.image("canva_name.png", use_column_width=True)
    name = st.text_input("What shall we call you, traveler?")
    if st.button("Continue"):
        play_click_sound()
        st.session_state.name = name
        st.session_state.page = "Tale"
        st.rerun()

# Tale Page
def show_tale():
    st.image("canva_tale.png", use_column_width=True)
    if st.button("Start with Ganesh Pujan"):
        play_click_sound()
        st.session_state.page = "Ganesh"
        st.rerun()

# Ganesh Pujan Page
def show_ganesh_pujan():
    st.video("ganeshpujan.mp4")
    if st.button("Do Puja"):
        play_click_sound()
        st.image("shloka.png", use_column_width=True)
        if st.button("Go Ahead"):
            play_click_sound()
            st.session_state.page = "Pick Tale"
            st.rerun()

# Pick Tale Page
def show_pick_tale_page():
    st.video("picktale.mp4")
    st.markdown("### Choose Your Tale")
    cols = st.columns(3)
    with cols[0]:
        if st.button("🗺️ Tale 1"):
            play_click_sound()
            st.success("Tale 1 chosen!")
    with cols[1]:
        if st.button("🏹 Tale 2"):
            play_click_sound()
            st.success("Tale 2 chosen!")
    with cols[2]:
        if st.button("🐍 Tale 3"):
            play_click_sound()
            st.success("Tale 3 chosen!")

# Page controller
page = st.session_state.page

if page == "Home":
    show_home()
elif page == "Name":
    show_name()
elif page == "Tale":
    show_tale()
elif page == "Ganesh":
    show_ganesh_pujan()
elif page == "Pick Tale":
    show_pick_tale_page()
