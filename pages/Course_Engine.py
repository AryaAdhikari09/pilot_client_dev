import streamlit as st
import asyncio
import aiohttp
import subprocess
import os
import re
import time
import requests
import faiss
import numpy as np
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from datetime import datetime
import requests
import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.set_page_config(page_title="Course Engine", page_icon=":books:")


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")
    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        if st.session_state.get("logged_in", False):
            
            col1, col2 = st.columns([2, 1])  # Adjust the ratio as needed
            
            with col1:
                # st.header("!")
                st.header(f"Hi {st.session_state.email}!")

            with col2:
                if st.button("Logout", key="logout_button_home"):
                    logout()
            
            st.write("---") 

            # st.write("---")   

            # st.header("Navigation")
            nav_buttons = [
                ("Home", "pages/home.py"),
                ("Course Engine", "pages/Course_Engine.py"),
                ("Project Engine", "pages/Project_Engine.py"),
                ("Research Mate", "pages/Research_Mate.py"),
                ("Curriculum Analyser", "pages/Curriculum_Analyser.py"),
                ("Curriculum Helper", "pages/Curriculum_Helper.py"),
                ("History", "pages/history.py")
            ]
            for label, page in nav_buttons:
                if st.button(label, key=f"{label.lower().replace(' ', '_')}_button_home"):
                    st.switch_page(page)

            st.write("---")


        elif get_current_page_name() != "login":
            st.switch_page("login.py")


def login_button():
    if st.button("Login", key="sdfsdfsdfsdfsdggfth"):
        st.session_state.logged_in = False

        st.switch_page("login.py")


def logout():
    st.session_state.logged_in = False
    st.session_state.token = None
    st.session_state.email = ""
    st.info("Logged out successfully!")

    st.switch_page("login.py")


make_sidebar()


def bruh(email, module, user_flow_choice, career_choice):
    BASE_URL = "https://pilot-server-12yj.vercel.app"
    if "token" not in st.session_state:
        st.error("No token available. Please log in first.")
        return
    token = st.session_state.token
    current_datetime = datetime.now().isoformat()
    if module == "Project Engine":
        response = requests.post(
            f"{BASE_URL}/saveUserData",
            json={
                "email": email,
                "userData": {
                    "Date&Time": current_datetime,
                    "Module": module,
                    "Engine": {
                        "engineering_stream": engineering_stream,
                        "domain_sector": domain_sector,
                        "career_choice": career_choice,
                        "user_flow_choice": user_flow_choice,
                        "selected_application": st.session_state.selected_application,
                        "projects_content": st.session_state.projects_content,
                        "overview_content": st.session_state.overview_content,
                        "roadmap_content": st.session_state.roadmap_content,
                        "final_report_content": st.session_state.final_report_content,
                    },
                },
            },
            headers={"Authorization": token},
        )
        if response.status_code == 200:
            st.success("User data saved successfully!")
        else:
            error_message = response.json().get("message", "Failed to save user data.")
            st.error(error_message)
    elif module == "Course Engine":
        if user_flow_choice == "Enter Job Designation":
            response = requests.post(
                f"{BASE_URL}/saveUserData",
                json={
                    "email": email,
                    "userData": {
                        "Date&Time": current_datetime,
                        "Module": module,
                        "Engine": {
                            "user_flow_choice": user_flow_choice,
                            "job_designation": st.session_state.job_designation,
                            "courses_list": st.session_state.courses_list,
                            "course_outline_content": st.session_state.course_outline_content,
                            "youtube": st.session_state.youtube,
                            "google": st.session_state.google,
                        },
                    },
                },
                headers={"Authorization": token},
            )
            if response.status_code == 200:
                st.success("User data saved successfully!")
            else:
                error_message = response.json().get(
                    "message", "Failed to save user data."
                )
                st.error(error_message)
        else:
            response = requests.post(
                f"{BASE_URL}/saveUserData",
                json={
                    "email": email,
                    "userData": {
                        "Date&Time": current_datetime,
                        "Module": module,
                        "Engine": {
                            "user_flow_choice": user_flow_choice,
                            "Stream": engineering_stream,
                            "Sector": domain_sector,
                            "Career": career_choice,
                            "Selected_job": selected_application,
                            "Selected_course": selected_course,
                            "job_profile_content": st.session_state.job_profile_content,
                            "courses_list": st.session_state.courses_list,
                            "course_outline_content": st.session_state.course_outline_content,
                            "youtube": st.session_state.youtube,
                            "google": st.session_state.google,
                        },
                    },
                },
                headers={"Authorization": token},
            )
            if response.status_code == 200:
                st.success("User data saved successfully!")
            else:
                error_message = response.json().get(
                    "message", "Failed to save user data."
                )
                st.error(error_message)
    elif module == "Research Engine":
        if user_flow_choice == "Enter Your Idea":
            if career_choice == "Entrepreneurship":
                response = requests.post(
                    f"{BASE_URL}/saveUserData",
                    json={
                        "email": email,
                        "userData": {
                            "Date&Time": current_datetime,
                            "Module": module,
                            "Engine": {
                                "user_flow_choice": user_flow_choice,
                                "career_choice": career_choice,
                                "job_designation": job_designation,
                                "goals": goals,
                                "subdomain": subdomain,
                                "courses_list": st.session_state.courses_list,
                                "data_insights": st.session_state.data_insights,
                                "strategy": st.session_state.strategy,
                                "marketing": st.session_state.marketing,
                                "roadmap": st.session_state.roadmap,
                                "success": st.session_state.success,
                            },
                        },
                    },
                    headers={"Authorization": token},
                )
            elif career_choice == "Placements":
                response = requests.post(
                    f"{BASE_URL}/saveUserData",
                    json={
                        "email": email,
                        "userData": {
                            "Date&Time": current_datetime,
                            "Module": module,
                            "Engine": {
                                "user_flow_choice": user_flow_choice,
                                "career_choice": career_choice,
                                "degree_and_field_of_study": st.session_state.degree_and_field_of_study,
                                "subdomain": st.session_state.subdomain,
                                "desired_industry": st.session_state.desired_industry,
                                "career_goals": st.session_state.career_goals,
                                "courses_list": st.session_state.courses_list.content,
                                "job_titles": st.session_state.job_titles.content,
                                "industry": st.session_state.industry.content,
                                "roadmap_attributes": st.session_state.roadmap_attributes.content,
                            },
                        },
                    },
                    headers={"Authorization": token},
                )
            else:
                response = requests.post(
                    f"{BASE_URL}/saveUserData",
                    json={
                        "email": email,
                        "userData": {
                            "Date&Time": current_datetime,
                            "Module": module,
                            "Engine": {
                                "user_flow_choice": user_flow_choice,
                                "career_choice": career_choice,
                                "degree_and_field_of_study": degree_and_field_of_study,
                                "subdomain": st.session_state.subdomain,
                                "preferred_location": st.session_state.location,
                                "budget": st.session_state.budget,
                                "courses_list": st.session_state.courses_list,
                                "academic": st.session_state.academic,
                                "roadmap_attributes": st.session_state.roadmap_attributes,
                                "success": st.session_state.success,
                            },
                        },
                    },
                    headers={"Authorization": token},
                )
            if response.status_code == 200:
                st.success("User data saved successfully!")
            else:
                error_message = response.json().get(
                    "message", "Failed to save user data."
                )
                st.error(error_message)
        else:
            if career_choice == "Entrepreneurship":
                response = requests.post(
                    f"{BASE_URL}/saveUserData",
                    json={
                        "email": email,
                        "userData": {
                            "Date&Time": current_datetime,
                            "Module": module,
                            "Engine": {
                                "user_flow_choice": user_flow_choice,
                                "Stream": engineering_stream,
                                "Sector": domain_sector,
                                "career_choice": career_choice,
                                "job_profile_content": st.session_state.job_profile_content,
                                "courses_list": st.session_state.courses_list,
                                "data_insights": st.session_state.data_insights,
                                "strategy": st.session_state.strategy,
                                "marketing": st.session_state.marketing,
                                "roadmap": st.session_state.roadmap,
                                "success": st.session_state.success,
                            },
                        },
                    },
                    headers={"Authorization": token},
                )
            elif career_choice == "Placements":
                response = requests.post(
                    f"{BASE_URL}/saveUserData",
                    json={
                        "email": email,
                        "userData": {
                            "Date&Time": current_datetime,
                            "Module": module,
                            "Engine": {
                                "user_flow_choice": user_flow_choice,
                                "Stream": engineering_stream,
                                "Sector": domain_sector,
                                "career_choice": career_choice,
                                "job_profile_content": st.session_state.job_profile_content,
                                "courses_list": st.session_state.courses_list,
                                "job_titles": st.session_state.job_titles,
                                "industry": st.session_state.industry,
                                "roadmap_attributes": st.session_state.roadmap_attributes,
                            },
                        },
                    },
                    headers={"Authorization": token},
                )
            else:
                response = requests.post(
                    f"{BASE_URL}/saveUserData",
                    json={
                        "email": email,
                        "userData": {
                            "Date&Time": current_datetime,
                            "Module": module,
                            "Engine": {
                                "user_flow_choice": user_flow_choice,
                                "Stream": engineering_stream,
                                "Sector": domain_sector,
                                "career_choice": career_choice,
                                "job_profile_content": st.session_state.job_profile_content,
                                "market": st.session_state.market,
                                "courses_list": st.session_state.courses_list,
                                "academic": st.session_state.academic,
                                "roadmap_attributes": st.session_state.roadmap_attributes,
                                "success": st.session_state.success,
                            },
                        },
                    },
                    headers={"Authorization": token},
                )
            if response.status_code == 200:
                st.success("User data saved successfully!")
            else:
                error_message = response.json().get(
                    "message", "Failed to save user data."
                )
                st.error(error_message)


