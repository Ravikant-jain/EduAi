import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(layout='wide')

def render_pdf(file_path):
    doc = fitz.open(file_path)
    num_pages = doc.page_count

    # Initialize or get the conversation history
    conversation_history_resource = st.session_state.get('conversation_history', [])
    
    par_c1, par_c2, par_c3 = st.columns([3, 1, 2])

    with par_c1:
        page_number = st.session_state.get('page_number', 1)
        page = doc.load_page(page_number - 1)
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
        if col1.button("Previous Page") and page_number > 1:
            st.session_state.page_number -= 1
        if col4.button("Next Page") and page_number < num_pages:
            st.session_state.page_number += 1
        image_bytes = page.get_pixmap().tobytes()
        st.image(image_bytes, use_column_width=True)

    with par_c3:
        st.title("Chat with AI")
        user_input = st.text_input("You:", key="user_input")

        if st.button("Send"):
            # You can replace this with your AI model or service for generating responses
            ai_response = "AI: Hello! I'm a simple AI"
            conversation_history_resource.append(f"You: {user_input}")
            conversation_history_resource.append(ai_response)
            st.session_state.conversation_history_resource = conversation_history_resource
        conversation_text = "\n".join(conversation_history_resource)
        st.text_area("Conversation:", value=conversation_text, height=400, key="conversation_area")

def main():
    render_pdf(r"C:\Users\rudra\Downloads\rdpd.pdf")

if __name__ == "__main__":
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history_resource = []
    main()
