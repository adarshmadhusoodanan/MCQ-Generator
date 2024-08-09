import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables from .env file

from g4f.client import Client

client = Client()

# Call OpenAI API to get the questions by passing parameter as text_content and quiz_level provided by the user
@st.cache_data  # Don't want to call OpenAI each time when the Streamlit page is refreshed
def fetch_questions(text_content, quiz_level):
    # Response MCQ format
    RESPONSE_JSON = {
        "mcqs": [
            {
                "mcq": "multiple choice question",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here",
                },
                "correct": "correct choice option",
            },
            {
                "mcq": "multiple choice question",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here",
                },
                "correct": "correct choice option",
            },
            {
                "mcq": "multiple choice question",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here",
                },
                "correct": "correct choice option",
            }
        ]
    }

    # Prompt for OpenAI to make MCQ
    PROMPT_TEMPLATE = """
    Text: {text_content}
    You are an expert in generating MCQ type quiz on the basis of provided content.
    Given the above text, create a quiz of 3 multiple choice questions keeping difficulty level as {quiz_level}.
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Ensure to make an array of 3 MCQs referring the following response json.
    Here is the RESPONSE_JSON:

    {RESPONSE_JSON}
    """

    formatted_template = PROMPT_TEMPLATE.format(text_content=text_content, quiz_level=quiz_level, RESPONSE_JSON=json.dumps(RESPONSE_JSON))

    # Make API request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": formatted_template}],
        # temperature=0.3,
        # max_tokens=1000,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0
    )

    # Print the entire API response for debugging
    print("API Response:", response)

    if not response or not response.choices:
        st.error("Empty response from API")
        return []

    extracted_response = response.choices[0].message.content.strip()

    print("Extracted Response:", extracted_response)  # Debugging: Print the raw response

    # Extract the JSON part of the response
    try:
        json_start_index = extracted_response.find('{')
        json_end_index = extracted_response.rfind('}') + 1
        json_str = extracted_response[json_start_index:json_end_index]

        return json.loads(json_str).get("mcqs", [])
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return []


# Main method
def main():
    st.title("MCQ Generator App")

    # Text input for user to paste content
    text_content = st.text_area("Paste the text content here:")

    # Dropdown for selecting quiz level
    quiz_level = st.selectbox("Select MCQ level:", ["Easy", "Medium", "Hard"])

    # Convert Quiz level to lower casing
    quiz_level_lower = quiz_level.lower()

    # Initialize session_state
    session_state = st.session_state

    # Check if quiz_generated flag exists in session_state, if not initialize it
    if 'quiz_generated' not in session_state:
        session_state.quiz_generated = False

    # Track if Generate Quiz button is clicked
    if not session_state.quiz_generated:
        session_state.quiz_generated = st.button("Generate MCQ")

    if session_state.quiz_generated:
        # Define question and options
        questions = fetch_questions(text_content=text_content, quiz_level=quiz_level_lower)

        # Display questions and radio buttons
        selected_options = []
        correct_answers = []
        for question in questions:
            options = list(question["options"].values())
            selected_option = st.radio(question["mcq"], options, index=None)
            selected_options.append(selected_option)
            correct_answers.append(question["options"][question["correct"]])

        # Submit button
        if st.button("Submit"):
            # Display selected options
            marks = 0
            st.header("Result:")
            for i, question in enumerate(questions):
                selected_option = selected_options[i]
                correct_option = correct_answers[i]

                st.subheader(f"{question['mcq']}")
                st.write(f"You selected: {selected_option}")
                st.write(f"Correct answer: {correct_option}")

                if selected_option == correct_option:
                    marks += 1
            st.subheader(f"You scored {marks} out of {len(questions)}")


if __name__ == "__main__":
    main()
