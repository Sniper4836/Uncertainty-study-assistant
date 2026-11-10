
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Uncertainty Study Assistant",
    page_icon="🤖"
)

st.title("🤖 Uncertainty Study Assistant")

st.write(
    "Ask me a study-related question. "
    "I will answer where possible and explain when I am uncertain."
)

# Our small knowledge base
knowledge_base = {
    "active recall": {
        "answer": (
            "Active recall is a study technique where you actively "
            "try to remember information without looking at your notes. "
            "For example, you could use flashcards or test yourself."
        ),
        "uncertainty": "Low",
        "explanation": (
            "Your question matches a topic in my knowledge base."
        )
    },

    "spaced repetition": {
        "answer": (
            "Spaced repetition involves reviewing information at "
            "increasing intervals over time. This can help improve "
            "long-term memory."
        ),
        "uncertainty": "Low",
        "explanation": (
            "Your question matches a topic in my knowledge base."
        )
    },

    "pomodoro": {
        "answer": (
            "The Pomodoro Technique involves studying for a focused "
            "period, commonly 25 minutes, followed by a short break."
        ),
        "uncertainty": "Low",
        "explanation": (
            "Your question matches a topic in my knowledge base."
        )
    }
}


# Function to process questions
def process_question(question):

    question = question.lower()

    # Check for ambiguous referencing questions
    if "referenc" in question or "cit" in question:
        return {
            "answer": (
                "I can help with referencing, but I need to know "
                "which referencing style you are using."
            ),
            "uncertainty": "Medium",
            "explanation": (
                "Your question is missing important context."
            )
        }

    # Check whether the question matches our knowledge base
    for topic, information in knowledge_base.items():

        if topic in question:
            return information

    # If no match is found
    return {
        "answer": (
            "I do not have enough information to answer this question "
            "reliably. Please check your official study materials "
            "or another trusted source."
        ),
        "uncertainty": "High",
        "explanation": (
            "This question does not match any topic in my knowledge base."
        )
    }


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Accept a new question
question = st.chat_input("Ask a study-related question...")

if question:

    # Display user's question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Process the question
    result = process_question(question)

    # Create the chatbot response
    response = (
        f'{result["answer"]}\n\n'
        f'**Uncertainty: {result["uncertainty"]}**\n\n'
        f'**Why?** {result["explanation"]}'
    )

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
