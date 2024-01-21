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