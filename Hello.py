'''import streamlit as st
import live
# Set page config at the beginning of the main script
st.set_page_config(layout="wide")

# Create Navigation Bar with unique keys for radio buttons
st.header("Navigation Bar")
col1, col2, col3 = st.columns(3)

with col1:
    selected_page = st.radio("", ("Live",), key="live_radio")
with col2:
    selected_page = st.radio("", ("Video",), key="video_radio")
with col3:
    selected_page = st.radio("", ("Resources",), key="resources_radio")

# Update session state and display content
if "page" not in st.session_state:
    st.session_state.page = "Live"  # Set default page

if selected_page:
    st.session_state.page = selected_page

if st.session_state.page == "Live":
    live.main()  # Call the main function of live.py
elif st.session_state.page == "Video":
    live.main()  # Call the main function of video.py
elif st.session_state.page == "Resources":
    live.main()  # Call the main function of resources.py
'''

import streamlit as st
import pandas as pd  # For creating a DataFrame to hold tile data (optional)

st.write("# Welcome to EduAi! 👋")
# st.set_page_config(page_title="Hello",page_icon="👋")

# Create a DataFrame to organize tile data
tile_data = {
    "subject": ["Math", "English", "Science", "History"],
    "image": ["math_icon.png", "english_icon.png", "science_icon.png", "history_icon.png"]  # Replace with your image filenames
}
df = pd.DataFrame(tile_data)

# Use st.columns to create 4 equally-spaced columns for the tiles
cols = st.columns(4)

# Iterate through the tile data (or create tiles manually)
for i, col in enumerate(cols):
    with col:
        # Display tile content
        st.image(df.loc[i, "image"], width=150)  # Adjust image size as needed
        st.subheader(df.loc[i, "subject"])




# st.sidebar.success("Select a demo above.")