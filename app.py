import streamlit as st
from chatbot import generate_response


st.set_page_config(page_title="Caprice's Chatbot")


st.markdown(
    """
    <h1 style="text-align:center; color:#6C63FF;">
        Caprice's AI Bestie Chatbot
    </h1>
    <p style="text-align:center; color:#555;">
        Ask me anything about Python or coding!
    </p>
    """,
    unsafe_allow_html=True,
)


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "You are a kind, patient Python tutor who explains things simply.",
        }
    ]


for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])


prompt = st.chat_input("your question here...")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)


    reply = generate_response(st.session_state["messages"])


    st.session_state["messages"].append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)
