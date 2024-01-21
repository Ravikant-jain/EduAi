import streamlit as st
import TextAi

st.set_page_config(layout='wide')


# Function to summarize the video (dummy function for example)


# Hardcoded YouTube video URL
yt_url = 'https://www.youtube.com/watch?v=RP2gIgRL6Yw'

@st.cache_data
def AI(yt_url):
    pass


# Streamlit app layout
st.title("Text Ai")

# Create two columns with the specified ratio
col1, col2 = st.columns([0.7, 0.3])

# Left column: YouTube video player
with col1:
    st.video(yt_url)

# Right column: Summarize button and bigger text box
with col2:
    
    X =TextAi.AiText(yt_url)
    st.text_area("Video Trans:",X['Story'], height=400)

    if st.button("Summarize"):
        st.text_area("Video Summary:",X['Summery'], height=400)
