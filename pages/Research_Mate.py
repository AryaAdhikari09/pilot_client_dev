import streamlit as st
import asyncio
import aiohttp
import subprocess
import os
import re
import time
import requests
# import faiss
import numpy as np
import streamlit as st
import time
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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium import webdriver


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
                                "job_designation": st.session_state.job_designation,
                                "goals": st.session_state.goals,
                                "subdomain": st.session_state.selected_application_mrm,
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
                                "courses_list": st.session_state.courses_list_irm,
                                "job_titles": st.session_state.job_titles_irm,
                                "industry": st.session_state.industry_irm,
                                "roadmap_attributes": st.session_state.roadmap_attributes_irm,
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
                                "degree_and_field_of_study": st.session_state.degree_and_field_of_study_arm,
                                "subdomain": st.session_state.subdomain_arm,
                                "preferred_location": st.session_state.location,
                                "budget": st.session_state.budget,
                                "courses_list": st.session_state.courses_list_arm,
                                "academic": st.session_state.academic_arm,
                                "roadmap_attributes": st.session_state.roadmap_attributes_arm,
                                "success": st.session_state.success_arm,
                                "market": st.session_state.market_arm,
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
                                "courses_list": st.session_state.courses_list,
                                "market": st.session_state.market,
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


def get_research_subdomains(question, engineering_stream, career_choice, domain_sector):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in {engineering_stream}, "
                f"considering a student's career choice as {career_choice} and interest in {domain_sector}, "
                f"can you suggest 15 research subdomains along with a small overview for each that would be relevant in the current Indian market scenario?"
                f"""format for generating 15 research subdomains:
                Example 1:
                1. **Sustainable Fashion Materials:** Exploring innovative materials that minimize environmental impact and promote sustainability in fashion.
                2. **Textile Recycling Technologies:** Developing efficient methods for recycling textiles to reduce waste and promote a circular economy.
                3. **Ethical Manufacturing Practices:** Investigating fair labor practices and sustainable production methods in the fashion industry.
                4. **Eco-Friendly Dyeing Techniques:** Creating dyeing processes that reduce water usage and pollution in textile manufacturing.
                5. **Circular Economy in Fashion:** Studying systems that encourage recycling and reuse of materials within the fashion industry.
                6. **Fashion Supply Chain Transparency:** Enhancing transparency in the supply chain to ensure ethical sourcing and production.
                7. **Zero Waste Fashion Design:** Designing clothing with minimal waste generation through innovative patterns and techniques.
                8. **Biodegradable Textiles:** Researching textiles that can naturally decompose without harming the environment.
                9. **Sustainable Fabric Innovations:** Developing new fabrics that are sustainable and eco-friendly.
                10. **Carbon Footprint Reduction in Fashion:** Strategies to reduce the carbon emissions associated with fashion production and distribution.
                11. **Water Conservation in Textile Production:** Techniques to minimize water use in the production of textiles.
                12. **Renewable Energy in Fashion Manufacturing:** Implementing renewable energy sources in fashion manufacturing processes.
                13. **Sustainable Apparel Marketing Strategies:** Effective marketing strategies that promote sustainable fashion.
                14. **Consumer Behavior Towards Sustainable Fashion:** Understanding consumer attitudes and behaviors towards sustainable fashion.
                15. **Impact of Technology on Sustainable Fashion:** How technology is transforming sustainable practices in the fashion industry.

                Example 2:
                1. **Renewable Energy Storage Solutions:** Innovative solutions for storing renewable energy efficiently.
                2. **Solar Power Innovations:** Advances in solar power technology to improve efficiency and accessibility.
                3. **Wind Energy Technologies:** New developments in wind energy to increase power generation.
                4. **Bioenergy and Biomass Conversion:** Researching methods to convert biomass into usable energy.
                5. **Smart Grid Technology:** Developing smart grid systems for efficient energy distribution and management.
                6. **Energy Efficiency in Buildings:** Techniques to enhance energy efficiency in residential and commercial buildings.
                7. **Green Hydrogen Production:** Exploring the production and use of green hydrogen as a clean energy source.
                8. **Electric Vehicle Charging Infrastructure:** Building and optimizing infrastructure for electric vehicle charging.
                9. **Waste-to-Energy Systems:** Converting waste materials into renewable energy.
                10. **Sustainable Energy Policies:** Analyzing and developing policies to support sustainable energy initiatives.
                11. **Microgrid Development:** Implementing microgrids for localized and resilient energy solutions.
                12. **Energy Harvesting Technologies:** Techniques to capture and store energy from various sources.
                13. **Ocean Energy Exploitation:** Harnessing energy from ocean waves and tides.
                14. **Geothermal Energy Utilization:** Exploring the potential of geothermal energy for power generation.
                15. **Impact of Climate Change on Renewable Energy:** Studying the effects of climate change on renewable energy resources and systems.

                Example 3:
                1. **Health Informatics:** Utilizing information technology to improve healthcare services and outcomes.
                2. **Telemedicine Solutions:** Developing remote healthcare solutions to increase accessibility.
                3. **Biomechanics in Rehabilitation:** Applying biomechanics to enhance rehabilitation techniques.
                4. **Medical Device Innovation:** Creating new medical devices to improve patient care.
                5. **Personalized Medicine:** Tailoring medical treatments to individual patient characteristics.
                6. **Health Data Analytics:** Using data analytics to improve healthcare decision-making.
                7. **Biomedical Imaging Techniques:** Advancing imaging techniques for better diagnosis and treatment.
                8. **AI in Healthcare Diagnostics:** Implementing artificial intelligence to enhance diagnostic accuracy.
                9. **Remote Patient Monitoring Systems:** Developing systems to monitor patients remotely and in real-time.
                10. **Health Wearables Development:** Creating wearable devices to track and improve health metrics.
                11. **Digital Health Platforms:** Building platforms to deliver healthcare services digitally.
                12. **Genomic Data Analysis:** Analyzing genomic data to inform medical research and treatment.
                13. **Drug Delivery Systems:** Innovating methods to deliver drugs more effectively.
                14. **Public Health Technology:** Leveraging technology to improve public health initiatives.
                15. **Mobile Health Applications:** Developing mobile apps to support health and wellness.

                Provide the research subdomains with a small overview. Do not provide a heading.
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


import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.set_page_config(page_title="Research Mate", page_icon=":smile:")


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


def get_target_audience_analysis(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the target audience's needs and pain points on thee research subdomain {selected_subdomain},"
                f"""Example of a response:
                Understanding the Target Audience's Needs and Pain Points

                1. Consumer Demographics
                - Age: Primarily 18-35 years old, tech-savvy, and environmentally conscious.
                - Location: Urban areas with high access to sustainable fashion options, suburban areas with growing interest, and rural areas with limited access but increasing awareness.
                - Income Level: Middle to upper-middle class with disposable income to spend on higher-priced sustainable goods, showing a willingness to invest in quality products.
                - Education Level: College-educated individuals who are well-informed about sustainability issues and seek out eco-friendly products.

                2. Consumer Preferences
                - Eco-Friendly Materials: High interest in clothing made from recycled, organic, or biodegradable materials such as organic cotton, hemp, and recycled polyester.
                - Transparency: Consumers want detailed information about production processes, sourcing of materials, and labor practices.
                - Ethical Production: Strong preference for brands that ensure fair wages, safe working conditions, and minimal environmental impact.
                - Durability and Quality: Consumers expect sustainable fashion to be durable, high-quality, and justify the higher price through longevity and performance.

                3. Pain Points
                - High Cost: Sustainable fashion is often more expensive than fast fashion, which can deter some consumers. Possible solutions include offering sliding scale pricing, payment plans, and highlighting long-term savings.
                - Limited Options: Consumers may perceive sustainable fashion as offering fewer style choices compared to traditional fashion. Addressing this can involve regularly updating collections and collaborating with designers.
                - Availability: Consumers face challenges in finding sustainable fashion brands in physical stores. Improving availability can involve expanding online presence and hosting pop-up shops in various cities.
                - Greenwashing: Consumers are wary of brands falsely claiming to be sustainable. Building trust can involve obtaining credible certifications and providing transparent information about practices."""
                f"Make sure to provide detailed insights and explanations for each of the points consumer demographics, consumer preferences, pain points. Do not provide a heading.",
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


def get_data_insights(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of data and insights on the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Data and Insights

                1. Survey Results and Studies
                - Global Data Survey (2021): 75% of millennials are willing to pay more for sustainable products.
                - McKinsey & Company (2020): 57% of consumers have made significant changes to their lifestyles to reduce their environmental impact.

                2. Trends
                - Rise of Circular Fashion: Increasing consumer interest in renting, swapping, and recycling clothes.
                - Technology Integration: Use of digital platforms to promote transparency and traceability (e.g., blockchain).

                3. Competitive Analysis
                - Key Competitors: Patagonia, Reformation, Everlane.
                - New Entrants: ThredUp, Poshmark.
                - Strengths of Competitors: Strong brand identity, loyal customer base, continuous innovation in sustainable practices.
                - Weaknesses of Competitors: High prices, limited physical presence, potential greenwashing issues.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
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


def get_strategies_to_address_pain_points(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide detailed strategies to address pain points in the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Strategies to Address Pain Points

                1. Affordability
                - Sliding Scale Pricing: Offering products at various price points to cater to different income levels.
                - Payment Plans: Introducing installment payment options to make purchases more manageable.

                2. Variety and Style
                - Trend Analysis: Regularly updating the collection to reflect current fashion trends while maintaining sustainability.
                - Collaborations: Partnering with influencers and designers to create exclusive, fashionable lines.

                3. Availability
                - Omni-Channel Presence: Expanding both online and offline presence to reach more consumers.
                - Pop-Up Stores: Hosting pop-up shops in various cities to increase visibility and accessibility.

                4. Building Trust
                - Transparency Initiatives: Providing detailed information about the sourcing and production of each item.
                - Certifications: Obtaining and showcasing certifications from credible sustainability organizations (e.g., GOTS, Fair Trade).

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
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


def get_marketing_engagement_strategies(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide detailed marketing and engagement strategies for the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Marketing and Engagement Strategies

                1. Social Media Campaigns
                - Educational Content: Sharing posts about the benefits of sustainable fashion and the brand’s sustainability practices.
                - User-Generated Content: Encouraging customers to share their sustainable fashion stories and outfits.

                2. Influencer Partnerships
                - Brand Ambassadors: Collaborating with eco-conscious influencers to promote the brand.
                - Giveaways and Challenges: Running social media contests to engage followers and increase brand awareness.

                3. Community Building
                - Sustainable Fashion Workshops: Hosting workshops and webinars on sustainable living and fashion.
                - Customer Loyalty Programs: Offering rewards for repeat purchases and referrals.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
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


def get_roadmap(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in business strategy and development, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed roadmap for the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Roadmap

                1. Idea Validation:
                - Market Research: Understand your target audience's needs. What are their pain points regarding sustainable fashion?
                - Customer Feedback: Create surveys or focus groups to gather insights directly from potential customers.

                2. Business Model Development:
                - Circular Economy: Consider implementing clothing rental or recycling programs. This can set you apart!
                - Revenue Streams: Explore different revenue models, such as subscription services or pop-up events.

                3. Mentorship and Networking:
                - Industry Events: Attend sustainable fashion conferences and events to meet industry experts.
                - Mentorship: Connect with successful entrepreneurs for guidance and inspiration.

                4. Funding and Resource Allocation:
                - Funding Options: Investigate impact investing, crowdfunding, and venture capital.
                - Resource Allocation: Focus on building a strong online presence and a robust marketing strategy.

                5. Timeline and Milestones:
                - MVP Development: Aim to create a minimum viable product (MVP) within 6 months.
                - Crowdfunding Campaign: Launch within 9 months to build a community and secure initial funding.
                - Scaling: Plan to scale your business within 12 months.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
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


def get_success_factors_metrics(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in business strategy and performance measurement, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of success factors and metrics for the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Success Factors and Metrics

                1. Key Performance Indicators (KPIs):
                - Website Traffic: Measure your online presence.
                - Social Media Engagement: Track interactions and growth.
                - Customer Acquisition Costs: Optimize your marketing spend.

                2. Success Factors:
                - Strong Brand Identity: Build a brand that resonates with your values and audience.
                - Loyal Customer Base: Engage and retain customers through excellent service and quality products.
                - Continuous Innovation: Keep improving and expanding your product line.

                3. Failure Analysis:
                - Learn from Others: Common pitfalls include poor market research, inadequate funding, and supply chain issues. Stay agile and adapt to changes.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
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


def get_research_subdomains_x(
    question, career_choice, business_idea, entrepreneurial_goals
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"can you suggest 15 research subdomains along with a small overview for each that would be relevant in the current Indian market scenario?"
                f"""format for generating 15 research subdomains:
                Example 1:
                1. **Sustainable Fashion Materials:** Exploring innovative materials that minimize environmental impact and promote sustainability in fashion.
                2. **Textile Recycling Technologies:** Developing efficient methods for recycling textiles to reduce waste and promote a circular economy.
                3. **Ethical Manufacturing Practices:** Investigating fair labor practices and sustainable production methods in the fashion industry.
                4. **Eco-Friendly Dyeing Techniques:** Creating dyeing processes that reduce water usage and pollution in textile manufacturing.
                5. **Circular Economy in Fashion:** Studying systems that encourage recycling and reuse of materials within the fashion industry.
                6. **Fashion Supply Chain Transparency:** Enhancing transparency in the supply chain to ensure ethical sourcing and production.
                7. **Zero Waste Fashion Design:** Designing clothing with minimal waste generation through innovative patterns and techniques.
                8. **Biodegradable Textiles:** Researching textiles that can naturally decompose without harming the environment.
                9. **Sustainable Fabric Innovations:** Developing new fabrics that are sustainable and eco-friendly.
                10. **Carbon Footprint Reduction in Fashion:** Strategies to reduce the carbon emissions associated with fashion production and distribution.
                11. **Water Conservation in Textile Production:** Techniques to minimize water use in the production of textiles.
                12. **Renewable Energy in Fashion Manufacturing:** Implementing renewable energy sources in fashion manufacturing processes.
                13. **Sustainable Apparel Marketing Strategies:** Effective marketing strategies that promote sustainable fashion.
                14. **Consumer Behavior Towards Sustainable Fashion:** Understanding consumer attitudes and behaviors towards sustainable fashion.
                15. **Impact of Technology on Sustainable Fashion:** How technology is transforming sustainable practices in the fashion industry.

                Example 2:
                1. **Renewable Energy Storage Solutions:** Innovative solutions for storing renewable energy efficiently.
                2. **Solar Power Innovations:** Advances in solar power technology to improve efficiency and accessibility.
                3. **Wind Energy Technologies:** New developments in wind energy to increase power generation.
                4. **Bioenergy and Biomass Conversion:** Researching methods to convert biomass into usable energy.
                5. **Smart Grid Technology:** Developing smart grid systems for efficient energy distribution and management.
                6. **Energy Efficiency in Buildings:** Techniques to enhance energy efficiency in residential and commercial buildings.
                7. **Green Hydrogen Production:** Exploring the production and use of green hydrogen as a clean energy source.
                8. **Electric Vehicle Charging Infrastructure:** Building and optimizing infrastructure for electric vehicle charging.
                9. **Waste-to-Energy Systems:** Converting waste materials into renewable energy.
                10. **Sustainable Energy Policies:** Analyzing and developing policies to support sustainable energy initiatives.
                11. **Microgrid Development:** Implementing microgrids for localized and resilient energy solutions.
                12. **Energy Harvesting Technologies:** Techniques to capture and store energy from various sources.
                13. **Ocean Energy Exploitation:** Harnessing energy from ocean waves and tides.
                14. **Geothermal Energy Utilization:** Exploring the potential of geothermal energy for power generation.
                15. **Impact of Climate Change on Renewable Energy:** Studying the effects of climate change on renewable energy resources and systems.

                Example 3:
                1. **Health Informatics:** Utilizing information technology to improve healthcare services and outcomes.
                2. **Telemedicine Solutions:** Developing remote healthcare solutions to increase accessibility.
                3. **Biomechanics in Rehabilitation:** Applying biomechanics to enhance rehabilitation techniques.
                4. **Medical Device Innovation:** Creating new medical devices to improve patient care.
                5. **Personalized Medicine:** Tailoring medical treatments to individual patient characteristics.
                6. **Health Data Analytics:** Using data analytics to improve healthcare decision-making.
                7. **Biomedical Imaging Techniques:** Advancing imaging techniques for better diagnosis and treatment.
                8. **AI in Healthcare Diagnostics:** Implementing artificial intelligence to enhance diagnostic accuracy.
                9. **Remote Patient Monitoring Systems:** Developing systems to monitor patients remotely and in real-time.
                10. **Health Wearables Development:** Creating wearable devices to track and improve health metrics.
                11. **Digital Health Platforms:** Building platforms to deliver healthcare services digitally.
                12. **Genomic Data Analysis:** Analyzing genomic data to inform medical research and treatment.
                13. **Drug Delivery Systems:** Innovating methods to deliver drugs more effectively.
                14. **Public Health Technology:** Leveraging technology to improve public health initiatives.
                15. **Mobile Health Applications:** Developing mobile apps to support health and wellness.

                Provide the research subdomains with a small overview. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_target_audience_analysis_x(
    question, career_choice, business_idea, entrepreneurial_goals, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the target audience's needs and pain points on the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Understanding the Target Audience's Needs and Pain Points

                1. Consumer Demographics
                - Age: Primarily 18-35 years old, tech-savvy, and environmentally conscious.
                - Location: Urban areas with high access to sustainable fashion options, suburban areas with growing interest, and rural areas with limited access but increasing awareness.
                - Income Level: Middle to upper-middle class with disposable income to spend on higher-priced sustainable goods, showing a willingness to invest in quality products.
                - Education Level: College-educated individuals who are well-informed about sustainability issues and seek out eco-friendly products.

                2. Consumer Preferences
                - Eco-Friendly Materials: High interest in clothing made from recycled, organic, or biodegradable materials such as organic cotton, hemp, and recycled polyester.
                - Transparency: Consumers want detailed information about production processes, sourcing of materials, and labor practices.
                - Ethical Production: Strong preference for brands that ensure fair wages, safe working conditions, and minimal environmental impact.
                - Durability and Quality: Consumers expect sustainable fashion to be durable, high-quality, and justify the higher price through longevity and performance.

                3. Pain Points
                - High Cost: Sustainable fashion is often more expensive than fast fashion, which can deter some consumers. Possible solutions include offering sliding scale pricing, payment plans, and highlighting long-term savings.
                - Limited Options: Consumers may perceive sustainable fashion as offering fewer style choices compared to traditional fashion. Addressing this can involve regularly updating collections and collaborating with designers.
                - Availability: Consumers face challenges in finding sustainable fashion brands in physical stores. Improving availability can involve expanding online presence and hosting pop-up shops in various cities.
                - Greenwashing: Consumers are wary of brands falsely claiming to be sustainable. Building trust can involve obtaining credible certifications and providing transparent information about practices."""
                f"Make sure to provide detailed insights and explanations for each of the points consumer demographics, consumer preferences, pain points. Do not provide a heading.",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_data_insights_x(
    question, career_choice, business_idea, entrepreneurial_goals, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of data and insights on the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Data and Insights

                1. Survey Results and Studies
                - Global Data Survey (2021): 75% of millennials are willing to pay more for sustainable products.
                - McKinsey & Company (2020): 57% of consumers have made significant changes to their lifestyles to reduce their environmental impact.

                2. Trends
                - Rise of Circular Fashion: Increasing consumer interest in renting, swapping, and recycling clothes.
                - Technology Integration: Use of digital platforms to promote transparency and traceability (e.g., blockchain).

                3. Competitive Analysis
                - Key Competitors: Patagonia, Reformation, Everlane.
                - New Entrants: ThredUp, Poshmark.
                - Strengths of Competitors: Strong brand identity, loyal customer base, continuous innovation in sustainable practices.
                - Weaknesses of Competitors: High prices, limited physical presence, potential greenwashing issues.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_strategies_to_address_pain_points_x(
    question, career_choice, business_idea, entrepreneurial_goals, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide detailed strategies to address pain points in the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Strategies to Address Pain Points

                1. Affordability
                - Sliding Scale Pricing: Offering products at various price points to cater to different income levels.
                - Payment Plans: Introducing installment payment options to make purchases more manageable.

                2. Variety and Style
                - Trend Analysis: Regularly updating the collection to reflect current fashion trends while maintaining sustainability.
                - Collaborations: Partnering with influencers and designers to create exclusive, fashionable lines.

                3. Availability
                - Omni-Channel Presence: Expanding both online and offline presence to reach more consumers.
                - Pop-Up Stores: Hosting pop-up shops in various cities to increase visibility and accessibility.

                4. Building Trust
                - Transparency Initiatives: Providing detailed information about the sourcing and production of each item.
                - Certifications: Obtaining and showcasing certifications from credible sustainability organizations (e.g., GOTS, Fair Trade).

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_marketing_engagement_strategies_x(
    question, career_choice, business_idea, entrepreneurial_goals, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide detailed marketing and engagement strategies for the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Marketing and Engagement Strategies

                1. Social Media Campaigns
                - Educational Content: Sharing posts about the benefits of sustainable fashion and the brand’s sustainability practices.
                - User-Generated Content: Encouraging customers to share their sustainable fashion stories and outfits.

                2. Influencer Partnerships
                - Brand Ambassadors: Collaborating with eco-conscious influencers to promote the brand.
                - Giveaways and Challenges: Running social media contests to engage followers and increase brand awareness.

                3. Community Building
                - Sustainable Fashion Workshops: Hosting workshops and webinars on sustainable living and fashion.
                - Customer Loyalty Programs: Offering rewards for repeat purchases and referrals.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_roadmap_x(
    question, career_choice, business_idea, entrepreneurial_goals, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in business strategy and development, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed roadmap for the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Roadmap

                1. Idea Validation:
                - Market Research: Understand your target audience's needs. What are their pain points regarding sustainable fashion?
                - Customer Feedback: Create surveys or focus groups to gather insights directly from potential customers.

                2. Business Model Development:
                - Circular Economy: Consider implementing clothing rental or recycling programs. This can set you apart!
                - Revenue Streams: Explore different revenue models, such as subscription services or pop-up events.

                3. Mentorship and Networking:
                - Industry Events: Attend sustainable fashion conferences and events to meet industry experts.
                - Mentorship: Connect with successful entrepreneurs for guidance and inspiration.

                4. Funding and Resource Allocation:
                - Funding Options: Investigate impact investing, crowdfunding, and venture capital.
                - Resource Allocation: Focus on building a strong online presence and a robust marketing strategy.

                5. Timeline and Milestones:
                - MVP Development: Aim to create a minimum viable product (MVP) within 6 months.
                - Crowdfunding Campaign: Launch within 9 months to build a community and secure initial funding.
                - Scaling: Plan to scale your business within 12 months.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_success_factors_metrics_x(
    question, career_choice, business_idea, entrepreneurial_goals, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in business strategy and performance measurement, "
                f"with a business idea of {business_idea} and entrepreneurial goals of {entrepreneurial_goals}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of success factors and metrics for the research subdomain {selected_subdomain},"
                f"""Example of a response:
                Success Factors and Metrics

                1. Key Performance Indicators (KPIs):
                - Website Traffic: Measure your online presence.
                - Social Media Engagement: Track interactions and growth.
                - Customer Acquisition Costs: Optimize your marketing spend.

                2. Success Factors:
                - Strong Brand Identity: Build a brand that resonates with your values and audience.
                - Loyal Customer Base: Engage and retain customers through excellent service and quality products.
                - Continuous Innovation: Keep improving and expanding your product line.

                3. Failure Analysis:
                - Learn from Others: Common pitfalls include poor market research, inadequate funding, and supply chain issues. Stay agile and adapt to changes.

                Make sure to provide detailed insights and explanations for each point. Do not provide a heading.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        career_choice=career_choice,
        business_idea=business_idea,
        entrepreneurial_goals=entrepreneurial_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_industry_requirements(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Industry Requirements of the industry subdomain {selected_subdomain},"
                f"""Example of a response:
                Industry Requirements

                1. Key technical skills:
                - Programming languages: Python, C++, Java
                - Software tools: Familiarity with security frameworks and tools such as Nmap, Nessus, and Burp Suite

                2. Certifications:
                - CompTIA Security+
                - Certified Information Systems Security Professional (CISSP)

                3. Experience level:
                - Entry-level
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


def get_job_titles(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the job roles and descriptions on the industry subdomain {selected_subdomain},"
                f"""Example of a response:
                Job Roles and Descriptions

                1. Job titles and descriptions:
                - Cybersecurity Analyst: Responsible for monitoring and analysing security threats, implementing security measures, and conducting vulnerability assessments
                - Senior Cybersecurity Consultant: Leads cybersecurity projects, develops security strategies, and provides expert advice to clients

                2. Responsibilities:
                - Cybersecurity Analyst: Conduct threat analysis, implement security patches, and monitor network activity
                - Senior Cybersecurity Consultant: Develop security policies, conduct risk assessments, and provide training to clients

                3. Salary ranges:
                - Cybersecurity Analyst: $70,000 - $90,000 per year
                - Senior Cybersecurity Consultant: $120,000 - $150,000 per year
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


def get_industry_trends(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the industry trends and outlook of the industry subdomain {selected_subdomain},"
                f"""Example of a response:
                Industry Trends and Outlook

                1. Growth rates: 18% growth rate from 2023 to 2028

                2. Emerging trends: Artificial Intelligence-powered security solutions, Cloud Security, and Internet of Things (IoT) security
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


def get_roadmap_attributes(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the roadmap attributes of the subdomain {selected_subdomain},"
                f"""Example of a response:
                Roadmap Attributes

                1. Milestones and Objectives:
                - Month 3: Complete online courses in Python programming and security frameworks
                - Month 6: Gain experience with security tools and software through hands-on projects
                - Month 9: Develop a portfolio of cybersecurity projects and present to industry professionals
                - Month 12: Land a Cybersecurity Analyst role and continue learning and developing skills

                2. Skills and Knowledge Gaps:
                - Technical skills: Python, C++, Java, security frameworks and tools
                - Soft skills: Communication, problem-solving, teamwork

                3. Education and Training:
                - Online courses: Python for Cybersecurity, Security Frameworks and Tools
                - Certifications: CompTIA Security+, CISSP
                - Bootcamps or workshops: Cybersecurity Bootcamp

                4. Networking Opportunities:
                - Conferences and meetups: Attend Cybersecurity conferences and meetups
                - Online communities: Join online communities such as Reddit (r/cybersecurity), LinkedIn groups, and Cybersecurity forums

                5. Timeframe and Deadlines:
                - Specific deadlines: Month 3: Complete online courses, Month 6: Finish hands-on projects
                - Timeframe for overall goals: 12 months for landing a Cybersecurity Analyst role, 5 years for becoming a Senior Cybersecurity Consultant
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


def get_industry_requirements_x(
    question,
    degree_and_field_of_study,
    desired_industry,
    career_goals,
    selected_subdomain,
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {desired_industry}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Industry Requirements of the industry subdomain {selected_subdomain} for a student with a degree in {degree_and_field_of_study} aiming for career goals in {career_goals},"
                f"""Example of a response:
                Industry Requirements

                1. Key technical skills:
                - Programming languages: Python, C++, Java
                - Software tools: Familiarity with security frameworks and tools such as Nmap, Nessus, and Burp Suite

                2. Certifications:
                - CompTIA Security+
                - Certified Information Systems Security Professional (CISSP)

                3. Experience level:
                - Entry-level
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        desired_industry=desired_industry,
        career_goals=career_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_job_titles_x(
    question,
    degree_and_field_of_study,
    desired_industry,
    career_goals,
    selected_subdomain,
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {desired_industry}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the job roles and descriptions on the industry subdomain {selected_subdomain} for a student with a degree in {degree_and_field_of_study} aiming for career goals in {career_goals},"
                f"""Example of a response:
                Job Roles and Descriptions

                1. Job titles and descriptions:
                - Cybersecurity Analyst: Responsible for monitoring and analysing security threats, implementing security measures, and conducting vulnerability assessments
                - Senior Cybersecurity Consultant: Leads cybersecurity projects, develops security strategies, and provides expert advice to clients

                2. Responsibilities:
                - Cybersecurity Analyst: Conduct threat analysis, implement security patches, and monitor network activity
                - Senior Cybersecurity Consultant: Develop security policies, conduct risk assessments, and provide training to clients

                3. Salary ranges:
                - Cybersecurity Analyst: $70,000 - $90,000 per year
                - Senior Cybersecurity Consultant: $120,000 - $150,000 per year
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        desired_industry=desired_industry,
        career_goals=career_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_industry_trends_x(
    question,
    degree_and_field_of_study,
    desired_industry,
    career_goals,
    selected_subdomain,
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {desired_industry}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the industry trends and outlook of the industry subdomain {selected_subdomain} for a student with a degree in {degree_and_field_of_study} aiming for career goals in {career_goals},"
                f"""Example of a response:
                Industry Trends and Outlook

                1. Growth rates: 18% growth rate from 2023 to 2028

                2. Emerging trends: Artificial Intelligence-powered security solutions, Cloud Security, and Internet of Things (IoT) security
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        desired_industry=desired_industry,
        career_goals=career_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_roadmap_attributes_x(
    question,
    degree_and_field_of_study,
    desired_industry,
    career_goals,
    selected_subdomain,
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {desired_industry}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the roadmap attributes of the subdomain {selected_subdomain} for a student with a degree in {degree_and_field_of_study} aiming for career goals in {career_goals},"
                f"""Example of a response:
                Roadmap Attributes

                1. Milestones and Objectives:
                - Month 3: Complete online courses in Python programming and security frameworks
                - Month 6: Gain experience with security tools and software through hands-on projects
                - Month 9: Develop a portfolio of cybersecurity projects and present to industry professionals
                - Month 12: Land a Cybersecurity Analyst role and continue learning and developing skills

                2. Skills and Knowledge Gaps:
                - Technical skills: Python, C++, Java, security frameworks and tools
                - Soft skills: Communication, problem-solving, teamwork

                3. Education and Training:
                - Online courses: Python for Cybersecurity, Security Frameworks and Tools
                - Certifications: CompTIA Security+, CISSP
                - Bootcamps or workshops: Cybersecurity Bootcamp

                4. Networking Opportunities:
                - Conferences and meetups: Attend Cybersecurity conferences and meetups
                - Online communities: Join online communities such as Reddit (r/cybersecurity), LinkedIn groups, and Cybersecurity forums

                5. Timeframe and Deadlines:
                - Specific deadlines: Month 3: Complete online courses, Month 6: Finish hands-on projects
                - Timeframe for overall goals: 12 months for landing a Cybersecurity Analyst role, 5 years for becoming a Senior Cybersecurity Consultant
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        desired_industry=desired_industry,
        career_goals=career_goals,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_higher_education_program_attributes(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Higher Education Program Attributes for the subdomain {selected_subdomain},"
                f"""Example of a response:
                Higher Education Program Attributes

                1. Program Types:
                - Master’s Programs: Typically, 1-2 years, focusing on advanced data science skills and practical experience. Available in both thesis and non-thesis formats.
                - Ph.D. Programs: Generally, 3-5 years, emphasizing original research and contributions to the field of data science.

                2. Program Specializations:
                - Data Science: Includes courses on machine learning, data mining, and statistical analysis.
                - Artificial Intelligence: Covers advanced AI techniques, deep learning, and neural networks.

                3. Program Duration:
                - Full-time Programs: Standard duration of 1-2 years for a Master’s degree.
                - Part-time Programs: Extended duration to accommodate working professionals.

                4. Program Format:
                - Online Programs: Offers flexibility for remote learning. Institutions like Georgia Tech and UC Berkeley provide online Master’s in Data Science.
                - Offline Programs: Requires physical attendance, such as at Carnegie Mellon University or University College London.
                - Hybrid Programs: Combines online and in-person coursework.

                5. Program Fees and Costs:
                - Tuition Fees: Range from $15,000 to $30,000 per year, depending on the institution.
                - Living Costs: Estimated $15,000 to $20,000 per year in urban areas.
                - Additional Costs: Includes textbooks, lab fees, and health insurance.
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


def get_market_and_economic_attributes(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Market and Economic Attributes for the subdomain {selected_subdomain},"
                f"""Example of a response:
                Market and Economic Attributes

                1. Current Market Trends:
                - Emerging Fields: Growing demand for data science professionals in tech, finance, and healthcare.
                - Shifting Educational Preferences: Increasing popularity of online and hybrid programs.

                2. Economic Indicators:
                - GDP Growth: Growth in tech-centric economies such as the US and UK.
                - Inflation Rate: Consideration of inflation to plan for living expenses and tuition.

                3. Industry Outlook:
                - Growth Prospects: High demand for data science skills, with a projected 30% job growth rate over the next decade.
                - Challenges and Opportunities: Need to stay updated with rapidly evolving technologies and methodologies.

                4. Competitive Landscape:
                - Top Institutions: Massachusetts Institute of Technology (MIT), Stanford University, and University of Oxford.
                - Program Features: Strong emphasis on practical projects, industry connections, and research opportunities.
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


def get_academic_skills_and_knowledge_attributes(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Academic Skills and Knowledge Attributes for the subdomain {selected_subdomain},"
                f"""Example of a response:
                Academic Skills and Knowledge Attributes

                1. Program Planning:
                - Market Research: Identify institutions with strong data science programs and good industry connections.
                - Financial Projections: Create a budget plan covering tuition, living expenses, and additional costs.

                2. Application Strategy:
                - Test Preparation: Prepare for GRE (if required) and other standardized tests.
                - Statement of Purpose: Craft a detailed statement explaining your interest in data science, career goals, and fit with the program.
                - Document Collection: Gather transcripts, recommendation letters, and test scores.

                3. Funding and Financial Management:
                - Funding Options: Apply for scholarships, research assistantships, and explore student loans if necessary.
                - Budget Management: Monitor spending and adjust as needed to stay within budget.

                4. Leadership and Networking:
                - Academic Networking: Attend data science conferences and seminars to connect with professionals and academics.
                - Academic Mentors: Seek advice from professors and industry experts for guidance on research and career development.
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


def get_academic_roadmap_attributes(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Roadmap Attributes for the subdomain {selected_subdomain},"
                f"""Example of a response:
                Roadmap Attributes

                1. Idea Validation:
                - Program Research: Evaluate programs based on curriculum, faculty, and industry connections.
                - Feedback and Testing: Obtain feedback from current students or alumni regarding program quality and opportunities.

                2. Program Selection:
                - Shortlisting Programs: Create a list of preferred programs based on research and personal criteria.
                - Application Requirements: Ensure all application materials are complete and submitted by the deadlines.

                3. Mentorship and Networking:
                - Industry Events: Participate in data science and tech industry events to build connections and gain insights.
                - Academic Mentors: Reach out to potential mentors for advice and support.

                4. Funding and Resource Allocation:
                - Scholarship Applications: Apply for relevant scholarships and financial aid opportunities.
                - Resource Management: Allocate resources for application fees, test preparation, and other costs.

                5. Timeline and Milestones:
                - Application Preparation: Complete applications by set deadlines, typically 6-12 months before the program starts.
                - Funding Campaign: Secure funding and financial aid before finalizing enrolment.
                - Enrolment: Finalize enrolment and prepare for the start of the program.
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


def get_success_factors_and_metrics_higher(
    question, engineering_stream, career_choice, domain_sector, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's interest in {domain_sector}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Success Factors and Metrics for the subdomain {selected_subdomain},"
                f"""Example of a response:
                Success Factors and Metrics

                1. Key Performance Indicators (KPIs):
                - Application Success Rate: Track acceptance rates and program offers.
                - Financial Aid Secured: Measure the amount of funding received.
                - Program Fit: Assess how well the program aligns with academic and career goals.

                2. Success Factors:
                - Program Quality: Choose programs with a strong reputation and relevant industry connections.
                - Academic Performance: Maintain high performance and engage in research opportunities.
                - Networking: Build a strong network of peers, mentors, and industry professionals.

                3. Failure Analysis:
                - Common Pitfalls: Address issues such as missed deadlines, insufficient funding, and lack of program fit. Remain flexible and proactive in overcoming challenges.
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


def get_higher_education_program_attributes_x(
    question, degree_and_field_of_study, preferred_location, budget, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's preference for {preferred_location} and interest in {degree_and_field_of_study}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Higher Education Program Attributes for the subdomain {selected_subdomain} within a budget of {budget},"
                f"""Example of a response:
                Higher Education Program Attributes

                1. Program Types:
                - Master’s Programs: Typically, 1-2 years, focusing on advanced data science skills and practical experience. Available in both thesis and non-thesis formats.
                - Ph.D. Programs: Generally, 3-5 years, emphasizing original research and contributions to the field of data science.

                2. Program Specializations:
                - Data Science: Includes courses on machine learning, data mining, and statistical analysis.
                - Artificial Intelligence: Covers advanced AI techniques, deep learning, and neural networks.

                3. Program Duration:
                - Full-time Programs: Standard duration of 1-2 years for a Master’s degree.
                - Part-time Programs: Extended duration to accommodate working professionals.

                4. Program Format:
                - Online Programs: Offers flexibility for remote learning. Institutions like Georgia Tech and UC Berkeley provide online Master’s in Data Science.
                - Offline Programs: Requires physical attendance, such as at Carnegie Mellon University or University College London.
                - Hybrid Programs: Combines online and in-person coursework.

                5. Program Fees and Costs:
                - Tuition Fees: Range from $15,000 to $30,000 per year, depending on the institution.
                - Living Costs: Estimated $15,000 to $20,000 per year in urban areas.
                - Additional Costs: Includes textbooks, lab fees, and health insurance.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        preferred_location=preferred_location,
        budget=budget,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_market_and_economic_attributes_x(
    question, degree_and_field_of_study, preferred_location, budget, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's preference for {preferred_location} and interest in {degree_and_field_of_study}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Market and Economic Attributes for the subdomain {selected_subdomain} within a budget of {budget},"
                f"""Example of a response:
                Market and Economic Attributes

                1. Current Market Trends:
                - Emerging Fields: Growing demand for data science professionals in tech, finance, and healthcare.
                - Shifting Educational Preferences: Increasing popularity of online and hybrid programs.

                2. Economic Indicators:
                - GDP Growth: Growth in tech-centric economies such as the US and UK.
                - Inflation Rate: Consideration of inflation to plan for living expenses and tuition.

                3. Industry Outlook:
                - Growth Prospects: High demand for data science skills, with a projected 30% job growth rate over the next decade.
                - Challenges and Opportunities: Need to stay updated with rapidly evolving technologies and methodologies.

                4. Competitive Landscape:
                - Top Institutions: Massachusetts Institute of Technology (MIT), Stanford University, and University of Oxford.
                - Program Features: Strong emphasis on practical projects, industry connections, and research opportunities.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        preferred_location=preferred_location,
        budget=budget,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_academic_skills_and_knowledge_attributes_x(
    question, degree_and_field_of_study, preferred_location, budget, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's preference for {preferred_location} and interest in {degree_and_field_of_study}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Academic Skills and Knowledge Attributes for the subdomain {selected_subdomain} within a budget of {budget},"
                f"""Example of a response:
                Academic Skills and Knowledge Attributes

                1. Program Planning:
                - Market Research: Identify institutions with strong data science programs and good industry connections.
                - Financial Projections: Create a budget plan covering tuition, living expenses, and additional costs.

                2. Application Strategy:
                - Test Preparation: Prepare for GRE (if required) and other standardized tests.
                - Statement of Purpose: Craft a detailed statement explaining your interest in data science, career goals, and fit with the program.
                - Document Collection: Gather transcripts, recommendation letters, and test scores.

                3. Funding and Financial Management:
                - Funding Options: Apply for scholarships, research assistantships, and explore student loans if necessary.
                - Budget Management: Monitor spending and adjust as needed to stay within budget.

                4. Leadership and Networking:
                - Academic Networking: Attend data science conferences and seminars to connect with professionals and academics.
                - Academic Mentors: Seek advice from professors and industry experts for guidance on research and career development.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        preferred_location=preferred_location,
        budget=budget,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_academic_roadmap_attributes_x(
    question, degree_and_field_of_study, preferred_location, budget, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's preference for {preferred_location} and interest in {degree_and_field_of_study}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Roadmap Attributes for the subdomain {selected_subdomain} within a budget of {budget},"
                f"""Example of a response:
                Roadmap Attributes

                1. Idea Validation:
                - Program Research: Evaluate programs based on curriculum, faculty, and industry connections.
                - Feedback and Testing: Obtain feedback from current students or alumni regarding program quality and opportunities.

                2. Program Selection:
                - Shortlisting Programs: Create a list of preferred programs based on research and personal criteria.
                - Application Requirements: Ensure all application materials are complete and submitted by the deadlines.

                3. Mentorship and Networking:
                - Industry Events: Participate in data science and tech industry events to build connections and gain insights.
                - Academic Mentors: Reach out to potential mentors for advice and support.

                4. Funding and Resource Allocation:
                - Scholarship Applications: Apply for relevant scholarships and financial aid opportunities.
                - Resource Management: Allocate resources for application fees, test preparation, and other costs.

                5. Timeline and Milestones:
                - Application Preparation: Complete applications by set deadlines, typically 6-12 months before the program starts.
                - Funding Campaign: Secure funding and financial aid before finalizing enrolment.
                - Enrolment: Finalize enrolment and prepare for the start of the program.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        preferred_location=preferred_location,
        budget=budget,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


def get_success_factors_and_metrics_x_higher(
    question, degree_and_field_of_study, preferred_location, budget, selected_subdomain
):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"As an experienced professional in market analysis, "
                f"considering a student's preference for {preferred_location} and interest in {degree_and_field_of_study}, "
                f"and focusing on the selected research subdomain {selected_subdomain}, "
                f"provide a detailed analysis of the Success Factors and Metrics for the subdomain {selected_subdomain} within a budget of {budget},"
                f"""Example of a response:
                Success Factors and Metrics

                1. Key Performance Indicators (KPIs):
                - Application Success Rate: Track acceptance rates and program offers.
                - Financial Aid Secured: Measure the amount of funding received.
                - Program Fit: Assess how well the program aligns with academic and career goals.

                2. Success Factors:
                - Program Quality: Choose programs with a strong reputation and relevant industry connections.
                - Academic Performance: Maintain high performance and engage in research opportunities.
                - Networking: Build a strong network of peers, mentors, and industry professionals.

                3. Failure Analysis:
                - Common Pitfalls: Address issues such as missed deadlines, insufficient funding, and lack of program fit. Remain flexible and proactive in overcoming challenges.
                """,
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        degree_and_field_of_study=degree_and_field_of_study,
        preferred_location=preferred_location,
        budget=budget,
        user_input=question,
    )

    response = model.invoke(formatted_messages)
    return response


load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyDPow8LG1uOOHG5kj8a2axfdbJ4qTxZxbs"))
model = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro", convert_system_message_to_human=True
)

st.header("Research Mate")
st.write(
    "Access essential insights on entrepreneurship, higher education, and industry trends. This portal equips you with the knowledge and tools to succeed in your academic and professional journey."
)

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

fixed_question_mrm = "help the student by listing 15 research subdomains positions specific to the {domain_sector} that would be relevant in the current Indian market scenario."

show_select_box = False

show_select_box = False

show_select_box = False


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

if "courses_list_arm" not in st.session_state:
    st.session_state.courses_list_arm = ""  

if "courses_list_irm" not in st.session_state:
    st.session_state.courses_list_irm = ""
st.write("---")

user_flow_choice = st.selectbox(
    "User Flow Choice:",
    ["Generate Ideas", "Enter Your Idea"],
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

if user_flow_choice == "Generate Ideas":

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
        ["Entrepreneurship", "Placements", "Higher Studies"],
        key="career_choice",
    )

    if career_choice == "Entrepreneurship":
        st.session_state.selected_application = ""
        st.session_state.subdomain_selected = False
        if st.button("Generate Subdomains"):
            st.session_state.job_profile_content = ""
            st.session_state.job_profile_shown = False
            st.session_state.applications = []
            st.session_state.courses_list = ""
            st.session_state.selected_subdomain = ""
            st.session_state.courses_list_shown = False
            st.session_state.courses = []
            st.session_state.course_list_stripped = False
            st.session_state.selected_coursee = ""
            st.session_state.course_selected = True
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            response = get_research_subdomains(
                fixed_question_mrm, engineering_stream, career_choice, domain_sector
            )

            x = response.content

            words = [line.split(":")[0].strip() for line in x.split("\n")]
            applications = [
                word.lstrip(".*0123456789 ").strip() for word in words if word
            ]
            print(applications)

            st.session_state.job_profile_content = response.content
            st.session_state.job_profile_shown = True

            st.session_state.applications = applications

        if st.session_state.applications and st.session_state.job_profile_content:
            st.write("---")
            st.subheader("Here are 15 Subdomains for you: ")
            st.write(st.session_state.job_profile_content)

        if (
            "applications" in st.session_state
            and st.session_state.applications
            and st.session_state.job_profile_shown
        ):
            st.write("---")
            st.subheader("Choose a Subdomain which interests you:")
            st.session_state.selected_subdomain = st.selectbox(
                "Select a Subdomain:",
                st.session_state.applications,
                key="selected_sub",
            )
            st.session_state.subdomain_selected = True

        if st.session_state.subdomain_selected:
            if st.button("Generate Market Report"):

                st.session_state.courses_list = ""
                st.session_state.courses_list_shown = False
                st.session_state.courses = []
                st.session_state.course_list_stripped = False
                st.session_state.selected_coursee = ""
                st.session_state.course_selected = True
                st.session_state.course_outline_content = ""
                st.session_state.course_outline_shown = False
                st.session_state.data_insights = ""
                st.session_state.strategy = ""
                st.session_state.marketing = ""
                st.session_state.roadmap = ""
                st.session_state.success = ""
                response_coursess = get_target_audience_analysis(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_data = get_data_insights(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_strategies = get_strategies_to_address_pain_points(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_marketing = get_marketing_engagement_strategies(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_roadmap = get_roadmap(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_success = get_success_factors_metrics(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                st.session_state.success = response_success.content
                st.session_state.roadmap = response_roadmap.content
                st.session_state.marketing = response_marketing.content
                st.session_state.strategy = response_strategies.content
                st.session_state.data_insights = response_data.content
                st.session_state.courses_list = response_coursess.content
                st.session_state.courses_list_shown = True

        if st.session_state.courses_list:
            st.write("---")
            st.subheader("Target audience Analysis")
            st.write(st.session_state.courses_list)
            st.write("---")
            st.subheader("Data Insights")
            st.write(st.session_state.data_insights)
            st.write("---")
            st.subheader("Strategies to Address Pain Points")
            st.write(st.session_state.strategy)
            st.write("---")
            st.subheader("Marketing and Engagement Strategies")
            st.write(st.session_state.marketing)
            st.write("---")
            st.subheader("Roadmap")
            st.write(st.session_state.roadmap)
            st.write("---")
            st.subheader("Success Factors and Metrics")
            st.write(st.session_state.success)
            st.write("---")
            if st.button("Save Generated Text"):
                email = st.session_state.email
                bruh(email, "Research Engine", user_flow_choice, career_choice)

    elif career_choice == "Placements":
        st.session_state.selected_application = ""
        st.session_state.subdomain_selected = False
        if st.button("Generate Subdomains"):
            st.session_state.job_profile_content = ""
            st.session_state.job_profile_shown = False
            st.session_state.applications = []
            st.session_state.courses_list = ""
            st.session_state.selected_subdomain = ""
            st.session_state.courses_list_shown = False
            st.session_state.courses = []
            st.session_state.course_list_stripped = False
            st.session_state.selected_coursee = ""
            st.session_state.course_selected = True
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            response = get_research_subdomains(
                fixed_question_mrm, engineering_stream, career_choice, domain_sector
            )

            x = response.content

            words = [line.split(":")[0].strip() for line in x.split("\n")]
            applications = [
                word.lstrip(".*0123456789 ").strip() for word in words if word
            ]
            print(applications)

            st.session_state.job_profile_content = response.content
            st.session_state.job_profile_shown = True

            st.session_state.applications = applications

        if st.session_state.applications and st.session_state.job_profile_content:
            st.write("---")
            st.subheader("Here are 15 Subdomains for you: ")
            st.write(st.session_state.job_profile_content)

        if (
            "applications" in st.session_state
            and st.session_state.applications
            and st.session_state.job_profile_shown
        ):
            st.write("---")
            st.subheader("Choose a Subdomain which interests you:")
            st.session_state.selected_subdomain = st.selectbox(
                "Select a Subdomain:",
                st.session_state.applications,
                key="selected_sub",
            )
            st.session_state.subdomain_selected = True

        if st.session_state.subdomain_selected:
            if st.button("Generate Industry Report"):

                st.session_state.courses_list = ""
                st.session_state.courses_list_shown = False
                st.session_state.courses = []
                st.session_state.course_list_stripped = False
                st.session_state.selected_coursee = ""
                st.session_state.course_selected = True
                st.session_state.course_outline_content = ""
                st.session_state.course_outline_shown = False
                st.session_state.job_titles = ""
                st.session_state.industry = ""
                st.session_state.roadmap_attributes = ""

                response_coursess = get_industry_requirements(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_job = get_job_titles(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_industry = get_industry_trends(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_roadmap_attr = get_roadmap_attributes(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )

                st.session_state.roadmap_attributes = response_roadmap_attr.content
                st.session_state.industry = response_industry.content
                st.session_state.job_titles = response_job.content
                st.session_state.courses_list = response_coursess.content
                st.session_state.courses_list_shown = True

        if st.session_state.courses_list:
            st.write("---")
            st.subheader("Industry Requirements")
            st.write(st.session_state.courses_list)
            st.write("---")
            st.subheader("Job Roles and Descriptions")
            st.write(st.session_state.job_titles)
            st.write("---")
            st.subheader("Industry Trends and Outlook")
            st.write(st.session_state.industry)
            st.write("---")
            st.subheader("Roadmap Attributes")
            st.write(st.session_state.roadmap_attributes)
            st.write("---")

            if st.button("Save Generated Text"):
                email = st.session_state.email
                bruh(email, "Research Engine", user_flow_choice, career_choice)

    else:
        st.session_state.selected_application = ""
        st.session_state.subdomain_selected = False
        if st.button("Generate Subdomains"):
            st.session_state.job_profile_content = ""
            st.session_state.job_profile_shown = False
            st.session_state.applications = []
            st.session_state.courses_list = ""
            st.session_state.selected_subdomain = ""
            st.session_state.courses_list_shown = False
            st.session_state.courses = []
            st.session_state.course_list_stripped = False
            st.session_state.selected_coursee = ""
            st.session_state.course_selected = True
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            response = get_research_subdomains(
                fixed_question_mrm, engineering_stream, career_choice, domain_sector
            )

            x = response.content

            words = [line.split(":")[0].strip() for line in x.split("\n")]
            applications = [
                word.lstrip(".*0123456789 ").strip() for word in words if word
            ]
            print(applications)

            st.session_state.job_profile_content = response.content
            st.session_state.job_profile_shown = True

            st.session_state.applications = applications

        if st.session_state.applications and st.session_state.job_profile_content:
            st.write("---")
            st.subheader("Here are 15 Subdomains for you: ")
            st.write(st.session_state.job_profile_content)

        if (
            "applications" in st.session_state
            and st.session_state.applications
            and st.session_state.job_profile_shown
        ):
            st.write("---")
            st.subheader("Choose a Subdomain which interests you:")
            st.session_state.selected_subdomain = st.selectbox(
                "Select a Subdomain:",
                st.session_state.applications,
                key="selected_sub",
            )
            st.session_state.subdomain_selected = True

        if st.session_state.subdomain_selected:
            if st.button("Generate Academic Report"):

                st.session_state.courses_list = ""
                st.session_state.courses_list_shown = False
                st.session_state.courses = []
                st.session_state.course_list_stripped = False
                st.session_state.selected_coursee = ""
                st.session_state.course_selected = True
                st.session_state.course_outline_content = ""
                st.session_state.course_outline_shown = False
                st.session_state.market = ""
                st.session_state.academic = ""
                st.session_state.roadmap_attributes = ""
                st.session_state.success = ""

                response_coursess = get_higher_education_program_attributes(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_market = get_market_and_economic_attributes(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_academic = get_academic_skills_and_knowledge_attributes(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_roadmap_attr = get_academic_roadmap_attributes(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )
                response_success = get_success_factors_and_metrics_higher(
                    st.session_state.selected_subdomain,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                    st.session_state.selected_subdomain,
                )

                st.session_state.success = response_success.content
                st.session_state.roadmap_attributes = response_roadmap_attr.content
                st.session_state.academic = response_academic.content
                st.session_state.market = response_market.content
                st.session_state.courses_list = response_coursess.content
                st.session_state.courses_list_shown = True

        if st.session_state.courses_list:
            st.write("---")
            st.subheader("Higher Education Program Attributes")
            st.write(st.session_state.courses_list)
            st.write("---")
            st.subheader("Market and Economic Attributes")
            st.write(st.session_state.market)
            st.write("---")
            st.subheader("Academic Skills and Knowledge Attributes")
            st.write(st.session_state.academic)
            st.write("---")
            st.subheader("Roadmap Attributes")
            st.write(st.session_state.roadmap_attributes)
            st.write("---")
            st.subheader("Success Factors and Metrics")
            st.write(st.session_state.success)
            st.write("---")

            if st.button("Save Generated Text"):
                email = st.session_state.email
                bruh(email, "Research Engine", user_flow_choice, career_choice)

else:
    xflag = False
    
    tempp = """"""
    st.session_state.designation_entered = False
    st.session_state.job_designation = ""
    st.session_state.type_entered = False
    st.session_state.goals = ""
    st.session_state.selected_application_mrm = ""
    st.session_state.degree_and_field_of_study = ""
    st.session_state.subdomain = ""
    st.session_state.location = ""
    st.session_state.budget = ""
    st.session_state.desired_industry = ""
    st.session_state.everything_shown = False
    
    selected_type = st.selectbox(
        "Select type of research:",
        ["MRM", "ARM", "IRM"],
        key="selected_type",
    )
    def reset_shown():
        st.session_state.everything_shown = False
    
    st.session_state.everything_shown = False
    
    # st.session_state.courses_list_shown = False
    if selected_type == "MRM":
     career_choice = "Entrepreneurship"
    elif selected_type == "ARM":
     career_choice = "Higher Studies"
    elif selected_type == "IRM":
     career_choice = "Placements"
    st.session_state.type_selected = selected_type
    st.session_state.type_entered = True    
    
    if st.session_state.type_entered:
        if st.session_state.type_selected == "MRM":
            st.session_state.job_designation = st.text_input(
                "Enter Business Idea:",
                key="job_designatiASDASDon",
                placeholder="Create a clothing line using recycled materials.",
            )

            st.session_state.goals = st.text_input(
                "Enter your goals:",
                key="goSDFSDFals",
                placeholder="I want to start a sustainable fashion brand.",
            )

            st.session_state.selected_application_mrm = st.text_input(
                "Enter the subdomain:",
                key="subdomaindkaj;f;lkadsf",
                placeholder="Fashion and Apparel.",
            )
            # st.session_state.selected_application = subdomain
            st.session_state.designation_entered = True
        elif st.session_state.type_selected == "IRM":
            # st.write("IRM")
            st.session_state.degree_and_field_of_study = st.selectbox(
                "Engineering Stream:",
                [
                    "B.Tech - Civil Engineering",
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
                key="engineering_stream_x",
            )

            st.session_state.subdomain = st.text_input(
                "Enter Subdomain:", key="subdomasasdain", placeholder="Ethical Hacking"
            )

            st.session_state.desired_industry = st.text_input(
                "Enter your Desired Industry:",
                key="desired_indasdustry",
                placeholder="Cyber Security",
            )

            st.session_state.career_goals = st.text_input(
                "Enter your Career Goals:",
                key="career_goalssdfs",
                placeholder="Security Analyst",
            )
            st.session_state.designation_entered = True
        else:
            st.session_state.degree_and_field_of_study_arm = st.selectbox(
                "Engineering Stream:",
                [
                    "B.Tech - Civil Engineering",
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
                key="engineering_stream_xx",
            )
            st.session_state.subdomain_arm = st.text_input(
                "Enter Subdomain:", key="degreee", placeholder="Robotics and Automation"
            )
            st.session_state.location = st.text_input(
                "Enter your Preferred Location:",
                key="preferred_location",
                placeholder="Germany",
            )
            st.session_state.budget = st.text_input(
                "Enter your Budget:", key="buDSFSDFDdget", placeholder="50k-60k USD"
            )
            st.session_state.designation_entered = True
             
    if st.session_state.designation_entered:
        if st.button("Generate Report"):
            st.session_state.courses_list = ""
            st.session_state.courses_list_shown = False
            st.session_state.courses = []
            st.session_state.course_list_stripped = False
            st.session_state.selected_coursee = ""
            st.session_state.course_selected = True
            st.session_state.course_outline_content = ""
            st.session_state.course_outline_shown = False
            st.session_state.everything_shown = False

            st.session_state.courses_list = {}
            st.session_state.success = {}
            st.session_state.roadmap = {}
            st.session_state.marketing = {}
            st.session_state.strategy = {}
            st.session_state.data_insights = {}

            st.session_state.courses_list_arm = ""
            st.session_state.success_arm = ""
            st.session_state.roadmap_attributes_arm = ""
            st.session_state.academic_arm = ""
            st.session_state.market_arm = ""
            st.session_state.courses_list_irm = ""
            st.session_state.job_titles_irm = ""
            st.session_state.industry_irm = ""
            st.session_state.roadmap_attributes_irm = ""    

            st.session_state.Target_audience_Analysis = None
            st.session_state.Data_Insights = None
            st.session_state.Strategies_To_Address_Pain_Points = None
            st.session_state.marketing_and_engagement_strategies = None
            st.session_state.roadmap_mrm_string = None
            st.session_state.success_factors_string = None

            st.session_state.higher_education_string = ""
            st.session_state.market_string = ""
            st.session_state.academic_skills = ""
            st.session_state.roadmap_attributes_string = ""
            st.session_state.success_factors_string_arm = ""    

            st.session_state.industry_requirements_string = ""
            st.session_state.job_roles_and_description = ""
            st.session_state.industry_trends_string = ""
            st.session_state.roadmap_attributes_string2 = ""
            # st.session_state.line_mrm = ""
            # st.session_state.line_arm = ""
            # st.session_state.line_irm = ""

            st.session_state.line_mrm1 = ""
            st.session_state.line_mrm2 = ""
            st.session_state.line_mrm3 = ""
            st.session_state.line_mrm4 = ""
            st.session_state.line_mrm5 = ""
            st.session_state.line_mrm6 = ""
            st.session_state.line_mrm7 = ""

            st.session_state.line_arm1 = ""
            st.session_state.line_arm2 = ""
            st.session_state.line_arm3 = ""
            st.session_state.line_arm4 = ""
            st.session_state.line_arm5 = ""
            st.session_state.line_arm6 = ""

            st.session_state.line_irm1 = ""
            st.session_state.line_irm2 = ""
            st.session_state.line_irm3 = ""
            st.session_state.line_irm4 = ""
            st.session_state.line_irm5 = ""

            
            if st.session_state.type_selected == "MRM":
                time.sleep(2)
                response_coursess = get_target_audience_analysis_x(
                    st.session_state.selected_application_mrm,
                    career_choice,
                    st.session_state.job_designation,
                    st.session_state.goals,
                    st.session_state.selected_application_mrm,
                )
                response_data = get_data_insights_x(
                    st.session_state.selected_application_mrm,
                    career_choice,
                    st.session_state.job_designation,
                    st.session_state.goals,
                    st.session_state.selected_application_mrm,
                )
                response_strategies = get_strategies_to_address_pain_points_x(
                    st.session_state.selected_application_mrm,
                    career_choice,
                    st.session_state.job_designation,
                    st.session_state.goals,
                    st.session_state.selected_application_mrm,
                )
                response_marketing = get_marketing_engagement_strategies_x(
                    st.session_state.selected_application_mrm,
                    career_choice,
                    st.session_state.job_designation,
                    st.session_state.goals,
                    st.session_state.selected_application_mrm,
                )
                response_roadmap = get_roadmap_x(
                    st.session_state.selected_application_mrm,
                    career_choice,
                    st.session_state.job_designation,
                    st.session_state.goals,
                    st.session_state.selected_application_mrm,
                )
                response_success = get_success_factors_metrics_x(
                    st.session_state.selected_application_mrm,
                    career_choice,
                    st.session_state.job_designation,
                    st.session_state.goals,
                    st.session_state.selected_application_mrm,
                )
                st.session_state.line_mrm1 = "---"
                st.session_state.line_mrm2 = "---"
                st.session_state.line_mrm3 = "---"
                st.session_state.line_mrm4 = "---"
                st.session_state.line_mrm5 = "---"
                st.session_state.line_mrm6 = "---"
                st.session_state.line_mrm7 = "---"

                st.session_state.Target_audience_Analysis = "Target audience Analysis"
                st.session_state.Data_Insights = "Data Insights"
                st.session_state.Strategies_To_Address_Pain_Points = "Strategies to Address Pain Points"
                st.session_state.marketing_and_engagement_strategies = "Marketing and Engagement Strategies"
                st.session_state.roadmap_mrm_string = "Roadmap"
                st.session_state.success_factors_string = "Success Factors and metrics"
                st.session_state.courses_list = response_coursess.content
                st.session_state.success = response_success.content
                st.session_state.roadmap = response_roadmap.content
                st.session_state.marketing = response_marketing.content
                st.session_state.strategy = response_strategies.content
                st.session_state.data_insights = response_data.content
                st.session_state.courses_list_shown = True
            elif st.session_state.type_selected == "ARM":
                # st.write("ARM")
                time.sleep(2)
                response_coursess = get_higher_education_program_attributes_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.location,
                    st.session_state.budget,
                    st.session_state.subdomain,
                )
                response_market = get_market_and_economic_attributes_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.location,
                    st.session_state.budget,
                    st.session_state.subdomain,
                )
                response_academic = get_academic_skills_and_knowledge_attributes_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.location,
                    st.session_state.budget,
                    st.session_state.subdomain,
                )
                response_roadmap_attr = get_academic_roadmap_attributes_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.location,
                    st.session_state.budget,
                    st.session_state.subdomain,
                )
                response_success = get_success_factors_and_metrics_x_higher(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.location,
                    st.session_state.budget,
                    st.session_state.subdomain,
                )

                st.session_state.line_arm1 = "---"
                st.session_state.line_arm2 = "---"
                st.session_state.line_arm3 = "---"
                st.session_state.line_arm4 = "---"
                st.session_state.line_arm5 = "---"
                st.session_state.line_arm6 = "---"

                st.session_state.higher_education_string = "Higher Education Program Attributes"
                st.session_state.market_string = "Market and Economic Attributes"
                st.session_state.academic_skills = "Academic Skills and Knowledge Attributes"
                st.session_state.roadmap_attributes_string = "Roadmap Attributes"
                st.session_state.success_factors_string_arm = "Success Factors and Metrics"
                st.session_state.success_arm = response_success.content
                st.session_state.roadmap_attributes_arm = response_roadmap_attr.content
                st.session_state.academic_arm = response_academic.content
                st.session_state.market_arm = response_market.content
                st.session_state.courses_list_arm = response_coursess.content
                st.session_state.courses_list_shown = True
            else:
                # st.write("IRM")
                time.sleep(2)
                response_courses_list_irm = get_industry_requirements_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.desired_industry,
                    st.session_state.career_goals,
                    st.session_state.subdomain,
                )
                response_job_titles_irm = get_job_titles_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.desired_industry,
                    st.session_state.career_goals,
                    st.session_state.subdomain,
                )
                response_industry_irm = get_industry_trends_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.desired_industry,
                    st.session_state.career_goals,
                    st.session_state.subdomain,
                )
                response_roadmap_attributes_irm = get_roadmap_attributes_x(
                    st.session_state.subdomain,
                    st.session_state.degree_and_field_of_study,
                    st.session_state.desired_industry,
                    st.session_state.career_goals,
                    st.session_state.subdomain,
                )

                st.session_state.line_irm1 = "---"
                st.session_state.line_irm2 = "---"
                st.session_state.line_irm3 = "---"
                st.session_state.line_irm4 = "---"
                st.session_state.line_irm5 = "---"

                st.session_state.industry_requirements_string = "Industry Requirements"
                st.session_state.job_roles_and_description = "Job Roles and Descriptions"
                st.session_state.industry_trends_string = "Industry Trends and Outlook"
                st.session_state.roadmap_attributes_string2 = "Roadmap Attributes"
                st.session_state.courses_list_irm = response_courses_list_irm.content
                st.session_state.job_titles_irm = response_job_titles_irm.content
                st.session_state.industry_irm = response_industry_irm.content
                st.session_state.roadmap_attributes_irm = response_roadmap_attributes_irm.content    
                st.session_state.courses_list_shown = True
            

    # if st.session_state.courses_list and st.session_state.courses_list_shown:
    #     if st.session_state.type_selected == "MRM":
    #         st.write("---")
    #         st.subheader("Target audience Analysis")
    #         st.write(st.session_state.courses_list)
    #         st.write("---")
    #         st.subheader("Data Insights")
    #         st.write(st.session_state.data_insights)
    #         st.write("---")
    #         st.subheader("Strategies to Address Pain Points")
    #         st.write(st.session_state.strategy)
    #         st.write("---")
    #         st.subheader("Marketing and Engagement Strategies")
    #         st.write(st.session_state.marketing)
    #         st.write("---")
    #         st.subheader("Roadmap")
    #         st.write(st.session_state.roadmap)
    #         st.write("---")
    #         st.subheader("Success Factors and Metrics")
    #         st.write(st.session_state.success)
    #         st.write("---")
    #     elif st.session_state.type_selected == "ARM":
    #         st.write("ARM")
        
    if (st.session_state.courses_list or st.session_state.courses_list_arm or st.session_state.courses_list_irm)  and  st.session_state.courses_list_shown:
    # if st.session_state.courses_list and st.session_state.courses_list_shown:
        if st.session_state.type_selected == "MRM":
            # st.write(st.session_state.line_mrm1)
            st.subheader(st.session_state.Target_audience_Analysis)
            st.write(st.session_state.courses_list)
            # st.write(st.session_state.line_mrm2)
            st.subheader(st.session_state.Data_Insights)
            st.write(st.session_state.data_insights)
            # st.write(st.session_state.line_mrm3)
            st.subheader(st.session_state.Strategies_To_Address_Pain_Points)
            st.write(st.session_state.strategy)
            # st.write(st.session_state.line_mrm4)
            st.subheader(st.session_state.marketing_and_engagement_strategies)
            st.write(st.session_state.marketing)
            # st.write(st.session_state.line_mrm5)
            st.subheader(st.session_state.roadmap_mrm_string)
            st.write(st.session_state.roadmap)
            # st.write(st.session_state.line_mrm6)
            st.subheader(st.session_state.success_factors_string)
            st.write(st.session_state.success)
            # st.write(st.session_state.line_mrm7)
            st.session_state.everything_shown = True
        elif st.session_state.type_selected == "ARM":
            # st.write(st.session_state.line_arm1)
            st.subheader(st.session_state.higher_education_string)
            st.write(st.session_state.courses_list_arm)
            # st.write(st.session_state.line_arm2)
            st.subheader(st.session_state.market_string)
            st.write(st.session_state.market_arm)
            # st.write(st.session_state.line_arm3)
            st.subheader(st.session_state.academic_skills)
            st.write(st.session_state.academic_arm)
            # st.write(st.session_state.line_arm4)
            st.subheader(st.session_state.roadmap_attributes_string)
            st.write(st.session_state.roadmap_attributes_arm)
            # st.write(st.session_state.line_arm5)
            st.subheader(st.session_state.success_factors_string_arm)
            st.write(st.session_state.success_arm)
            # st.write(st.session_state.line_arm6)
            st.session_state.everything_shown = True
        else: 
            # st.write(st.session_state.line_irm1)
            st.subheader(st.session_state.industry_requirements_string)
            st.write(st.session_state.courses_list_irm)
            # st.write(st.session_state.line_irm2)
            st.subheader(st.session_state.job_roles_and_description)
            st.write(st.session_state.job_titles_irm)
            # st.write(st.session_state.line_irm3)
            st.subheader(st.session_state.industry_trends_string)
            st.write(st.session_state.industry_irm)
            # st.write(st.session_state.line_irm4)
            st.subheader(st.session_state.roadmap_attributes_string2)
            st.write(st.session_state.roadmap_attributes_irm)
            # st.write(st.session_state.line_irm5)
            st.session_state.everything_shown = True
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
            reset_shown()
            email = st.session_state.email
            bruh(email, "Research Engine", user_flow_choice, career_choice)
            st.session_state.everything_shown = False
            
