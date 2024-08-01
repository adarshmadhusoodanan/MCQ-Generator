
# MCQ Generator

This repository contains the code for an MCQ (Multiple Choice Question) Generator using Streamlit, designed to facilitate personalized learning through automated question generation.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Introduction
The MCQ Generator is a web application built with Streamlit that leverages the power of large language models to generate multiple-choice questions. This tool can be used by educators and students to create personalized quizzes and enhance learning experiences.

## Features
- Generate multiple-choice questions from text input
- User-friendly interface built with Streamlit
- Real-time question generation
- Ability to customize the level of questions

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/adarshmadhusoodanan/MCQ-Generator.git
    cd MCQ-Generator
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the GPT-4 model:**
    This project uses the `gpt4free` library. Follow the instructions from the [gpt4free repository](https://github.com/xtekky/gpt4free) to set up the GPT model.

5. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

## Usage
Once the application is running, you can use the web interface to input text and generate multiple-choice questions. 

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter the text or passage from which you want to generate MCQs.
3. Click the "Generate" button to create questions.
4. Customize the level of questions as needed.

## Deployment
The application can be deployed on Streamlit's cloud platform. The live version of the app is available at [MCQ Generator App](https://adarshmadhusoodanan-mcq-generator-main-dmk1ie.streamlit.app/).

![image](https://github.com/user-attachments/assets/1892e0eb-6050-4860-8cb2-1a4242b9157e)


To deploy your own version:

1. **Set up a new repository on GitHub and push your code.**
2. **Create an account on Streamlit and link your GitHub repository.**
3. **Deploy the app directly from the Streamlit dashboard.**

## Acknowledgements
- The `gpt4free` library by [xtekky](https://github.com/xtekky/gpt4free) for providing the GPT model integration.
- Streamlit for their easy-to-use framework for building web applications.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

