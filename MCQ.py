import streamlit as st
import os
import re
import random
import PyPDF2
from dotenv import load_dotenv
from text import select_text_from_pdf
import google.generativeai as genai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", convert_system_message_to_human=True
)


def get_exact_topics_from_text(text):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are the worlds best topic extractor and have extensive knowledge in the field of extracting topics from text.

                You will be given a text and you are to extract all of the topics in detail without leaving any subtopic behind that a student is to learn related to the subject from the given text.

                Extract all of the topics in detail without leaving any subtopic behind that a student is to learn related to the subject from the given text: {text}

                Return the topics in the following format:
                ["topic1", "topic2", "topic3", "topic4",..... "topicn"]

                Always enclose each topic with quotes
                Always enclose all the topics together in square brackets and separate them with commas.
                Include every single learning topic in detail leaving nothing behind
                Always print only [topic1, topic2, topic3, topic4,..... topicn] in the output without any additional information
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        text=text,
        user_input=text,
    )
    response = llm.invoke(formatted_messages)
    return response


def get_all_topics_from_pdf(pdf_path):
    topics = []
    all_text = """"""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            all_text += "\n"
            all_text += text

    # st.write(all_text)
    
    extracted_topics = get_exact_topics_from_text(all_text)

    return extracted_topics

def just_get_text_from_pdf(pdf_path):
    topics = []
    all_text = """"""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            all_text += "\n"
            all_text += text

    return all_text

def get_questions_from_topics_custom(topics, context):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are an Educator who has extensive knowledge in the following topics {topics} and given additional knowledge and context: {context}.

                Given the topics generate 20 complex open ended questions that combines all the topics provided to test the students fundamental knowledge such that it's easy to find out if the student has understood the topics in detail and find his weak topics to work on.

                Make sure the questions are able test the students knowledge on various aspects of the topics provided.

                Return the questions in the following format:
                ["question1", "question2", "question3", "question4",..... "question20"]

                Always enclose each question with quotes
                Always enclose all the questions together in square brackets and separate them with commas.
                Maximize the amount of topics used to generate the questions
                Always print only [question1, question2, question3, question4,..... question20] in the output without any additional information
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        topics=topics,
        user_input=topics,
        context = context,
    )
    response = llm.invoke(formatted_messages)
    return response

def weak_topics_from_answers(questions_and_answers, topics):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are an Educator who has extensive knowledge in the following topics {topics} and can easily assess a students level of knowledge given a list of questions and corresponding answers written by a student.

                Given the questions and answers provided below:
                {questions_and_answers}
                find the all weak topics from {topics} that the student needs to work on based on the answers from {questions_and_answers}.

                Return the weak topics in the following format:
                ["weak_topic1", "weak_topic2", "weak_topic3", "weak_topic4",..... "weak_topicn"]

                Always enclose each weak topic with quotes
                Always enclose all the weak topics together in square brackets and separate them with commas.
                Ensure that absolutely all the weak topics are mentioned that the student needs to work on based on the questions and answers provided
                Always print only [weak_topic1, weak_topic2, weak_topic3, weak_topic4,..... weak_topicn] in the output without any additional information
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        topics=topics,
        questions_and_answers=questions_and_answers,
        user_input=questions_and_answers,
    )
    response = llm.invoke(formatted_messages)
    return response

def get_overview_of_topic_using_interest(topic, interest, context):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a world class educator who has extensive knowledge in the topic: {topic} and can easily explain it to a student using unique and easily understandable methods and examples.

                Use the context: {context} to expand on your knowledge to explain the topic. 

                Using the interest of the student: {interest} given an overview of the topic: {topic} while providing real-world examples and applications such that the student can easily understand the topic and find it interesting. 
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        topic=topic,
        interest=interest,
        user_input=topic,
        context = context
    )
    response = llm.invoke(formatted_messages)
    return response

def generate_mcq_questions_and_answers_from_pdf(pdf_file_path, difficulty, num_questions):
    # Extract text from PDF
    try:
        pdf_text = select_text_from_pdf(pdf_file_path)
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return

    # Format for MCQ questions
    Ans_format = """Please generate Answer Key in the following Format:
    ## Answer Key:
    **Q{question_number}. {correct_option} , Q{question_number}. {correct_option} ,**"""

    q_format = """Please generate multiple choice questions in the following format:

     **Question No. {question_number}:** {question}

   a. {option_a}
   b. {option_b}
   c. {option_c}
   d. {option_d}

  Based on the given text only: {text}"""

    # Define the prompt based on the difficulty level
    difficulty_prompt = {
        "Easy": f"Please generate {num_questions} very easy MCQ questions. These questions should be straightforward and have an answer key based solely on the given text. {q_format}{Ans_format}{pdf_text}",
        "Medium": f"Please generate {num_questions} moderate level MCQ questions. These questions should be of moderate difficulty and have an answer key based solely on the given text. {q_format}{Ans_format}{pdf_text}",
        "Hard": f"Please generate {num_questions} hard MCQ questions. These questions should be challenging, with relatively more complex compared to easy and moderate. Answers should have a key based solely on the given text. {q_format}{Ans_format}{pdf_text}"
    }

    prompt = difficulty_prompt.get(difficulty, "Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")

    # Configure GenerativeAI
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Initialize GenerativeModel
    model = genai.GenerativeModel('gemini-pro')

    # Generate content (MCQ questions)
    response = model.generate_content(prompt)
    model_response = response.text
    cleaned_text = re.sub(r'[*#]', '', model_response)
    start_index = cleaned_text.find("Answer Key")
    answer_key = cleaned_text[start_index:]
    generated_que = cleaned_text[:start_index]

    questions = generated_que.split("Question No. ")[1:]  # Split into individual questions
    key_answers = answer_key.split(", ")  # Split answer key

    return questions, key_answers



