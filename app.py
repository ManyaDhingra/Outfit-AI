import streamlit as st
from PIL import Image
from clip_utils import classify_outfit
from llm_utils import generate_response

st.set_page_config(page_title="Outfit AI", page_icon="👗")

st.title("👗 Outfit AI")

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "analysis" not in st.session_state:
    st.session_state.analysis = None

# ---------------- SIDEBAR ----------------
st.sidebar.header("Upload Outfit Image (Optional)")

uploaded_file = st.sidebar.file_uploader(
    "Upload image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.sidebar.image(
        image,
        caption="Uploaded Outfit",
        use_container_width=True
    )

    if st.session_state.analysis is None:
        with st.spinner("Analyzing outfit..."):
            st.session_state.analysis = classify_outfit(image)

# ---------------- CHAT ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- INPUT ----------------
user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = generate_response(
                user_input,
                st.session_state.analysis,
                st.session_state.messages
            )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )