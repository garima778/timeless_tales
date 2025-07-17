import streamlit as st
from streamlit.components.v1 import html
import base64

st.set_page_config(page_title="Timeless Tales", layout="wide")

# Load background music
def autoplay_bg_music(file_path):
    audio_file = open(file_path, "rb")
    audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio autoplay loop>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Click sound
def click_sound():
    click_audio = open("click.mp3", "rb").read()
    b64 = base64.b64encode(click_audio).decode()
    click_html = f"""
    <audio id="click-sound">
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    <script>
        const buttons = parent.document.querySelectorAll("button");
        buttons.forEach(btn => {{
            btn.addEventListener("click", () => {{
                var audio = parent.document.getElementById("click-sound");
                if(audio) {{
                    audio.play();
                }}
            }});
        }});
    </script>
    """
    html(click_html)

# Initialize session
if "page" not in st.session_state:
    st.session_state.page = "home"
if "name" not in st.session_state:
    st.session_state.name = ""

# Music
autoplay_bg_music("whole_bg.mp3")
click_sound()

# Navigation function
def go(page):
    st.session_state.page = page

# PAGES ----------------------------------

# 1. Home
if st.session_state.page == "home":
    st.image("canva_home.png", use_column_width=True)
    st.audio("starting.mp3")
    if st.button("Begin Your Journey"):
        go("name")

# 2. Name Entry
elif st.session_state.page == "name":
    st.image("canva_name.png", use_column_width=True)
    st.session_state.name = st.text_input("Enter your name to continue:")
    if st.session_state.name:
        if st.button("Continue"):
            go("tale")

# 3. Tale Page
elif st.session_state.page == "tale":
    st.image("canva_tale.png", use_column_width=True)
    st.markdown(f"Welcome, **{st.session_state.name}**.")
    if st.button("Continue to Ganesh Pujan"):
        go("pujan")

# 4. Ganesh Pujan
elif st.session_state.page == "pujan":
    st.video("ganeshpujan.mp4")
    if st.button("Do Puja"):
        st.image("shloka.png", use_column_width=True)
        if st.button("Go Ahead"):
            go("picktale")

# 5. Pick Tale Page
elif st.session_state.page == "picktale":
    st.video("picktale.mp4")
    st.markdown("Choose a tale to continue (feature coming soon!)")
