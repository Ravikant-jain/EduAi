import streamlit as st
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
