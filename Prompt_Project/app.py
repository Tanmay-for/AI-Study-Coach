import streamlit as st
import ollama

# Page Configuration (Title and Logo/Icon)
st.set_page_config(page_title="AI Study Coach", page_icon="🎓", layout="centered")

st.title("🎓 AI Study Coach")
st.caption("Your personal prompt-engineered study assistant for exams, concept breakdowns, and quizzes!")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            'role': 'system',
            'content': """You are an expert, highly encouraging AI Study Coach. Your goal is to help students master new subjects, build study schedules, break down complex topics into simple terms, and quiz them effectively.

You operate in three distinct modes based on what the user needs:
1. **Study Planner Mode**: When a user wants to study a subject or prepare for an exam, ask for their timeline and current skill level, then generate a clear, milestone-based study plan.
2. **Topic Breakdown Mode**: When a user asks you to explain a hard concept, use the Feynman Technique—explain it using simple analogies and zero dense jargon.
3. **Quizmaster Mode**: When a user wants to test themselves, ask conceptual or multiple-choice questions one at a time, wait for their answer, and provide constructive feedback.

Always maintain an engaging, supportive tone."""
        },
        {
            'role': 'assistant',
            'content': "Hello! I'm your AI Study Coach. What subject, exam, or goal do you want to work on today? (Are you looking for a study plan, a topic explanation, or a quiz?)"
        }
    ]

# Display prior chat messages (excluding the system prompt)
for message in st.session_state["messages"]:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Handle user input from the chat box at the bottom
if user_input := st.chat_input("Ask your study coach anything..."):
    # Append user message
    st.session_state["messages"].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response from Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(model='llama3.2', messages=st.session_state["messages"])
            reply = response['message']['content']
            st.markdown(reply)
            
    # Append assistant response
    st.session_state["messages"].append({'role': 'assistant', 'content': reply})