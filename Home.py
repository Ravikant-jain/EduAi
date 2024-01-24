import streamlit as st
import pandas as pd

st.write("# Welcome to EduAi! 👋")
tile_data = {
    "subject": ["Math", "English", "Science", "History"],
    "image": [
        "assets/math_icon.png",
        "assets/english_icon.png",
        "assets/science_icon.png",
        "assets/history_icon.png",
    ],
}
df = pd.DataFrame(tile_data)
cols = st.columns(4)
for i, col in enumerate(cols):
    with col:
        st.image(df.loc[i, "image"], width=150)
        st.subheader(df.loc[i, "subject"])