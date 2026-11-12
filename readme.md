# Uncertainty-Aware Study Assistant

**README prose word count: approximately 275 words (excluding headings, code and file names).**

## Project Overview

The Uncertainty-Aware Study Assistant is an interactive chatbot prototype designed to explore how AI systems can communicate uncertainty and help users make informed decisions about whether to trust an answer.

The system responds to study-related questions using a predefined knowledge base and communicates uncertainty through three categories: Low, Medium and High.

## Project Status

**Status: Functional prototype developed.**

The prototype includes the following features:

- **Uncertainty indicators:** Displays colour-coded low, medium and high uncertainty categories.
- **Clarification:** Requests additional information when a question is ambiguous.
- **Further explanation:** Allows users to request more detailed information about an answer.
- **Challenge responses:** Allows users to challenge an answer and receive advice about independently verifying the information.
- **Chat interface:** Maintains conversation history during the session.

## Technology Stack

- Python
- Streamlit
- Python IDLE
- GitHub

## How to Run

1. Install Python.
2. Install Streamlit using:

   `python -m pip install streamlit`

3. Navigate to the project folder.
4. Run the application using:

   `python -m streamlit run app.py`

5. Open the local URL provided by Streamlit in your browser.

## System Design and Limitations

The application uses Python-based keyword matching to identify questions and retrieve predefined responses from a small knowledge base.

Uncertainty categories are assigned using predefined rules. They do not represent genuine AI confidence scores or a trained machine learning model.

The system cannot independently verify factual accuracy, and its responses are limited to the information included in its knowledge base.

## Development Record

The project was developed incrementally, beginning with a basic chatbot and predefined knowledge base. Further development introduced uncertainty indicators, clarification requests, expandable explanations and user challenges.

The application was tested using example questions to check its responses and interactive functionality.

## AI Assistance

ChatGPT was used to support project planning, explain Python and Streamlit functionality, and assist with developing and improving sections of the application code.

Generated code and suggestions were reviewed, implemented and tested during development. The final implementation was checked through interaction with the application.

AI was not used for any planning or writing of the final report.

## Repository Contents

- `app.py` – Main application code.
- `requirements.txt` – Python dependencies.
- `.gitignore` – Files excluded from version control.
- `README.md` – Project documentation.
