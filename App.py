import streamlit as st
import random

# Behtar Knowledge Base: Isme hum ek hi jawab ke liye multiple keywords set kar rahe hain
knowledge_base = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "namaste", "salam"],
        "responses": ["Hello! Welcome to BCA Support Chatbot. How can I help you?", "Hi there! What can I do for you today?"]
    },
    "fees": {
        "keywords": ["fee", "fees", "paisa", "cost", "charge", "amount"],
        "responses": ["The fee structure for BCA is approximately ₹40,000 per year.", "BCA costs around ₹40,000/year, and MCA is ₹55,000/year."]
    },
    "courses": {
        "keywords": ["course", "courses", "stream", "subject", "branch", "padhai"],
        "responses": ["We offer BCA, MCA, and B.Sc. Computer Science courses.", "Currently, admissions are open for BCA and MCA."]
    },
    "duration": {
        "keywords": ["duration", "year", "years", "time", "semester", "sem"],
        "responses": ["BCA is a 3-year undergraduate degree program divided into 6 semesters."]
    },
    "admission": {
        "keywords": ["admission", "apply", "form", "seat", "join"],
        "responses": ["You can apply online through the college official portal or visit the campus admission cell directly."]
    }
}

# UI Setup
st.set_page_config(page_title="BCA Inquiry Chatbot", page_icon="🤖")
st.title("🤖 BCA College Inquiry Chatbot")
st.write("Ask me anything about BCA courses, fees, or admission!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input("Type your question here..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    clean_input = user_input.lower().strip()
    bot_response = "Sorry, I am not trained for this question yet. Try asking about fees, courses, or admission."
    
    # Naya Intelligent Matching Logic
    found = False
    for category, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in clean_input:  # Agar user ke message me koi bhi keyword match hua
                bot_response = random.choice(data["responses"])
                found = True
                break
        if found:
            break

    with st.chat_message("assistant"):
        st.write(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})