def get_gemini_response_course(question, chat_template):
    messages = chat_template.format_messages(user_input=question)
    response = model.invoke(messages)
    st.session_state["flowmessages"].extend(messages)
    return response


def get_gemini_response_faq_course(
    roadmap, engineering_stream, career_choice, domain_sector, user_question
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are an Educator with real-world knowledge in only and only {roadmap}. "
                f"Please answer the following question: '{user_question}' while ensuring your response strictly adheres to the knowledge outlined in {roadmap}, you may utilize external internet sources to provide accurate and relevant information, but always consider the context of {roadmap} in your response. Do not answer questions that fall outside the scope of the provided {roadmap}.",
            ),
            ("human", "{user_input}"),
        ]
    )
    formatted_messages = chat_template.format_messages(
        engineering_stream=engineering_stream,
        career_choice=career_choice,
        domain_sector=domain_sector,
        user_input=user_question,
    )
    response = model.invoke(formatted_messages)
    return response


def get_gemini_response_faq_x_course(roadmap, user_question):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are an Educator with real-world knowledge in only and only {roadmap}. "
                f"Please answer the following question: '{user_question}' while ensuring your response strictly adheres to the knowledge outlined in {roadmap}, you may utilize external internet sources to provide accurate and relevant information, but always consider the context of {roadmap} in your response. Do not answer questions that fall outside the scope of the provided {roadmap}.",
            ),
            ("human", "{user_input}"),
        ]
    )
    formatted_messages = chat_template.format_messages(
        roadmap=roadmap,
        user_input=user_question,
    )
    response = model.invoke(formatted_messages)
    return response


