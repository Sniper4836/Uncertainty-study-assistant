# Uncertainty-Aware Study Assistant

**README prose word count: approximately 190 words (excluding code and headings).**

## 1. Project Overview

The Uncertainty-Aware Study Assistant is a prototype chatbot designed to explore how AI systems communicate uncertainty when answering user questions.

The project focuses on helping users understand when an answer may be reliable, when more information is needed, and when an answer should be checked against another source.

The application currently uses predefined responses and rule-based keyword matching to simulate different levels of uncertainty.

## 2. Project Status

**Current status: Initial prototype developed.**

The current version includes:
- A web-based chat interface.
- A small predefined knowledge base covering study techniques.
- Low, medium and high uncertainty categories.
- Explanations of why the system assigns each uncertainty level.
- A fallback response for questions outside its knowledge base.

Further improvements are planned, including more effective clarification interactions and additional user feedback and verification options.

## 3. Technology Stack

- **Python:** Main programming language.
- **Streamlit:** Framework used to create the interactive web application.
- **Python IDLE:** Used to write and edit the Python code.
- **GitHub:** Used to store the source code and document project development.

## 4. How to Run the Application

Python must be installed on your computer.

Install Streamlit using:

```bash
python -m pip install streamlit
```

Navigate to the project folder in Command Prompt and run:

```bash
python -m streamlit run app.py
```

The application should open in your web browser.

## 5. Development Record

The initial development stage involved creating a basic chatbot interface, a small knowledge base and a rule-based uncertainty mechanism.

The prototype was tested using questions designed to produce low, medium and high uncertainty responses.

Further development and testing will be documented as the project progresses.

## 6. AI Assistance

ChatGPT was used to support project planning, explain Python and Streamlit concepts, and assist with the initial application code.

The generated code was added to the project and tested by running the application and trying example questions. AI-generated suggestions and code will be reviewed, tested and modified during further development.

## 7. Important Limitations

This is a simulated uncertainty-aware system, not a chatbot with a trained machine-learning model or genuine confidence estimation. Its responses are determined by predefined rules and keyword matching. It does not independently verify factual information.

These limitations will be considered when evaluating the prototype.
