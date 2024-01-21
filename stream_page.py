import streamlit as st
from streamlit_webrtc import webrtc_streamer
import requests
import cv2
# from gaze_tracking import GazeTracking


st.set_page_config(layout="wide")

# Fetch transcript (replace with actual URL)
transcript_url = "https://chat.openai.com/share/ad2470f8-6e35-4c71-9034-748126e4b8b5"
transcript_text = requests.get(transcript_url).text

# Main container with grid layout
col1, col2 = st.columns([0.7, 0.3])

# def capture_video():
#     cap = cv2.VideoCapture(0)
#     frame_placeholder = st.empty()
#     attention=[0,0]
#     gaze = GazeTracking()
#     while True:
#         ret, frame = cap.read()
#         if not ret: break

#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         attention[0]+=1
#         _, frame = cap.read()

#         gaze.refresh(frame)
#         frame = gaze.annotated_frame()
#         text = ""

#         if gaze.is_blinking():
#             text = "Blinking"
#         elif gaze.is_right():
#             text = "Looking right"
#         elif gaze.is_left():
#             text = "Looking left"
#         elif gaze.is_center():
#             text = "Looking center"
#             attention[1]+=1

#         cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#         left_pupil = gaze.pupil_left_coords()
#         right_pupil = gaze.pupil_right_coords()
#         cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#         cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#         frame_placeholder.image(frame, channels="RGB", use_column_width=True)
#         # cv2.imshow("Demo", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()

def generate_bot_response(user_input):
        # Replace this with your logic to generate a bot response based on user input
        # You can use language models, chatbot APIs, or custom logic here
        return "I'm still under development, but I'll try my best to respond!"
# Left column for livestream
with col1:
    st.subheader("Livestream")
    st.video(
        "https://www.youtube.com/embed/ErMSHiQRnc8"
    )  # Replace with actual YouTube embed URL


with col2:
    # Chat interface code
    with st.container():
        st.title("Chat Interface")

        # Text area for chat messages
    chat_history = st.empty()

    # Function to append messages to the chat history
    def add_message(message, role):
        with chat_history.container():
            with st.chat_message(role):
                st.markdown(message)

    # User input area
    user_input = st.text_input("Enter your message", key="user_input")

    # Submit button (optional)
    if st.button("Send"):
        # Process user input and generate a response
        bot_response = generate_bot_response(user_input)

        # Add both user and bot messages to the chat history
        add_message(user_input, "user")
        add_message(bot_response, "bot")

        # Clear the input field
        st.session_state.user_input = ""  # Clear the input using session state

        # ... rest of the chat interface code (as provided in the previous response)
    # capture_video()

    