def get_gemini_response_course(
    question, engineering_stream, career_choice, domain_sector
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in {engineering_stream}, "
                f"considering a student's career choice as {career_choice} and interest in {domain_sector}, "
                f"can you suggest 15 job titles that would be relevant in the current Indian market scenario?"
                f"""format for generating 15 job titles:
                Example 1:
                1. Public Health Engineer
                2. Environmental Health Engineer
                3. Water and Sanitation Engineer
                4. Infrastructure Planning Engineer
                5. Healthcare Facility Design Engineer
                6. Hospital Project Manager
                7. Biomedical Engineer (with specialization in Public Health)
                8. Health Impact Assessment Analyst
                9. Environmental Risk Management Specialist
                10. Community Health Development Engineer
                11. Sanitation and Hygiene Promotion Engineer
                12. Disaster Risk Reduction Engineer (with focus on Health)
                13. Health Infrastructure Planning and Implementation Officer
                14. Rural Health and Development Engineer
                15. Health Policy Analyst (with Engineering Background)
                Example 2:
                1. Environmental Engineer
                2. Water Resource Engineer
                3. Forestry Engineer
                4. Environmental Impact Assessment Analyst
                5. Sustainability Consultant
                6. Renewable Energy Engineer
                7. Environmental Monitoring Officer
                8. Environmental Auditor
                9. Water Treatment Engineer
                10. Wastewater Management Engineer
                11. Air Pollution Control Engineer
                12. Forest Conservation Officer
                13. Wildlife Conservation Officer
                14. Environmental Management Specialist
                15. Climate Change Adaptation Engineer
                Example 3:
                1. Public Health Engineer
                2. Environmental Health Engineer
                3. Water and Sanitation Engineer
                4. Infrastructure Planning Engineer (Healthcare)
                5. Healthcare Facility Design Engineer
                6. Hospital Project Manager
                7. Biomedical Engineer (Public Health)
                8. Health Impact Assessment Analyst
                9. Environmental Risk Management Specialist (Healthcare)
                10. Community Health Development Engineer
                11. Sanitation and Hygiene Promotion Engineer
                12. Disaster Risk Reduction Engineer (Health)
                13. Health Infrastructure Planning and Implementation Officer
                14. Rural Health and Development Engineer
                15. Health Policy Analyst (Engineering Background)
                Simply write the 15 job titles. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )
    formatted_messages = chat_template.format_messages(
        engineering_stream=engineering_stream,
        career_choice=career_choice,
        domain_sector=domain_sector,
        user_input=question,
    )
    response = model.invoke(formatted_messages)
    return response


def get_gemini_response_roadmap_course(question, domain_sector):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an Educator, you possess practical experience and expertise in the field of {domain_sector}, allowing you to provide valuable insights and guidance to students or individuals seeking to learn about {domain_sector} practices."
                f"As an Educator with real-world knowledge in {domain_sector}, you possess the expertise to offer detailed and practical advice to address users' questions effectively. Drawing upon your background, you can break down complex concepts into manageable subtasks, providing actionable steps and strategies tailored to the specific job. Your insights bridge the gap between theory and practice, empowering learners with the skills and knowledge they need to succeed in real-world {domain_sector} settings."
                f"As an Educator with real-world knowledge in {domain_sector}, you possess the expertise to offer detailed and practical advice to address users' questions effectively. When providing guidance, it's essential to break down complex concepts into manageable subtasks, ensuring that each step is explained thoroughly and is understandable on its own. If necessary, further sub-points can be provided to clarify specific aspects of the task. This approach allows learners to grasp the intricacies of the job and empowers them to navigate {domain_sector} challenges with confidence."
                f"You possess expertise in various job types: research, simulation, software development, engineering, design, entrepreneurial, social impact, internship, artistic, literature review, community service, and data analysis. You can accurately categorize jobs based on their characteristics and requirements, sometimes mixing two or three categories."
                f" When addressing a user's query {question} suggest 15 courses that will help the student understand the job better and be technically prepared for it."
                f"""Generate the output exactly in this format:
                The Course: An overview
                Like this:
                Biomedical Engineering Fundamentals: Introduces core concepts and applications in the interdisciplinary field of biomedical engineering.
                Physiology and Anatomy for Biomedical Engineers: Examines human body systems and functions essential for engineering design and innovation.
                Biomaterials and Tissue Engineering: Explores materials science for medical devices and strategies for tissue regeneration and repair.
                Biomechanics: Analyzes forces and motions within biological systems, crucial for designing biomechanical solutions.
                Bioinformatics: Utilizes computational tools to analyze biological data, aiding in research and medical diagnosis.
                Medical Imaging: Covers principles and techniques of various imaging modalities for medical diagnosis and treatment.
                Medical Device Design: Focuses on the design and development of innovative medical devices and systems.
                Biomedical Signal Processing: Studies methods for analyzing and interpreting biological signals for diagnostics and monitoring.
                Public Health Informatics: Utilizes information technology to enhance public health practices and outcomes.
                Epidemiology and Biostatistics: Investigates disease patterns and employs statistical methods in public health research.
                Environmental Health: Explores the impact of environmental factors on public health and well-being.
                Global Health: Addresses health issues and challenges on a global scale, considering diverse populations and contexts.
                Health Policy and Management: Examines principles and practices for developing and managing effective health policies and systems.
                Bioethics: Explores ethical considerations in biomedical research, treatment, and patient care.
                Capstone Project in Biomedical Engineering (Public Health): Applies biomedical engineering principles to solve real-world public health challenges through a comprehensive project.
                Simply write the 15 courses. Do not provide a heading.
                Remember to provide an overview of 2 lines after the colon after listing the course.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )
    formatted_messages = chat_template.format_messages(
        domain_sector=domain_sector, user_input=question
    )
    response = model.invoke(formatted_messages)
    return response


