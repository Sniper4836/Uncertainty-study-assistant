
import streamlit as st

st.set_page_config(
    page_title="Uncertainty Study Assistant",
    page_icon="🤖"
)

st.title("🤖 Uncertainty Study Assistant")

st.write(
    "Ask me a study-related question. "
    "I will answer where possible and explain when I am uncertain."
)

# -----------------------------------
# 1. PREDEFINED KNOWLEDGE BASE
# -----------------------------------

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


# -----------------------------------
# 2. PROCESS USER QUESTIONS
# -----------------------------------

def process_question(question):

    question = question.lower()

    # Check whether referencing clarification is needed
    if "referenc" in question or "cit" in question:

        return {
            "type": "clarification",
            "answer": (
                "I can help with referencing, but I need "
                "a little more information first."
            ),
            "uncertainty": "Medium",
            "explanation": (
                "Your question is missing the referencing style."
            )
        }

    # Search the knowledge base
    for topic, information in knowledge_base.items():

        if topic in question:

            return {
                "type": "answer",
                **information
            }

    # If no matching topic is found
    return {
        "type": "answer",
        "answer": (
            "I do not have enough information to answer this "
            "question reliably. Please check your official "
            "study materials or another trusted source."
        ),
        "uncertainty": "High",
        "explanation": (
            "This question does not match any topic in my knowledge base."
        )
    }


# -----------------------------------
# 3. PROCESS CLARIFICATION ANSWERS
# -----------------------------------

def process_clarification(style):

    if style == "Not sure":

        return (
            "That's okay. If you are unsure which referencing style "
            "to use, check your assignment brief or university guidance. "
            "Different modules may require different styles."
        )

    return (
        f"Thanks! You selected {style} referencing. "
        f"I can now give you general guidance specific to {style}. "
        "For accurate formatting, you should still check your "
        "university's official referencing guide."
    )


# -----------------------------------
# 4. INITIALISE SESSION STATE
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_clarification" not in st.session_state:
    st.session_state.pending_clarification = False


# -----------------------------------
# 5. DISPLAY CHAT HISTORY
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------------
# 6. HANDLE CLARIFICATION INTERACTION
# -----------------------------------

if st.session_state.pending_clarification:

    st.write("**Which referencing style are you using?**")

    with st.form("clarification_form"):

        selected_style = st.radio(
            "Select an option:",
            ["Harvard", "APA", "MLA", "Not sure"],
            horizontal=True
        )

        submitted = st.form_submit_button("Submit answer")

        if submitted:

            response = process_clarification(selected_style)

            st.session_state.messages.append({
                "role": "user",
                "content": selected_style
            })

            st.session_state.messages.append({
                "role": "assistant",
                "content": (
                    response
                    + "\n\n**Uncertainty: Low**"
                    + "\n\n**Why?** "
                    + "The user has provided the missing referencing style. "
                    + "The response is still general guidance, not a "
                    + "verified reference-formatting result."
                )
            })

            st.session_state.pending_clarification = False

            st.rerun()


# -----------------------------------
# 7. HANDLE NEW USER QUESTIONS
# -----------------------------------

question = st.chat_input(
    "Ask a study-related question...",
    disabled=st.session_state.pending_clarification
)

if question:

    # Store and display the user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    result = process_question(question)

    # Prepare the assistant response
    response = (
        f'{result["answer"]}'
        f'\n\n**Uncertainty: {result["uncertainty"]}**'
        f'\n\n**Why?** {result["explanation"]}'
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # If clarification is required, activate the interaction
    if result["type"] == "clarification":

        st.session_state.pending_clarification = True

    st.rerun()
