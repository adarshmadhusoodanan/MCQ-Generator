#MCQ generator project
    
import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv() # load all the environment variables from .env file



from openai import OpenAI                      #import OpenAI class from openai package 
OpenAI.api_key = os.getenv("OPENAI_API_KEY")   #fetch the openai key from env file
client = OpenAI()                              #create a object of the class OpenAI


# call openai api for get the questions by passing parameter as text_content and quiz_level that are provided by the user
def fetch_questions(text_content, quiz_level):
    
    #response mcq format
    RESPONSE_JSON = {
        "mcqs" : [
            {
                "mcq": "multiple choice question1",
                "options":{
                    "a": "choice here1",
                    "b": "choice here2",
                    "c": "choice here3",
                    "d": "choice here4",
                },
                "correct": "correct choice option",
            },
            {
                "mcq": "multiple choice question2",
                "options":{
                    "a": "choice here1",
                    "b": "choice here2",
                    "c": "choice here3",
                    "d": "choice here4",
                },
                "correct": "correct choice option",
            },
            {
                "mcq": "multiple choice question3",
                "options":{
                    "a": "choice here1",
                    "b": "choice here2",
                    "c": "choice here3",
                    "d": "choice here4",
                },
                "correct": "correct choice option",
            }
        ]
    }
    # promt for the openai to make MCQ

    PROMPT_TEMPLATE="""
    Text: {text_content}
    You are an expert in generating MCQ type quiz on the basis of provided content.
    Given the above text, create a quiz of 3 multiple choice questions keeping difficulty level as {quiz_level}.
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Ensure to make an array of 3 MCQs referring the following response json.
    Here is the RESPONSE_JSON:

    {RESPONSE_JSON}

    """

    formatted_template = PROMPT_TEMPLATE.format(text_content=text_content, quiz_level=quiz_level,RESPONSE_JSON=RESPONSE_JSON) 

    #make API request
    response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {
                "role":"user",
                "content": formatted_template
            }
        ],
        temperature=0.3,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0                                             
    )

    #Extract response JSON
    extracted_response = response.choices[0].message.content

    print(extracted_response)

    return json.loads(extracted_response).get("mcq",[])


#main method

def main():

    #streamlit is used for the frontent
    st.title("MCQ Generator App")

    #text input for user to paste content
    text_content = st.text_area("Paste the text content here:")

    #Dropdown for selecting quiz level
    quiz_level = st.selectbox("Select MCQ level:",["Easy","Medium","Head"])

    #Convert Quiz level to lower casing
    quiz_level_lower = quiz_level.lower()

    if st.button("Generate MCQ"):
        #define question and options
        questions = fetch_questions(text_content=text_content,quiz_level=quiz_level_lower)

        #Display questions and radio buttons
        selected_options = []
        correct_answers = []
        for question in questions:
            options = list(question["options"].values())
            selected_option = st.radio(question["mcq"], options, index=None)
            selected_options.append(selected_option)
            correct_answers.append(question["options"][question["correct"]])

            #submit button
            if st.button("Submit"):
                #display selected options
                marks = 0
                st.header("Result: ")
                for i, question in enumerate(questions):
                    selected_option = selected_option[i]
                    correct_option = correct_answers[i]

                    st.subheader(f"{question['mcq']}")
                    st.write(f"You selected:{selected_option}")
                    st.write(f"Correct answer:{correct_option}")

                    if selected_option == correct_option:
                        marks +=1
                st.subheader(f"Yow scored {marks} out of {len(questions)}")

if __name__ == "__main__":
    main()