def get_gemini_response_roadmap_x_course(question):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an Educator, you possess practical experience and expertise in the job of {question}, allowing you to provide valuable insights and guidance to students or individuals seeking to learn about practices."
                f"As an Educator with real-world knowledge in the job {question}, you possess the expertise to offer detailed and practical advice to address users' questions effectively. Drawing upon your background, you can break down complex concepts into manageable subtasks, providing actionable steps and strategies tailored to the specific job. Your insights bridge the gap between theory and practice, empowering learners with the skills and knowledge they need to succeed in real-world settings."
                f"As an Educator with real-world knowledge in the job {question}, you possess the expertise to offer detailed and practical advice to address users' questions effectively. When providing guidance, it's essential to break down complex concepts into manageable subtasks, ensuring that each step is explained thoroughly and is understandable on its own. If necessary, further sub-points can be provided to clarify specific aspects of the task. This approach allows learners to grasp the intricacies of the job {question} and empowers them to navigate challenges with confidence."
                f"You possess expertise in various job types: research, simulation, software development, engineering, design, entrepreneurial, social impact, internship, artistic, literature review, community service, and data analysis. You can accurately categorize jobs based on their characteristics and requirements, sometimes mixing two or three categories."
                f" When addressing a user's query {question} suggest 15 courses that will help the student understand the job better and be technically prepared for it."
                f"""Generate the output exactly in this format:
                The Course: An overview
                Like this:
                Biomedical Engineering Fundamentals: Introduces core concepts and applications in the interdisciplinary field of biomedical engineering.
                Physiology and Anatomy for Biomedical Engineers: Examines human body systems and functions essential for engineering design and innovation.
                Biomaterials and Tissue Engineering: Explores materials science for medical devices and strategies for tissue regeneration and repair.
                Biomechanics: Analyzes forces and motions within biological systems, crucial for designing biomechanical solutions.
                Bioinformatics: Utilizes computational tools to analyze biological data, aiding in research and medical diagnosis.
                Medical Imaging: Covers principles and techniques of various imaging modalities for medical diagnosis and treatment.
                Medical Device Design: Focuses on the design and development of innovative medical devices and systems.
                Biomedical Signal Processing: Studies methods for analyzing and interpreting biological signals for diagnostics and monitoring.
                Public Health Informatics: Utilizes information technology to enhance public health practices and outcomes.
                Epidemiology and Biostatistics: Investigates disease patterns and employs statistical methods in public health research.
                Environmental Health: Explores the impact of environmental factors on public health and well-being.
                Global Health: Addresses health issues and challenges on a global scale, considering diverse populations and contexts.
                Health Policy and Management: Examines principles and practices for developing and managing effective health policies and systems.
                Bioethics: Explores ethical considerations in biomedical research, treatment, and patient care.
                Capstone Project in Biomedical Engineering (Public Health): Applies biomedical engineering principles to solve real-world public health challenges through a comprehensive project.
                Simply write the 15 courses. Do not provide a heading.
                Remember to provide an overview of 2 lines after the colon after listing the course.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )
    formatted_messages = chat_template.format_messages(user_input=question)
    response = model.invoke(formatted_messages)
    return response


def get_gemini_response_course_outline_course(question, job_designation):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:
                Intermediate
                This course delves into the intricate world of sustainable transportation planning, empowering learners with the knowledge and skills to create environmentally conscious and equitable transportation systems. The course emphasizes real-world applications, equipping learners to address pressing challenges in the transportation sector.
                Geographic Information Systems (GIS) for data analysis and visualization
                Transportation modeling software for simulating traffic patterns and predicting outcomes
                Project management tools for planning and implementation
                Data analysis techniques for interpreting transportation data
                Basic understanding of transportation engineering or planning
                Familiarity with urban planning and land use concepts
                Proficiency in data analysis and modeling software
                This course is highly relevant for professionals in transportation planning, engineering, and policymaking. It enhances the skills needed to design and implement sustainable transportation solutions, such as:
                Transit planning
                Roadway design
                Active transportation planning
                Transportation policy analysis
                Upon completing the course, participants will have:
                A comprehensive understanding of sustainable transportation principles and best practices
                Proficiency in using GIS, transportation modeling, and data analysis tools
                The ability to analyze transportation data and identify sustainability challenges
                Skills in developing and evaluating sustainable transportation plans
                An understanding of the regulatory and policy frameworks for sustainable transportation
                The course unfolds over 10 weeks, each week dedicated to a specific aspect of sustainable transportation planning:
                Weeks 1-2: Introduction to sustainable transportation and its principles\n
                Weeks 3-4: Data collection and analysis for transportation planning\n
                Weeks 5-6: Transportation modeling and forecasting\n
                Weeks 7-8: Sustainable transportation plan development\n
                Week 9: Transportation policy analysis and evaluation\n
                Week 10: Case studies and best practices in sustainable transportation\n
                To supplement the course content, learners are encouraged to explore the following resources:
                Transportation Research Board (TRB): A leading source of research and publications on transportation topics, including sustainable transportation.
                Institute of Transportation Engineers (ITE): A professional organization that offers resources and training on transportation engineering and planning.
                American Planning Association (APA): Provides guidance and resources on sustainable land use planning, including transportation planning.
                International Association of Public Transport (UITP): A global organization dedicated to promoting sustainable public transportation.
                By utilizing these resources, learners can expand their knowledge and stay up-to-date on the latest advancements in sustainable transportation planning.
                """
                f"""
                example 2:
                Intermediate
                Soil Science unravels the intricate world of soils, their properties, and their vital role in agriculture, environmental sustainability, and ecosystem functioning. This course provides a comprehensive understanding of soil science principles, enabling learners to analyze, manage, and conserve soil resources effectively.
                Learners will gain proficiency in:
                Soil sampling and analysis techniques
                Soil classification systems
                Soil fertility management
                Soil erosion control
                Soil moisture monitoring and modeling
                Basic understanding of biology, chemistry, and earth science
                Introductory soil science or related coursework
                Soil Science is highly relevant for professionals in agriculture, environmental science, land management, and related fields. It enhances the skills required for:
                Soil health assessment and improvement
                Sustainable crop production
                Soil conservation and remediation
                Environmental impact assessment
                Land use planning
                Upon completing the course, participants will have:
                A thorough understanding of soil science principles and their practical applications
                Proficiency in soil sampling, analysis, and interpretation
                Skills in soil fertility management, erosion control, and moisture conservation
                The ability to evaluate soil health and develop sustainable soil management strategies
                Knowledge of the environmental and economic significance of soils
                The course unfolds over 10 weeks, each week dedicated to a specific aspect of the project:
                Weeks 1-2: Introduction to soil science and soil properties
                empty line\n
                Weeks 3-4: Soil classification and soil survey
                empty line\n
                Weeks 5-6: Soil fertility and nutrient management
                empty line\n
                Weeks 7-8: Soil erosion and conservation\n
                Weeks 9-10: Soil moisture management and modeling\n
                Resources
                To supplement the course content, learners are encouraged to explore the following resources:
                Soil Science Society of America (SSSA): A leading organization providing resources and publications on soil science.
                Natural Resources Conservation Service (NRCS): A government agency offering guidance and technical assistance on soil management and conservation.
                International Union of Soil Sciences (IUSS): A global organization dedicated to promoting soil science research and education.
                National Soil Survey Center (NSSC): A repository of soil survey data and maps.
                Soil and Water Conservation Society (SWCS): A professional organization focused on soil and water conservation issues.
                """
                f"Drawing on your significant expertise and practical experience in {job_designation}, you are well-equipped to guide learners aiming to excel in this field. Your real-world insights enable you to simplify complex concepts related to {job_designation}, making them accessible and actionable for students. You can dissect the essentials of the job into clear, manageable steps, ensuring each concept is fully understood. This methodical breakdown not only demystifies the job's intricacies but also builds learner confidence to tackle {job_designation} challenges effectively."
                f"provide me a course outline of the course {question} using the above 2 examples as a reference on how to output the course outline, "
                f"remember to include the tilte of the course {question} exactly like in the two examples, "
                f"remember to include the difficulty level of the course {question} exactly like in the two examples, "
                f"remember to include a course overview of the course {question} exactly like in the two examples, "
                f"remember to include the tech stacks, technologies, and tools covered in the course {question} exactly like in the two examples, "
                f"remember to include the prerequisite knowledge/courses required for the course {question} exactly like in the two examples, "
                f"remember to include the relevance to job enhancement of the course {question} exactly like in the two examples, "
                f"remember to include the expected outcomes of the course {question} exactly like in the two examples, "
                f"remember to include the tentative course timeline of the course {question} and make sure each week is displayed in its own line and not all in a single paragraph, exactly like in the two examples, "
                f"remember to include the resources of the course {question} exactly like in the two examples, ",
            ),
            ("human", "{user_input}"),
        ]
    )
    formatted_messages = chat_template.format_messages(
        job_designation=job_designation, user_input=question
    )
    response = model.invoke(formatted_messages)
    return response


