
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

st.caption(
    "This prototype uses simulated uncertainty categories, "
    "not genuine AI confidence scores."
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
        ),
        "further_explanation": (
            "Active recall works by making you retrieve information "
            "from memory rather than simply reading it again. "
            "For example, after studying a lecture, close your notes "
            "and try to write down everything you can remember. "
            "You can then compare your answer with your notes "
            "to identify gaps in your understanding."
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
        ),
        "further_explanation": (
            "Instead of studying the same information repeatedly "
            "in one session, spaced repetition spreads revision "
            "across multiple sessions. For example, you might review "
            "a topic today, again tomorrow, then after several days "
            "and eventually after a week. This helps you revisit "
            "information over time."
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
        ),
        "further_explanation": (
            "A typical Pomodoro session involves studying for "
            "25 minutes without distractions, followed by a "
            "5-minute break. After completing four sessions, "
            "you take a longer break. The idea is to divide "
            "large tasks into manageable periods of focused work."
        )
    }
}


# -----------------------------------
# 2. PROCESS USER QUESTIONS
# -----------------------------------

def process_question(question):

    question = question.lower()

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
            ),
            "further_explanation": None
        }

    for topic, information in knowledge_base.items():

        if topic in question:

            return {
                "type": "answer",
                **information
            }

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
        ),
        "further_explanation": (
            "My knowledge base currently contains information about "
            "active recall, spaced repetition and the Pomodoro Technique. "
            "I cannot confidently answer questions outside these topics. "
            "You could try asking about one of these topics or consult "
            "your lecture materials for information about this subject."
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
# 4. DISPLAY ASSISTANT RESPONSES
# -----------------------------------

def display_assistant_message(message):

    st.markdown(message["content"])

    uncertainty = message.get("uncertainty", "High")
    explanation = message.get("explanation", "")

    if uncertainty == "Low":

        st.success("🟢 LOW UNCERTAINTY")

    elif uncertainty == "Medium":

        st.warning("🟠 MEDIUM UNCERTAINTY")

    else:

        st.error("🔴 HIGH UNCERTAINTY")

    if explanation:

        st.caption("Why? " + explanation)


# -----------------------------------
# 5. INITIALISE SESSION STATE
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_clarification" not in st.session_state:
    st.session_state.pending_clarification = False


# -----------------------------------
# 6. DISPLAY CHAT HISTORY
# -----------------------------------

for i, message in enumerate(st.session_state.messages):

    with st.chat_message(message["role"]):

        if message["role"] == "assistant":

            if "uncertainty" in message:

                display_assistant_message(message)

                # Show the further explanation button
                if message.get("further_explanation"):

                    if st.button(
                        "Explain further",
                        key=f"explain_{i}"
                    ):

                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": message["further_explanation"],
                            "uncertainty": message["uncertainty"],
                            "explanation": (
                                "This is additional information based "
                                "on the same knowledge base entry."
                            ),
                            "further_explanation": None
                        })

                        st.rerun()

            else:

                st.markdown(message["content"])

        else:

            st.markdown(message["content"])


# -----------------------------------
# 7. HANDLE CLARIFICATION INTERACTION
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
                "content": response,
                "uncertainty": "Medium",
                "explanation": (
                    "The referencing style is now known, but this is "
                    "general guidance rather than a verified reference."
                ),
                "further_explanation": None
            })

            st.session_state.pending_clarification = False

            st.rerun()


# -----------------------------------
# 8. HANDLE NEW USER QUESTIONS
# -----------------------------------

question = st.chat_input(
    "Ask a study-related question...",
    disabled=st.session_state.pending_clarification
)

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    result = process_question(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "uncertainty": result["uncertainty"],
        "explanation": result["explanation"],
        "further_explanation": result["further_explanation"]
    })

    if result["type"] == "clarification":

        st.session_state.pending_clarification = True

    st.rerun()