load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyDPow8LG1uOOHG5kj8a2axfdbJ4qTxZxbs"))
model = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro", convert_system_message_to_human=True
)
st.header("Course Recommendation Engine")
st.write(
    "Get tailored course recommendations to align your education with career aspirations and industry standards. Our system ensures you make informed decisions and enhances your readiness for the job market.")
temp = """"""
formatt = """
                Difficulty Level: Beginner to Advanced
                This course is meticulously crafted to cater to learners at all stages of their educational journey. It begins with foundational concepts perfect for beginners who are new to game audio and sound design. As the course progresses, the content delves into more sophisticated topics suitable for intermediate learners, and ultimately, it challenges advanced practitioners with specialized, high-level techniques. This structured approach ensures a comprehensive learning experience that adapts to the skill level of each participant.
                Course Overview
                The "Game Audio and Sound Design" course provides an extensive exploration into the art and technology of creating captivating soundscapes for video games. This journey encompasses the vital role of audio in gaming, from its contribution to storytelling and player immersion to the technical aspects of its production. Participants will engage in detailed study and hands-on practice in areas such as sound design, music composition, audio software manipulation, and the seamless integration of sound with game mechanics. This course is designed to bridge the gap between theoretical knowledge and practical application, preparing learners for real-world challenges in the game development industry.
                Tech Stacks, Technologies, and Tools Covered
                Throughout the course, learners will be introduced to and gain proficiency in a range of industry-standard technologies and tools. This includes:
                - Digital Audio Workstations (DAWs) like Ableton Live, Pro Tools, and FL Studio for creating and editing sound and music.
                - Audio Middleware such as FMOD and Wwise, which are crucial for integrating complex sound designs into games without deep programming knowledge.
                - Game Engines including Unity and Unreal Engine, where students will learn how to implement and manipulate audio within interactive environments.
                - Advanced techniques in 3D Audio and Spatial Sound creation to enhance immersion in VR, AR, and traditional gaming platforms.
                Learners will be guided through each tool's unique features and applications, with a strong emphasis on practical, project-based learning.
                Prerequisite Knowledge/Courses
                This course is open to everyone with a passion for game development and sound design. No prior knowledge is specifically required, making it an excellent opportunity for beginners. However, individuals with a basic understanding of music theory, some familiarity with computers and software, and a keen interest in sound design and gaming will find the course particularly enriching.
                Relevance to Job Enhancement
                For professionals in the game development industry or those aspiring to enter this field, the course is highly relevant. It equips sound designers, music composers, audio engineers, and game developers with the skills needed to create engaging and immersive audio experiences. The practical knowledge and hands-on experience gained will significantly enhance one's ability to contribute to various aspects of game audio, from conceptual design to technical implementation.
                Expected Outcomes
                Upon completing the course, participants will have:
                - A deep understanding of the role and impact of sound in video games.
                - Advanced skills in sound design and music composition tailored specifically for gaming applications.
                - Proficiency in using leading audio production tools and integrating sound into game engines.
                - A comprehensive portfolio of projects demonstrating their skills and creativity in game audio design.
                Tentative Course Timeline
                The course unfolds over 10 weeks, each week dedicated to a specific aspect of game audio and sound design:
                1. Weeks 1-2: Introduction to the fundamentals of game audio.
                2. Weeks 3-4: Diving deeper into audio production techniques and software.
                3. Weeks 5-6: Exploring audio middleware and integration with game engines.
                4. Weeks 7-8: Advanced sound design techniques and music composition for games.
                5. Week 9: Focusing on professional skills, collaboration, and communication within game development teams.
                6. Week 10: Portfolio development, providing a platform to showcase skills and projects.
                Resources
                To complement the structured course content, learners are encouraged to explore a wide array of external resources for a more rounded understanding of game audio and sound design:
                YouTube
                For visual and auditory learning, YouTube is an invaluable resource. Search for comprehensive playlists and tutorials on game sound design basics, music production, and specific software tutorials to enhance your learning experience.
                Online Learning Platforms
                Platforms such as Coursera, Udemy, and others offer specialized courses that can expand your knowledge in game audio design, music composition, and audio software. Look for courses that match your skill level and interests.
                Articles and Blogs
                Websites dedicated to sound design and game development, such as Designing Sound and the AudioKinetic Blog, are excellent sources of articles, tutorials, and industry insights.
                Academic Papers and Books
                For those interested in the theoretical underpinnings of sound design and its application in games, academic databases like Google Scholar and IEEE Xplore offer a wealth of research papers. Additionally, comprehensive books on game audio, available through online retailers, provide in-depth knowledge and are a great addition to any learning path.
                Learners are encouraged to utilize these resources alongside the course materials to maximize their understanding and skills in game audio and sound design.   
"""
fixed_question = "help the student by listing 15 job positions specific to the {engineering_stream} , {domain_sector}, {career_choice} that would be relevant in the current Indian market scenario."
show_select_box = False
show_select_box = False
show_select_box = False
if 'youtube' not in st.session_state:
    st.session_state.youtube = None  # or any default value you want to set
if 'google' not in st.session_state:
    st.session_state.google = None
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "job_content" not in st.session_state:
    st.session_state.job_content = ""
if "flowmessages" not in st.session_state:
    st.session_state["flowmessages"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "job_profile_content" not in st.session_state:
    st.session_state.job_profile_content = ""
if "job_profile_shown" not in st.session_state:
    st.session_state.jop_profile_shown = False
if "applications" not in st.session_state:
    st.session_state.applications = []
if "courses_list" not in st.session_state:
    st.session_state.courses_list = ""
if "courses_list_shown" not in st.session_state:
    st.session_state.courses_list_shown = False
if "courses" not in st.session_state:
    st.session_state.courses = []
if "course_list_stripped" not in st.session_state:
    st.session_state.course_list_stripped = False
if "selected_coursee" not in st.session_state:
    st.session_state.selected_coursee = ""
if "course_selected" not in st.session_state:
    st.session_state.course_selected = True
if "course_outline_content" not in st.session_state:
    st.session_state.course_outline_content = ""
if "course_outline_shown" not in st.session_state:
    st.session_state.course_outline_shown = False
st.write("---")
user_flow_choice = st.selectbox(
    "Select Your Path:",
    ["Generate Job Designation", "Enter Job Designation"],
    key="user_flow_choice",
)
st.write("---")
if "current_user_flow_choice" not in st.session_state:
    st.session_state.current_user_flow_choice = user_flow_choice
if st.session_state.current_user_flow_choice != user_flow_choice:
    st.session_state.job_profile_content = ""
    st.session_state.job_profile_shown = False
    st.session_state.applications = []
    st.session_state.courses_list = ""
    st.session_state.courses_list_shown = False
    st.session_state.courses = []
    st.session_state.course_list_stripped = False
    st.session_state.selected_coursee = ""
    st.session_state.course_selected = True
    st.session_state.course_outline_content = ""
    st.session_state.course_outline_shown = False
    st.session_state.current_user_flow_choice = user_flow_choice
if user_flow_choice == "Generate Job Designation":
    temp = """"""
    engineering_stream = st.selectbox(
        "Engineering Stream:",
        [
            "B.Tech - Civil Engineering",
            "B.Tech - Electrical Engineering",
            "B.Tech - Computer Science and Engineering",
            "B.Tech - Computer Science and Engineering (Artificial Intelligence and Machine Learning)",
            "B.Tech - Computer Science and Engineering (Artificial Intelligence and Robotics)",
            "B.Tech. Computer Science and Engineering (Data Science)",
            "B.Tech - Computer Science and Engineering (Cyber Physical Systems)",
            "B.Tech - Computer Science and Engineering (Cyber Security)",
            "B.Tech - Electrical and Electronics Engineering",
            "B.Tech - Electrical and Computer Science Engineering",
            "B.Tech - Electronics and Communication Engineering",
            "B.Tech - Electronics Engineering (VLSI Design and Technology)",
            "B.Tech - Electronics and Computer Engineering",
            "B.Tech - Fashion Technology",
            "B.Tech - Mechanical Engineering",
            "B.Tech - Mechatronics and Automation",
            "B. Tech - Mechanical Engineering (Electric Vehicles)",
        ],
        key="engineering_stream",
    )
    domain_sector = st.selectbox(
        "Domain Sector:",
                [
            "Agriculture",
            "Atomic Energy",
            "Automible",
            "Chemicals & Fertilizers",
            "Civil Aviation",
            "Coal",
            "Commerce & Industry",
            "Corporate Affairs",
            "Culture",
            "Defence",
            "Earth Sciences",
            "Education and Human Resource Development",
            "Environment & Forests",
            "External Affairs",
            "Finance",
            "Food Processing Industries",
            "Health & Family Welfare",
            "Heavy Industry & Public Enterprises",
            "Home Affairs",
            "Housing & Urban Poverty Alleviation",
            "Information & Broadcasting",
            "Infrastructure (Road Transport & Highways, Railways, Urban Development)",
            "Labour & Employment",
            "Law & Justice",
            "Micro, Small and Medium Enterprises",
            "Mines",
            "Minority Affairs",
            "Panchayati Raj",
            "Parliamentary Affairs",
            "Petroleum & Natural Gas",
            "Personnel, Public Grievances & Pensions",
            "Planning Commission",
            "Power",
            "Renewable Energy",
            "Rural Development",
            "Science & Technology",
            "Shipping",
            "Social Justice & Empowerment",
            "Space",
            "Statistics & Programme Implementation",
            "Steel",
            "Textiles",
            "Tourism",
            "Tribal Affairs",
            "Water Resources and Sanitation",
            "Women & Child Development",
            "Youth Affairs & Sports",
        ],

        key="domain_sector",
    )
    career_choice = st.selectbox(
        "Career Choice:",
        ["Higher Studies", "Placements", "Entrepreneurship"],
        key="career_choice",
    )
    st.session_state.app_selected = False
    if st.button("Generate Job Profiles"):
        st.session_state.job_profile_content = ""
        st.session_state.job_profile_shown = False
        st.session_state.applications = []
        st.session_state.courses_list = ""
        st.session_state.courses_list_shown = False
        st.session_state.courses = []
        st.session_state.course_list_stripped = False
        st.session_state.selected_coursee = ""
        st.session_state.course_selected = True
        st.session_state.course_outline_content = ""
        st.session_state.course_outline_shown = False
        response = get_gemini_response_course(
            fixed_question, engineering_stream, career_choice, domain_sector
        )
        x = response.content
        words = [line.split(":")[0].strip() for line in x.split("\n")]
        applications = [item.strip("") and item.replace("*", "") for item in words]
        st.session_state.job_profile_content = response.content
        st.session_state.job_profile_shown = True
        st.session_state.applications = applications
    if st.session_state.applications and st.session_state.job_profile_content:
        st.write("---")
        st.subheader("Here are 15 Job Profiles for you: ")
        st.write(st.session_state.job_profile_content)
    if (
        "applications" in st.session_state
        and st.session_state.applications
        and st.session_state.job_profile_shown
    ):
        st.write("---")
        st.subheader("Choose a job designation which interests you:")
        selected_application = st.selectbox(
            "Select a Job:",
            st.session_state.applications,
            key="selected_application",
        )
        st.session_state.app_selected = True
    if st.session_state.app_selected:
        if st.button("Generate Courses"):
            st.session_state.courses_list = ""
            st.session_state.courses_list_shown = False
            st.session_state.courses = []
            st.session_state.course_list_stripped = False
            st.session_state.selected_coursee = ""
            st.session_state.course_selected = True
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            response_coursess = get_gemini_response_roadmap_course(
                st.session_state.selected_application, domain_sector
            )
            st.session_state.courses_list = response_coursess.content
            st.session_state.courses_list_shown = True
    if st.session_state.courses_list:
        st.write("---")
        st.subheader("Here are 15 Courses Necessary for the Job: ")
        st.write(st.session_state.courses_list)
    if st.session_state.courses_list_shown:
        wordss = [
            line.split(":")[0].strip()
            for line in st.session_state.courses_list.split("\n")
        ]
        courses = [item.strip("") and item.replace("*", "") for item in wordss]
        st.session_state.courses = courses
        st.session_state.course_list_stripped = True
    if st.session_state.course_list_stripped:
        st.write("---")
        st.subheader("Know more about a course:")
        selected_course = st.selectbox(
            "Select a Course:",
            st.session_state.courses,
            key="selected_course",
        )
        st.session_state.selected_coursee = selected_course
        st.session_state.course_selected = True
    if st.session_state.selected_coursee:
        if st.button("Process Course"):
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument("--headless=new")
            # driver = webdriver.Chrome(options=chrome_options)
            # driver.get("https://www.google.com/")
            # topic = f"{st.session_state.selected_coursee} course"
            # search_box = driver.find_element(By.NAME, "q")
            # search_box.send_keys(topic)
            # search_box.send_keys(Keys.RETURN)
            # time.sleep(3)
            # html_content = driver.page_source
            # soup = BeautifulSoup(html_content, "html.parser")
            # google_data = []
            # results = soup.select("h3.LC20lb.MBeuO.DKV0Md")
            # for result in results:
            #     title = result.text
            #     link = result.find_parent("a")["href"]
            #     google_data.append({"title": title, "link": link})
            # video_link_element = soup.find(
            #     "a", {"class": "LatpMc nPDzT T3FoJb", "jsname": "VIftV"}
            # )
            # if video_link_element:
            #     video_link = "https://www.google.com" + video_link_element["href"]
            #     driver.get(video_link)
            # else:
            #     print("Videos link not found")
            # time.sleep(3)
            # html_content_vid = driver.page_source
            # soup_vid = BeautifulSoup(html_content_vid, "html.parser")
            # youtube_data = []
            # video_results = soup_vid.select('a[jsname="UWckNb"]')
            # for video in video_results:
            #     link = video["href"]
            #     title = video.find("h3", class_="LC20lb MBeuO DKV0Md").text
            #     youtube_data.append({"title": title, "link": link})
            # st.session_state.google = google_data
            # st.session_state.youtube = youtube_data
            # driver.quit()
            response_course_outline = get_gemini_response_course_outline_course(
                st.session_state.selected_coursee, st.session_state.selected_application
            )
            temp += "\n"
            temp += response_course_outline.content
            st.session_state.course_outline_content = response_course_outline.content
            st.session_state.course_outline_shown = True
    if st.session_state.course_outline_shown:
        st.write("---")
        st.subheader("Course Outline: ")
        st.write(st.session_state.course_outline_content)
        # st.write("---")
        # if st.session_state.youtube:
        #     st.subheader("Here are some Youtube videos that might help you:")
        #     for video in st.session_state.youtube:
        #         st.markdown(f"[{str(video['title'])}]({video['link']})")
        #         st.write(f"{video['link']}")
        #     st.write("---")
        # if st.session_state.google:
        #     st.subheader("Here are some additional links that might help you:")
        #     for data in st.session_state.google:
                # st.markdown(f"[{data['title']}]({data['link']})")
        with st.sidebar:
            st.subheader("Feel free to inquire about any aspect of the Courses")
            user_FAQ_que = st.text_input("Enter your query:", key="heluuuuuuuuuuuu")
            if st.button("Ask Daira"):
                if user_FAQ_que:
                    response_fa = get_gemini_response_faq_course(
                        temp,
                        engineering_stream,
                        career_choice,
                        domain_sector,
                        user_FAQ_que,
                    )
                    st.write(response_fa.content)
                else:
                    st.warning("Please enter a question before asking Daira.")
        st.write("---")
        if st.button("Save Generated Text"):
            email = st.session_state.email
            bruh(email, "Course Engine", user_flow_choice, career_choice)
else:
    tempp = """"""
    st.session_state.designation_entered = False
    st.session_state.job_designation = ""
    st.session_state.job_designation = st.text_input(
        "Desired Job Designation:", key="job_desjjjjjjjjjjjjjjjjjjhhhhhhhhhhhhhhhhignationn", placeholder="Game Developer"
    )
    st.session_state.designation_entered = True
    if st.session_state.designation_entered:
        if st.button("Generate Courses"):
            st.session_state.courses_list = ""
            st.session_state.courses_list_shown = False
            st.session_state.courses = []
            st.session_state.course_list_stripped = False
            st.session_state.selected_coursee = ""
            st.session_state.course_selected = True
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            response_coursess = get_gemini_response_roadmap_x_course(
                st.session_state.job_designation
            )
            st.session_state.courses_list = response_coursess.content
            st.session_state.courses_list_shown = True
    if st.session_state.courses_list:
        st.write("---")
        st.subheader("Here are 15 Courses Necessary for the Job: ")
        st.write(st.session_state.courses_list)
    if st.session_state.courses_list_shown:
        wordss = [
            line.split(":")[0].strip()
            for line in st.session_state.courses_list.split("\n")
        ]
        courses = [item.strip("") and item.replace("*", "") for item in wordss]
        st.session_state.courses = courses
        st.session_state.course_list_stripped = True
    if st.session_state.course_list_stripped:
        st.write("---")
        st.subheader("Know more about a course:")
        selected_course = st.selectbox(
            "Select a Course:",
            st.session_state.courses,
            key="selected_course",
        )
        st.session_state.selected_coursee = selected_course
        tempp += "\n"
        tempp += selected_course
        st.session_state.course_selected = True
    if st.session_state.selected_coursee:
        if st.button("Process Course"):
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument("--headless=new")
            # driver = webdriver.Chrome(options=chrome_options)
            # driver.get("https://www.google.com/")
            # topic = f"{st.session_state.selected_coursee} course"
            # search_box = driver.find_element(By.NAME, "q")
            # search_box.send_keys(topic)
            # search_box.send_keys(Keys.RETURN)
            # time.sleep(3)
            # html_content = driver.page_source
            # soup = BeautifulSoup(html_content, "html.parser")
            # google_data = []
            # results = soup.select("h3.LC20lb.MBeuO.DKV0Md")
            # for result in results:
            #     title = result.text
            #     link = result.find_parent("a")["href"]
            #     google_data.append({"title": title, "link": link})
            # video_link_element = soup.find(
            #     "a", {"class": "LatpMc nPDzT T3FoJb", "jsname": "VIftV"}
            # )
            # if video_link_element:
            #     video_link = "https://www.google.com" + video_link_element["href"]
            #     driver.get(video_link)
            # else:
            #     print("Videos link not found")
            # time.sleep(3)
            # html_content_vid = driver.page_source
            # soup_vid = BeautifulSoup(html_content_vid, "html.parser")
            # youtube_data = []
            # video_results = soup_vid.select('a[jsname="UWckNb"]')
            # for video in video_results:
            #     link = video["href"]
            #     title = video.find("h3", class_="LC20lb MBeuO DKV0Md").text
            #     youtube_data.append({"title": title, "link": link})
            # st.session_state.google = google_data
            # st.session_state.youtube = youtube_data
            # driver.quit()
            response_course_outline = get_gemini_response_course_outline_course(
                st.session_state.selected_coursee, st.session_state.job_designation
            )
            st.session_state.course_outline_content = response_course_outline.content
            tempp += "\n"
            tempp += response_course_outline.content
            st.session_state.course_outline_shown = True
    if st.session_state.course_outline_shown:
        st.write("---")
        st.subheader("Course Outline: ")
        st.write(st.session_state.course_outline_content)
        st.write("---")
        # if st.session_state.youtube:
        #     st.subheader("Here are some Youtube videos that might help you:")
        #     for video in st.session_state.youtube:
        #         st.markdown(f"[{str(video['title'])}]({video['link']})")
        #         st.write(f"{video['link']}")
        # st.write("---")
        # if st.session_state.google:
        #     st.subheader("Here are some additional links that might help you:")
        #     for data in st.session_state.google:
        #         st.markdown(f"[{data['title']}]({data['link']})")
        with st.sidebar:
            st.subheader("Feel free to inquire about any aspect of the Courses")
            user_FAQ_que = st.text_input("Enter your query:", key="heluuuuuuuuuuuu")
            if st.button("Ask Daira"):
                if user_FAQ_que:
                    response_fa = get_gemini_response_faq_x_course(tempp, user_FAQ_que)
                    st.write(response_fa.content)
                else:
                    st.warning("Please enter a question before asking Daira.")
        st.write("---")
        if st.button("Save Generated Text"):
            email = st.session_state.email
            bruh(email, "Course Engine", user_flow_choice, "No")
