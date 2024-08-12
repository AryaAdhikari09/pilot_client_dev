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
                        "selected_application": st.session_state.selected_subdomain,
                        "projects_content": st.session_state.job_profile_content,
                        "overview_content": st.session_state.courses_list,
                        "roadmap_content": st.session_state.roadmap,
                        "final_report_content": st.session_state.marketing,
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
                                "courses_list": st.session_state.courses_list_irm.content,
                                "job_titles": st.session_state.job_titles_irm.content,
                                "industry": st.session_state.industry_irm.content,
                                "roadmap_attributes": st.session_state.roadmap_attributes_irm.content,
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
                                "courses_list": st.session_state.courses_list_arm,
                                "academic": st.session_state.academic_arm,
                                "roadmap_attributes": st.session_state.roadmap_attributes_arm,
                                "success": st.session_state.success_arm,
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

st.set_page_config(page_title="Project Engine", page_icon=":smile:")


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


def get_gemini_response_faq(
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

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_response(
    question, context, engineering_stream, career_choice, domain_sector
):

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are an Educator with real-world knowledge in {engineering_stream}. "
                f"Given a student's career choice as {career_choice} and interest in {domain_sector}. "
                f"Generate and display 15 unique and interesting applications specific to the {engineering_stream} , {domain_sector}, {career_choice} for hands-on projects relevant to current trends in India using the context: {context} 3 examples as a reference on how to output the applications. Remember to provide an overview of 2 lines after the colon after listing the course. Do not provide any heading or overall description above or below the applications."
                f"Provided below are examples for the format of. DONT generate the projects given in the format example everytime, use it as a reference for formating the output. "
                f"""
                General Fomrat:
                1. **Project Heading:** Project Overview.
                2. **Project Heading:** Project Overview. 
                3. **Project Heading:** Project Overview.               
                4. **Project Heading:** Project Overview.
                5. **Project Heading:** Project Overview.
                6. **Project Heading:** Project Overview.
                7. **Project Heading:** Project Overview.
                8. **Project Heading:** Project Overview.
                9. **Project Heading:** Project Overview.
                10. **Project Heading:** Project Overview.
                11. **Project Heading:** Project Overview.
                12. **Project Heading:** Project Overview.
                13. **Project Heading:** Project Overview.
                14. **Project Heading:** Project Overview.
                15. **Project Heading:** Project Overview.

                Format Example for reference 1:
                1. **Health Monitoring System:** Develop an IoT-based system to monitor vital health parameters (e.g., blood pressure, heart rate) and transmit data to healthcare providers.
                2. **Telemedicine Platform:** Create a web or mobile application that enables remote consultation and diagnosis between patients and healthcare professionals.
                3. **Medical Image Analysis:** Design an AI-powered system to analyze medical images (e.g., X-rays, MRI scans) for disease detection and diagnosis.
                4. **Health Data Management System:** Build a centralized system to store, manage, and analyze large volumes of health data for population health 
                management.
                5. **E-Health Records System:** Develop a secure and accessible system for storing and sharing electronic health records, improving patient care coordination.
                6. **Health Education and Awareness App:** Create a mobile application that provides health information, resources, and support to promote healthy living and well-being.
                7. **Remote Patient Monitoring and Management:** Design a wearable or IoT device to monitor patient health metrics in real-time and provide alerts to healthcare providers.
                8. **Health Insurance Optimization Platform:** Develop an AI-based system to analyze health insurance data and identify opportunities for cost optimization and improved coverage.
                9. **Health Policy Analysis and Simulation:** Build a simulation model to analyze the impact of different health policies on population health outcomes and economic costs.
                10. **Medical Device Development:** Design and prototype innovative medical devices that address unmet healthcare needs, such as wearable health sensors or diagnostic tools.
                11. **Health Workforce Planning and Management:** Develop a data-driven system to forecast future healthcare workforce needs and optimize staffing levels.
                12. **Health Equity and Access Improvement:** Design a web or mobile application that connects underserved populations with healthcare resources and services.
                13. **Public Health Surveillance and Outbreak Detection:** Build a system to monitor and analyze public health data to identify disease outbreaks 
                and implement early intervention measures.
                14. **Health Research and Development:** Utilize machine learning and data analytics to extract insights from clinical data and support health research advancements.
                15. **Health Economics and Outcomes Analysis:** Develop models to evaluate the cost-effectiveness and outcomes of different healthcare interventions and policies.

                Format Example for reference 2:
                1. **Solar Energy Prediction using Machine Learning:** Develop a model to predict solar energy output using historical data and machine learning algorithms.
                2. **Wind Turbine Optimization using Data Analytics:** Analyze data from wind turbines to optimize their performance and increase energy efficiency.
                3. **Smart Grid Management with IoT:** Design an IoT-based system to monitor and manage smart grids, ensuring efficient energy distribution and reducing power outages.
                4. **Grid-Connected PV System Design and Simulation:** Model and simulate a grid-connected photovoltaic system to optimize its design and maximize energy production.
                5. **Electric Vehicle Charging Infrastructure Optimization:** Develop algorithms to optimize the placement and utilization of electric vehicle charging stations based on demand and grid constraints.
                6. **Energy Storage System Design for Renewables:** Design and evaluate energy storage systems for renewable energy sources, such as batteries or 
                pumped hydro storage.
                7. **Renewable Energy Resource Assessment using Satellite Data:** Utilize satellite data to assess the potential of renewable energy sources, such as solar and wind, in different regions.
                8. **Hydroelectric Power Plant Simulation and Control:** Model and simulate a hydroelectric power plant to optimize its operation and improve energy generation efficiency.
                9. **Microgrid Design and Control for Rural Electrification:** Design and implement microgrids for rural areas, utilizing renewable energy sources to provide reliable electricity.
                10. **Biofuel Production Optimization using Computational Fluid Dynamics:** Utilize CFD simulations to optimize biofuel production processes and maximize yield.
                11. **Geothermal Energy Modeling and Simulation:** Develop models and simulations to assess the potential and optimize the extraction of geothermal energy.
                12. **Energy Efficiency in Buildings using Building Information Modeling:** Utilize BIM to design and optimize energy-efficient buildings, reducing energy consumption and carbon emissions.
                13. **Renewable Energy Policy Analysis using Data Science:** Analyze data to identify trends and patterns in renewable energy policies and their impact on energy production.
                14. **Smart Home Energy Management with AI:** Design and implement AI-powered smart home energy management systems to reduce energy consumption and optimize energy usage.
                15. **Renewable Energy Education Platform Development:** Create an online or mobile platform to provide interactive and engaging educational resources on renewable energy and its applications.
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
        context=context,
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_response_roadmap(question, context, domain_sector):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:

                Agriculture, Data Analysis

                Develop a sophisticated machine learning model designed to forecast crop yields with high accuracy, leveraging environmental and agricultural data. This model aims to equip farmers with predictive insights that enable strategic planning, resource optimization, and maximization of agricultural outputs.

                - **Languages:** Deep proficiency in Python for its extensive data science ecosystem and R for statistical analysis. Both languages are essential for manipulating datasets, applying statistical models, and visualizing data insights.
                - **Machine Learning Libraries:** Expertise in scikit-learn for its comprehensive suite of machine learning tools, TensorFlow for deep learning applications critical in handling complex datasets, and Keras for building and deploying neural network models.
                - **Skills:** Advanced skills in data analysis for uncovering trends and patterns, machine learning modeling to build predictive algorithms, data preprocessing to clean and prepare data, and feature engineering to extract and select meaningful data points.
                - **Tools:** Proficiency in Jupyter Notebook for interactive development and testing, PyCharm or RStudio for robust development environments, and Tableau or Power BI for creating dynamic data visualizations for stakeholders.
                - **Resources:** A commitment to leveraging online tutorials for upskilling, documentation for understanding library functionalities, and participation in community forums for problem-solving and staying updated on industry trends.

                - **Sensors:** Implementation of a network of IoT sensors across multiple test fields to gather micro-climatic data (e.g., soil moisture levels using capacitive moisture sensors, temperature and humidity with DHT sensors) and crop health indicators (e.g., NDVI sensors for vegetation health).
                - **Drones:** drones equipped with high-resolution and multispectral cameras to capture detailed aerial imagery, enabling precise monitoring of crop growth, pest infestation, and water stress levels across vast areas.
                - **Tractors and Equipment:** Integration of smart data loggers on tractors and farming machinery to systematically collect data on planting densities, soil compaction, and harvest volumes, enhancing the dataset with operational insights.

                - **Simulation Models:** Development of complex agronomic models to simulate crop growth stages under varying environmental conditions, providing a virtual testing ground for yield predictions without the need for direct field data.
                - **Remote Sensing Data:** Adoption of satellite imagery and aerial photography services to obtain comprehensive, large-scale data on vegetation health, land use, and environmental factors impacting crop growth.
                - **Historical Data Analysis:** Compilation and analysis of extensive historical datasets from agricultural databases, research institutions, and weather stations to inform model predictions with trends and patterns observed over years.

                - **Data Acquisition:** Establish partnerships with agricultural research institutes and local farming cooperatives to access diverse datasets, including sensor data, drone imagery, and operational logs from farm equipment.
                - **Data Cleaning:** Employ sophisticated data cleaning techniques to address noise, outliers, and missing values. Techniques include temporal data interpolation for filling gaps and robust statistical methods to identify and correct anomalies.
                - **Data Exploration:** Conduct an in-depth exploratory data analysis (EDA) using advanced visualization tools to uncover underlying data structures, correlations between variables, and potential predictors of crop yield.

                - **Feature Extraction:** Apply domain-specific knowledge to extract relevant features from raw data, such as calculating vegetation indices from drone imagery or deriving soil health metrics from sensor data.
                - **Feature Construction:** Innovate by creating new features that capture the interactions between different environmental and agricultural factors, using techniques like polynomial feature combinations to model complex relationships.
                - **Feature Selection:** Implement machine learning-based feature selection methods, such as recursive feature elimination (RFE) or model-based selection, to identify and retain features with the highest predictive power.

                - **Model Selection:** Evaluate multiple machine learning models, including ensemble methods like Random Forest and gradient boosting machines (GBM), and deep learning approaches like Convolutional Neural Networks (CNNs) for image data analysis.
                - **Model Training:** Utilize advanced training techniques, including k-fold cross-validation to ensure model robustness and grid search or Bayesian optimization for hyperparameter tuning to enhance model performance.
                - **Model Evaluation:** Apply a comprehensive evaluation framework, using a mix of metrics (e.g., R^2 for model fit, RMSE for prediction accuracy) and domain-specific validation techniques, such as comparing predicted versus actual yields in controlled test plots.

                - **Documentation and Training:** Create detailed user guides and video tutorials to assist farmers in navigating the platform. Organize interactive webinars and workshops for hands-on training, aiming to enhance user confidence and encourage feedback for continuous improvement.

                - **Performance Monitoring:** Establish a system for ongoing monitoring of the model's predictive accuracy using real-world agricultural data. This includes setting up automated alerts for significant deviations in model performance metrics.
                - **Feedback Loop:** Create channels for regular feedback from the user community, including surveys, focus groups, and direct communication tools. This feedback is crucial for understanding the model's effectiveness and areas where it can be enhanced.
                - **Model Updates:** Implement a structured process for periodically updating the model with new data, insights, and user feedback. This includes refining algorithms, introducing new features, and adjusting model parameters to reflect the latest agricultural trends and technologies.
                """
                f"""
                example 2:

                Precision Agriculture, Remote Sensing

                This project seeks to revolutionize farm management by deploying drones equipped with advanced imaging technology to collect data on crop health, environmental conditions, and more. By analyzing this data with sophisticated algorithms, the project will provide actionable insights to farmers, enabling them to make informed decisions, optimize agricultural practices, and ultimately increase crop yields while promoting sustainability.

                - **Languages:** Mastery of Python for leveraging AI and machine learning libraries, and JavaScript for building interactive web applications.
                - **Remote Sensing Libraries:** In-depth knowledge of remote sensing libraries such as GDAL for geographic data manipulation, OpenCV for image processing, and PyTorch or TensorFlow for applying neural networks to image data.
                - **Skills:** Expertise in drone operation and imagery analysis, proficiency in GIS technology for mapping and spatial analysis, and strong analytical skills for data interpretation.
                - **Tools:** Proficiency with drone flight planning and monitoring software, GIS platforms like ArcGIS or QGIS for spatial data analysis, and web development environments such as Visual Studio Code or Atom.
                - **Resources:** Access to comprehensive online courses on remote sensing and GIS, specialized forums and communities for drone technology, and agricultural data science resources for continuous learning and troubleshooting.

                - **Drones:** Selection and procurement of high-capacity drones capable of carrying multispectral and thermal sensors for detailed field imagery.
                - **Ground Control Stations:** Setup of advanced ground control systems for real-time monitoring and management of drone flights.
                - **Computing Infrastructure:** Investment in high-performance computing resources for the storage, processing, and analysis of large datasets generated by drone flights.

                - **Automated Data Processing System:** Development of an automated pipeline for processing and analyzing drone-captured imagery, including features for image stitching, enhancement, and feature extraction.
                - **Predictive Analytics Engine:** Creation of predictive models using machine learning to analyze crop health indicators, predict potential yield, and identify areas requiring intervention.
                - **Farmer Dashboard:** Design and implementation of a secure, user-friendly web dashboard that provides farmers with easy access to insights, visualizations, and recommendations derived from drone data.

                - **Technical Specifications:** Define the technical specifications for drones, including sensor requirements, battery life, and payload capacity to ensure comprehensive field coverage and data collection capabilities.
                - **Software Architecture Planning:** Outline the architecture for the data processing and analysis pipeline, ensuring scalability, efficiency, and integration capability with external platforms and APIs.
                - **Pilot Area Selection:** Choose diverse agricultural regions for pilot testing to cover a range of crops, climates, and farming practices, ensuring the system's adaptability and effectiveness.

                - **Drone Flight Operations:** Conduct systematic drone flights over pilot areas to collect high-resolution and multispectral imagery, focusing on different times of day and crop stages for comprehensive data.
                - **Data Processing Workflow:** Implement the data processing workflow to clean, stitch, and enhance images, preparing them for detailed analysis.
                - **Preliminary Data Analysis:** Perform initial data analysis to identify patterns, anomalies, and insights that can inform crop health assessments and management decisions.

                - **Feature Engineering:** Utilize remote sensing data to engineer features relevant to crop health, such as vegetation indices and thermal anomalies, that serve as inputs for machine learning models.
                - **Model Training and Testing:** Train machine learning models on the engineered features to identify crop health issues, estimate yield, and detect areas needing intervention; thoroughly test models for accuracy and reliability.
                - **Validation with Experts:** Collaborate with agronomists and farming experts to validate model predictions against real-world observations and outcomes, refining models based on expert feedback.

                - **User Interface Creation:** Develop an intuitive, interactive web interface that allows farmers to access personalized insights, view aerial imagery, and receive actionable recommendations.
                - **User Training and Support:** Provide comprehensive training materials, online tutorials, and support services to assist farmers in utilizing the platform effectively.

                - **Expansion to New Regions:** Gradually expand the service to new geographical regions and crop types, adapting the system based on regional agricultural practices and challenges.
                - **Feedback Loop and Iteration:** Establish mechanisms for collecting user feedback, monitoring system performance, and iteratively improving the data analysis models and user interface based on real-world usage and evolving agricultural technologies.
                - **Stakeholder Engagement:** Engage continuously with farmers, agricultural advisors, and researchers to enhance the system's relevance and impact, fostering a community of practice
                """
                f"""
                example 3:

                Smart Agriculture, Irrigation Technology

                To create a highly efficient smart fertigation system that leverages IoT (Internet of Things) technology and advanced data analytics to precisely manage the delivery of water and nutrients to crops. This project aims to enhance crop yields, minimize resource wastage, and support sustainable farming practices by ensuring that fertilization is dynamically adjusted based on real-time soil and plant needs.

                - **Languages:** Proficiency in Python for backend development and data analysis; familiarity with JavaScript for frontend web application development.
                - **IoT Platforms:** In-depth knowledge of IoT platforms such as Arduino or Raspberry Pi for sensor integration and data collection.
                - **Data Analytics Libraries:** Expertise in data analytics and machine learning libraries, such as Pandas for data manipulation, NumPy for numerical analysis, and Scikit-learn for predictive modeling.
                - **Skills:** Strong background in IoT system design, data analytics, machine learning, and web development; understanding of agronomy and irrigation principles is essential.
                - **Tools:** Experience with IoT development environments, database management systems (e.g., PostgreSQL, MongoDB), and web development frameworks (e.g., React, Flask).

                - **Sensors:** of soil moisture sensors, nutrient level detectors, and climate sensors to monitor environmental conditions and crop health.
                - **Controllers:** Utilization of smart controllers capable of processing sensor data and managing irrigation and fertilizer distribution systems based on predefined algorithms.
                - **Networking Equipment:** Installation of reliable networking equipment to facilitate communication between sensors, controllers, and the central data management system.

                - **Data Management Platform:** Development of a centralized data management platform to aggregate, process, and analyze data collected from various sensors and controllers.
                - **Predictive Modeling Software:** Creation of predictive models to forecast crop nutrient requirements and optimize fertigation schedules.
                - **User Interface (UI):** Designing an intuitive web-based UI that allows farmers to monitor real-time data, receive alerts and recommendations, and adjust fertigation parameters manually if needed.

                - **Component Selection:** Careful selection of sensors and controllers that meet the requirements for accuracy, durability, and cost-effectiveness.
                - **Prototype Design:** Design and assemble a prototype system that integrates sensors, controllers, and networking equipment to test functionality and gather preliminary data.
                - **Software Architecture:** Outline the software architecture for the data management platform and predictive modeling software, ensuring scalability and user accessibility.

                - **Pilot Implementation:** Deploy the prototype system in a controlled pilot environment to collect data on soil moisture, nutrient levels, and other relevant agronomic factors.
                - **Data Processing and Analysis:** Implement data processing workflows to clean and analyze the collected data, identifying key patterns and relationships between soil/plant conditions and crop health/yield.

                - **Predictive Model Development:** Develop and train machine learning models to predict crop nutrient requirements and optimal fertigation schedules based on collected data and agronomic principles.
                - **System Refinement:** Refine the prototype system based on data analysis and model predictions, optimizing sensor placement, controller logic, and networking efficiency for improved performance.

                - **Data Management Platform:** Build a robust data management platform that integrates with the smart fertigation system, supporting data aggregation, processing, and analysis.
                - **UI Development:** Design and develop a user-friendly web-based UI that provides farmers with insights, alerts, and recommendations generated by the predictive models, and allows for manual system adjustments.

                - **Field Testing:** Conduct extensive field testing in diverse agricultural settings to validate system performance, model accuracy, and user satisfaction.
                - **Feedback Collection:** Gather feedback from end-users (farmers) and agronomy experts to identify areas for improvement in the system design, software functionality, and user interface.
                - **Commercial:** Finalize the smart fertigation system for commercial, incorporating feedback from field testing and ensuring scalability, reliability, and ease of use.
                """
                f"As an Educator with real-world knowledge in {domain_sector} and the most recent trends and context: {context} you possess the expertise to offer detailed and practical advice to address users' questions effectively. Drawing upon your background, you can break down complex concepts into manageable subtasks, providing actionable steps and strategies tailored to the specific project. Your insights bridge the gap between theory and practice, empowering learners with the skills and knowledge they need to succeed in real-world settings."
                f"provide me a roadmap of the project {question} using the above 3 examples as a reference on how to output the roadmap, "
                f"remember to include a project category of the project {question} exactly like in the three examples, "
                f"remember to include knowledge requirements for the the project {question} exactly like in the three examples, "
                f"remember to hardware products (if feasible) related to the project {question} exactly like in the three examples, "
                f"remember to include software alternatives (if hardware is not feasible) related to the the project {question} might have exactly like in the three examples, "
                f"remember to include the detailed phases(excluding a deployment phase) of the roadmap of the project {question} exactly like in the three examples, ",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        domain_sector=domain_sector, user_input=question, context=context
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_respone_overview(
    question, context, engineering_stream, career_choice, domain_sector
):

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:

                In an era where technology bridges gaps across various sectors, the legal field in India is poised for a transformation that caters to the needs of its citizens more efficiently. The "Legal Chatbot for Citizen Assistance" project stands at this juncture, aiming to leverage artificial intelligence to democratize access to legal information and assistance, especially for the marginalized and underprivileged communities.

                India's diverse population, characterized by significant disparities in income, education, and access to resources, underscores the critical need for legal assistance. Marginalized and underprivileged communities often find themselves entangled in legal issues without the means to seek justice. The digital divide further exacerbates this situation, leaving a substantial portion of the population, particularly in rural and remote areas, in a legal vacuum.

                Despite the presence of legal aid clinics and organizations, the reach is limited, often constrained by geographical, financial, and informational barriers. The burgeoning case loads on courts and legal professionals underline the pressing need for alternative solutions to legal assistance that are both effective and scalable.

                The silver lining lies in the increasing penetration of technology within the legal sector. Digital platforms and solutions are being increasingly recognized as viable means to address the systemic gaps in legal assistance delivery.

                This act provides a robust framework for the delivery of legal aid to the poor and disadvantaged, setting a precedent for initiatives aimed at enhancing access to justice.

                The policy emphasizes the integration of technology in legal aid delivery, advocating for innovative solutions like the proposed legal chatbot to streamline and enhance the accessibility of legal services.

                Aligned with the Digital India Mission's objectives, this project leverages digital technologies for citizen empowerment, ensuring that legal assistance is just a click away for anyone in need.

                By providing a platform that is accessible 24/7, the chatbot significantly lowers the barriers to legal information, making it easier for citizens to understand their legal rights and the remedies available to them.

                Automating the initial stages of legal consultation can alleviate the workload on courts and legal practitioners, allowing them to focus on more complex aspects of legal service delivery.

                The chatbot serves not just as a tool for legal assistance but also as a means for legal education, empowering citizens with the knowledge to navigate the legal system more effectively.

                By digitizing legal assistance, the project introduces a level of transparency and accountability into the system, building trust and confidence among citizens.

                The chatbot's design allows for across various platforms, including websites, mobile apps, and social media, ensuring wide accessibility.

                Potential integrations with existing government portals and legal databases can enrich the chatbot's resource base, making it a comprehensive tool for legal assistance.

                Built to scale, the chatbot can manage a vast number of inquiries simultaneously, providing timely assistance to citizens nationwide.

                Collaborations with existing legal aid clinics and organizations can provide a foundation of legal knowledge and expertise to support the chatbot's development.

                Access to government legal databases will enable the chatbot to provide accurate and up-to-date legal information, enhancing its effectiveness.

                Leveraging open-source chatbot frameworks can expedite the development process, allowing for customization and scalability according to project needs.

                Engaging legal professionals in the project can ensure that the chatbot's responses are vetted for accuracy and relevance, maintaining a high standard of legal assistance.

                The "Legal Chatbot for Citizen Assistance" project emerges as a beacon of innovation in the Indian legal landscape, promising to bridge the gap between legal services and the citizens they aim to serve. By harnessing technology, this project not only aligns with government policies but also sets a new standard for legal assistance in India. Through its scalable design and impactful delivery, it has the potential to transform legal accessibility, making justice truly accessible to all.
                """
                f"""
                example 2:

                In an era where technological innovation drives progress across various sectors, agriculture stands on the brink of a significant transformation. The "Drone-based Crop Monitoring" project seeks to leverage the power of drone technology to revolutionize how crops are monitored, managed, and optimized. This initiative is positioned to offer unprecedented insights into crop health and environmental conditions, thereby facilitating informed decision-making, enhancing productivity, and promoting sustainable agricultural practices.

                The agricultural sector is under increasing pressure to meet the global demand for food, which is set to rise substantially in the coming decades. Efficient crop management is crucial for maximizing yield, conserving resources, and minimizing environmental impact. The advent of precision agriculture, facilitated by technological advancements, offers a pathway to achieving these goals.

                Traditional crop monitoring methods are often labor-intensive, time-consuming, and prone to errors, making it difficult to respond promptly to issues. Furthermore, access to advanced agricultural technologies remains limited, especially in developing regions, exacerbating the challenges of ensuring food security and sustainable farming practices.

                The integration of technology in agriculture, particularly through the adoption of drones, presents a significant opportunity to overcome these challenges. Drones offer a unique vantage point and the ability to deploy advanced imaging technologies, making them a pivotal tool in the evolution of agricultural practices.

                Although not yet existent, a hypothetical national policy on precision agriculture could serve as a crucial framework for integrating drone technology in agricultural practices. This policy would encourage the adoption of precision farming techniques, including drone-based monitoring, to improve crop yield and resource efficiency.

                Aligned with the broader Digital India initiative, a specialized mission focusing on the digitization of agriculture could support projects like drone-based crop monitoring. Such a mission would aim to bridge the technological gap in agriculture, promoting innovation and technology adoption across the sector.

                By providing detailed, real-time data on crop health and environmental conditions, drone-based monitoring can significantly enhance agricultural productivity. This technology enables precise interventions, optimizing resource use and maximizing crop yield.

                Drones facilitate efficient water, fertilizer, and pesticide use, contributing to sustainable resource management. By identifying precisely where and how much of these inputs are needed, the technology helps reduce waste and environmental impact.

                The project contributes to sustainable agricultural practices by promoting efficient resource use and minimizing the adverse effects of farming on the environment. In the long term, this will help ensure food security and the health of agricultural ecosystems.

                The drone-based crop monitoring system is designed to be adaptable and scalable across different crops and geographical areas. This versatility ensures that the benefits of the technology can be realized in diverse agricultural settings, from small family farms to large commercial operations.

                The project envisages seamless integration with existing agricultural technologies and data management systems, enhancing the utility and impact of drone-based monitoring within the broader ecosystem of agricultural innovation.

                Given its modular nature and the decreasing cost of drone technology, the project has the potential for wide adoption. Customization options allow for the technology to be tailored to specific crops, climates, and farming practices, further enhancing its applicability and impact.

                Partnerships with academic institutions and research bodies will be crucial in refining the technology, ensuring its relevance and effectiveness for various agricultural applications.

                Collaborations with government bodies and private sector stakeholders can provide the necessary support in terms of funding, regulatory guidance, and technological expertise, facilitating the project's development and deployment.

                Engaging directly with farming communities and implementing training programs are essential for encouraging adoption and ensuring that farmers can fully leverage the technology to improve their practices.

                The "Drone-based Crop Monitoring" project stands at the forefront of agricultural innovation, poised to redefine the paradigms of crop management and sustainability. By harnessing the capabilities of drone technology, this initiative aims to empower farmers with precise, actionable data, fostering informed decision-making and optimized agricultural practices. As the project progresses, its alignment with policy initiatives and its scalable, adaptable design promise to make a significant and lasting impact on the agricultural sector, paving the way for a future where technology and tradition converge to sustainably feed the world.
                """
                f"""
                example 3:

                As global agricultural demands continue to rise, the necessity for efficient, sustainable farming practices becomes increasingly paramount. The Smart Fertigation System project aims to revolutionize the way farmers manage and apply fertilizers by utilizing advanced technology to optimize nutrient delivery. This innovative approach promises to enhance crop yield, reduce environmental impact, and save resources by ensuring that fertilization is precisely tailored to the crops' needs at optimal times.

                The agricultural sector is under growing scrutiny to adopt practices that are both productive and sustainable. Excessive and improper use of fertilizers has been linked to environmental problems such as water pollution and soil degradation. There's a clear demand for methods that can increase crop yield without exacerbating these issues.

                Farmers are continually seeking ways to optimize resource use, including water, nutrients, and labor. Traditional fertigation methods often fall short in precision, leading to wasted resources and less-than-ideal crop outcomes.

                The trend towards integrating technology into farming practices is on the rise, with more farmers recognizing the benefits of data-driven decision-making. Technologies that offer real-time insights and automated processes are particularly valued for their potential to improve efficiency and outcomes.

                Policies aimed at promoting sustainable agriculture practices could support the adoption of smart fertigation systems. These policies might include incentives for farmers who implement technologies that reduce environmental impact and improve water and nutrient use efficiency.

                Similar to the Digital India initiative, a focused mission on digital agriculture could significantly benefit projects like the Smart Fertigation System. This would promote the use of IoT, AI, and other digital tools in farming, encouraging innovation and technology adoption across the sector.

                By providing precise nutrient delivery tailored to the crops' specific needs, smart fertigation systems can significantly improve crop yield and quality. This precision ensures that plants receive the right amount of nutrients at the right time, optimizing growth conditions.

                Smart fertigation systems minimize the risk of fertilizer runoff and leaching, thereby reducing the impact of farming on local water bodies and ecosystems. This approach aligns with broader environmental goals and regulatory requirements.

                Automating the fertigation process not only saves labor but also increases the efficiency of water and fertilizer use. This is critical in regions facing water scarcity and where the cost of inputs represents a significant burden for farmers.

                The flexible design of smart fertigation systems allows for their application across a wide range of crops and environmental conditions. This adaptability is key to the technology's scalability and potential for widespread impact.

                The potential for smart fertigation systems to integrate seamlessly with existing farm management systems and digital agriculture tools enhances their utility. This integration can provide a more holistic view of farm operations, facilitating better decision-making.

                Given the modular and increasingly cost-effective nature of smart technology, there is significant potential for the broad adoption of smart fertigation systems. This potential extends from smallholder farms to large-scale agricultural operations, both in India and globally.

                Partnerships with companies specializing in smart agriculture technologies can provide access to cutting-edge solutions and expertise, ensuring the fertigation system remains at the forefront of innovation.

                Leveraging government grants, subsidies, and support programs can help overcome initial setup costs and barriers to adoption, making the technology accessible to a wider range of farmers.

                Educational initiatives and training programs are essential to ensure farmers are equipped to implement and maximize the benefits of smart fertigation systems. These programs can also foster community engagement and feedback, driving continuous improvement.

                The Smart Fertigation System project represents a forward-thinking solution to modern agricultural challenges, offering a sustainable, efficient, and technology-driven approach to fertigation. By aligning with government policies promoting sustainable and digital agriculture, and leveraging available resources and partnerships, this project has the potential to transform agricultural practices. Its impact on enhancing crop yield and quality, reducing environmental footprint, and improving resource efficiency underscores its value and necessity in today's farming landscape. As the project evolves, its adaptability, scalability, and potential for broad adoption promise to make a significant contribution to the future of agriculture.
                """
                f"You are an Educator with real-world knowledge in {engineering_stream}. "
                f"Given a student's career choice as {career_choice} and interest in {domain_sector}. "
                f"and taking into account the Indian market and recent government policies given the context of the latest trends: {context}"
                f"provide me an overview of the project {question} using the above 3 examples as a reference on how to output the overview, "
                f"remember to include a title for the project {question} exactly like in the three examples, "
                f"remember to include an introduction of the project {question} exactly like in the three examples, "
                f"remember to include the relevance in the current indian market of the project {question} exactly like in the three examples, "
                f"remember to include indian government policies that can be applied to the project {question} exactly like in the three examples, "
                f"remember to include what impact the project {question} might have exactly like in the three examples, "
                f"remember to include the scability of the project {question} exactly like in the three examples, "
                f"remember to include the available resources that will help the student to make the project {question} exactly like in the three examples, "
                f"remember to include a conclusion on the project {question} exactly like in the three examples.",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        engineering_stream=engineering_stream,
        career_choice=career_choice,
        domain_sector=domain_sector,
        user_input=question,
        context=context,
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_respone_final_report(
    question, context, engineering_stream, career_choice, domain_sector
):

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:

                The Crop Yield Prediction Using Machine Learning project was initiated to develop a predictive model that leverages environmental and agricultural data to forecast crop yields. Through the integration of machine learning (ML) techniques with extensive datasets, the project aimed to enable farmers to make informed decisions, optimize their farming practices, and maximize yields. This report outlines the project's objectives, methodology, results, challenges, and future directions.

                The primary goal of the project was to create a robust machine learning model capable of accurately predicting crop yields based on a variety of factors, including soil properties, weather conditions, crop types, and farming practices. Key objectives included:
                - Collecting and preprocessing a comprehensive dataset of environmental and agricultural variables.
                - Developing and validating an ML model with high predictive accuracy.
                - Deploying the model in a user-friendly application for real-time crop yield predictions.

                Data was sourced from multiple channels, including IoT sensors in fields (measuring soil moisture, temperature, etc.), drones (for aerial imagery), and historical crop yield records. The data underwent extensive preprocessing, including cleaning, normalization, and feature engineering, to prepare it for model training.

                Several ML algorithms were evaluated, including linear regression, decision trees, random forests, and neural networks. The models were trained on a split dataset, with 70% used for training and 30% for validation. Performance metrics such as R-squared, mean absolute error (MAE), and mean squared error (MSE) were used to evaluate model accuracy.

                The best-performing model, a random forest algorithm with feature selection, was integrated into a web-based application. This platform provides a simple interface where farmers can input data about their fields and receive yield predictions. The application also offers insights and recommendations for optimizing crop yields.

                The random forest model demonstrated high accuracy, with an R-squared value of 0.85, MAE of 1.2 tons per hectare, and MSE of 2.4 tons per hectare in yield prediction. The user-friendly application has been successfully deployed and is currently being utilized by a pilot group of farmers, who have reported improved decision-making and increased yields as a result.

                Initial challenges included inconsistent data quality and limited access to historical yield data. These were addressed by establishing partnerships with agricultural research institutes and deploying additional sensors to enhance data collection.

                The complexity of the initial neural network model made it difficult for end-users to understand how predictions were made. By switching to a random forest model, we maintained high accuracy while improving interpretability and trust among users.

                Ensuring the system could handle increasing amounts of data required infrastructure adjustments. Cloud-based solutions and efficient data management practices were implemented to enhance scalability.

                - **Data Enrichment:** Incorporating more diverse data sources, such as satellite imagery and genetic information of crops, to further improve model accuracy.
                - **Advanced Modeling Techniques:** Exploring deep learning and ensemble methods to enhance predictive performance and adaptability to different crop types.
                - **User Engagement:** Expanding the user base through targeted outreach and incorporating user feedback to refine the application's functionality and usability.
                - **Sustainability Integration:** Developing features that predict the environmental impact of farming practices, supporting sustainable agriculture.

                The Crop Yield Prediction Using Machine Learning project represents a significant advancement in agricultural technology. By leveraging ML algorithms, the project delivers actionable insights to farmers, helping them to increase efficiency and crop yields. Although challenges remain, ongoing improvements and expansions are expected to increase the project's impact, contributing to more informed and sustainable agricultural practices worldwide.
                """
                f"""
                example 2:

                The Drone-based Crop Monitoring project sought to enhance agricultural productivity and sustainability by utilizing drone technology for detailed monitoring of crop health and environmental conditions. This initiative aimed to provide farmers with precise, real-time data to optimize agricultural practices, improve crop management, and facilitate timely interventions. This report summarizes the project's objectives, methodologies, outcomes, challenges faced, and potential future directions.

                The main objective was to deploy an advanced drone-based monitoring system capable of capturing high-resolution and multispectral imagery to assess crop health, identify potential issues early, and predict yields more accurately. Specific goals included:
                - Establishing a fleet of drones equipped with the necessary imaging technology.
                - Developing an analytical platform to process and interpret the collected data.
                - Creating a user-friendly interface for farmers to access insights and make informed decisions.

                A fleet of drones equipped with high-resolution and multispectral cameras was deployed to collect aerial imagery of agricultural fields. These drones conducted regular flights to gather data on vegetation indices, soil moisture levels, and other critical indicators of crop health.

                The collected imagery underwent processing to stitch together comprehensive field maps and extract relevant features. Advanced algorithms analyzed these features to identify signs of stress, pest infestation, or nutrient deficiencies in crops.

                A web-based platform was developed to present the analyzed data to farmers. This platform included visualization tools for easy interpretation of the data and integrated decision-support systems to advise on potential interventions.

                The of the drone-based monitoring system resulted in the successful collection and analysis of crop and field data across multiple pilot sites. The system demonstrated significant potential in detecting early signs of crop stress, improving water management, and optimizing fertilizer use. Farmers using the platform reported greater control over their agricultural practices and observed notable improvements in crop yields and resource efficiency.

                Initial challenges included the integration of drone data with the analytical platform and ensuring the reliability of data under varying weather conditions. These were overcome through the development of robust data processing pipelines and the use of drones capable of operating in diverse environmental conditions.

                Encouraging farmers to adopt this new technology presented another challenge. This was addressed by conducting workshops, providing hands-on demonstrations, and showcasing tangible benefits through case studies of early adopters.

                Scaling the system to cover larger areas and more diverse crop types required enhancements in data processing capabilities and drone fleet management. Solutions included cloud-based data storage and processing, as well as additional drones with varied sensing technologies.

                - **Enhanced Analytical Models:** Implementing AI and machine learning models to improve the accuracy of crop health assessments and yield predictions.
                - **Integration with Other Technologies:** Combining drone data with ground sensor data and satellite imagery for a more comprehensive monitoring system.
                - **Expansion to New Markets:** Extending the service to more regions and crop types, adapting the technology to meet the specific needs of different agricultural sectors.
                - **Sustainability Metrics:** Developing indicators for measuring the sustainability of farming practices based on drone data, supporting global efforts towards sustainable agriculture.

                The Drone-based Crop Monitoring project has established a foundation for transforming agricultural practices through advanced technology. By providing detailed, actionable insights into crop health and environmental conditions, the project empowers farmers to make more informed decisions, leading to increased productivity and sustainability. As the project evolves, it will continue to adapt and expand, offering new tools and insights to support the agriculture industry's future needs.
                """
                f"""
                example 3:

                The Smart Fertigation System project was conceived to revolutionize the way fertilization and irrigation are managed in agriculture. By incorporating Internet of Things (IoT) technology and data analytics, this system provides precision in the delivery of water and nutrients directly to crop roots, optimizing resource use and enhancing crop yields. This report encapsulates the project's goals, methodology, achievements, encountered challenges, and prospective future developments.

                The project aimed to develop a smart fertigation system capable of adjusting water and nutrient delivery in real-time based on the specific needs of crops. Objectives included:
                - Designing and deploying a network of soil and environmental sensors to monitor field conditions accurately.
                - Developing a data-driven decision-making platform for precise fertigation.
                - Creating an intuitive interface for farmers to monitor their crops and manage fertigation schedules efficiently.

                A comprehensive array of soil moisture, nutrient level, and climate condition sensors was installed across various agricultural fields to collect real-time data. This setup was intended to capture a detailed picture of the crop environment.

                The collected data were processed through a centralized platform that utilized advanced algorithms to analyze conditions and determine optimal fertigation schedules. This system considered factors such as crop type, growth stage, and local weather patterns.

                The decision-making logic was integrated with fertigation hardware, allowing automated adjustments to irrigation and fertilization practices. A user-friendly dashboard was developed for farmers, providing them with insights, alerts, and manual controls over the fertigation process.

                The implementation of the Smart Fertigation System demonstrated significant improvements in water and nutrient use efficiency across pilot sites. Farmers reported an increase in crop yield and quality while noting substantial reductions in water usage and fertilizer costs. The system's predictive capabilities also allowed for proactive management of field conditions, reducing the risk of over- or under-fertilization.

                Initial challenges included ensuring the reliability of sensor data and integrating various hardware components. These issues were addressed through rigorous testing, selection of high-quality sensors, and development of robust software for hardware integration.

                Promoting the adoption of the system among farmers required overcoming skepticism and unfamiliarity with the technology. Solution strategies included conducting on-site demonstrations, offering initial setup support, and providing comprehensive training materials.

                Ensuring the security and privacy of the collected agricultural data was paramount. The project team implemented advanced encryption methods and secure data storage solutions, along with clear data governance policies.

                - **Advanced Analytics Enhancement:** Incorporating machine learning models to further refine fertigation recommendations based on historical data and predictive analytics.
                - **Expansion to Additional Crops:** Tailoring the system for a wider variety of crops by incorporating specific crop models and nutrient requirements.
                - **Integration with Broader Farm Management Systems:** Creating interoperability with other agricultural technology systems, such as crop health monitoring and pest management tools, for a holistic approach to farm management.
                - **Sustainability Impact Tracking:** Developing features to monitor and report on the environmental impact of fertigation practices, aiding farmers in achieving sustainability goals.

                The Smart Fertigation System project marks a significant advancement in agricultural technology, offering a practical solution for the precise management of water and nutrients. The project not only achieves enhanced crop yields and resource conservation but also sets the stage for future innovations in sustainable farming practices. Moving forward, the project will continue to evolve, addressing new agricultural challenges and expanding its benefits to a broader farming community.
                """
                f"You are an Educator with real-world knowledge in {engineering_stream}. "
                f"Given a student's career choice as {career_choice} and interest in {domain_sector}. "
                f"provide me a final report of the project {question} with the most recent trends and context: {context} using the above 3 examples as a reference on how to output the final report, "
                f"remember to include a title for the project {question} exactly like in the three examples, "
                f"remember to include an executive summary of the project {question} exactly like in the three examples, "
                f"remember to include the project objectives of the project {question} exactly like in the three examples, "
                f"remember to include methodology of the project {question} exactly like in the three examples, "
                f"remember to include the results of the project {question} exactly like in the three examples, "
                f"remember to include the challenges and solutions of the project {question} exactly like in the three examples, "
                f"remember to include the future directions of the project {question} exactly like in the three examples, "
                f"remember to include a conclusion on the project {question} exactly like in the three examples.",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        engineering_stream=engineering_stream,
        career_choice=career_choice,
        domain_sector=domain_sector,
        user_input=question,
        context=context,
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_response_x(
    question, context, engineering_stream, career_choice, domain_sector
):

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are an Educator with real-world knowledge in {engineering_stream} who teaches first year students or freshman year students. "
                f"Given a first year student's career choice as {career_choice} and interest in {domain_sector}. "
                f"Remember you are providing projects for first year students or freshman year students so keep the complexity of the projects realistic and approachable with a basic level of knowledge."
                f"Generate and display 15 unique and interesting applications which are realistically doable by first year or freshman year students that are specific to the {engineering_stream} , {domain_sector}, {career_choice} for hands-on projects relevant to current trends in India using the context: {context} 3 examples as a reference on how to output the applications. Remember to provide an overview of 2 lines after the colon after listing the course. Do not provide any heading or overall description above or below the applications."
                f"Keep the {context} in mind while generating the projects for first year students since its important to keep the projects unique and up to date. "
                f"Provided below are examples for the format of. DONT generate the projects given in the format example everytime, use it as a reference for formating the output. "
                f"Don't take inspiration for the content of the projects from the examples below, only take inspiration for the format of the output."
                f"""
                General Format:
                1. **Project Heading:** Project Overview.
                2. **Project Heading:** Project Overview. 
                3. **Project Heading:** Project Overview.               
                4. **Project Heading:** Project Overview.
                5. **Project Heading:** Project Overview.
                6. **Project Heading:** Project Overview.
                7. **Project Heading:** Project Overview.
                8. **Project Heading:** Project Overview.
                9. **Project Heading:** Project Overview.
                10. **Project Heading:** Project Overview.
                11. **Project Heading:** Project Overview.
                12. **Project Heading:** Project Overview.
                13. **Project Heading:** Project Overview.
                14. **Project Heading:** Project Overview.
                15. **Project Heading:** Project Overview.

                Format Example for reference 1:
                1. **Health Monitoring System:** Develop an IoT-based system to monitor vital health parameters (e.g., blood pressure, heart rate) and transmit data to healthcare providers.
                2. **Telemedicine Platform:** Create a web or mobile application that enables remote consultation and diagnosis between patients and healthcare professionals.
                3. **Medical Image Analysis:** Design an AI-powered system to analyze medical images (e.g., X-rays, MRI scans) for disease detection and diagnosis.
                4. **Health Data Management System:** Build a centralized system to store, manage, and analyze large volumes of health data for population health 
                management.
                5. **E-Health Records System:** Develop a secure and accessible system for storing and sharing electronic health records, improving patient care coordination.
                6. **Health Education and Awareness App:** Create a mobile application that provides health information, resources, and support to promote healthy living and well-being.
                7. **Remote Patient Monitoring and Management:** Design a wearable or IoT device to monitor patient health metrics in real-time and provide alerts to healthcare providers.
                8. **Health Insurance Optimization Platform:** Develop an AI-based system to analyze health insurance data and identify opportunities for cost optimization and improved coverage.
                9. **Health Policy Analysis and Simulation:** Build a simulation model to analyze the impact of different health policies on population health outcomes and economic costs.
                10. **Medical Device Development:** Design and prototype innovative medical devices that address unmet healthcare needs, such as wearable health sensors or diagnostic tools.
                11. **Health Workforce Planning and Management:** Develop a data-driven system to forecast future healthcare workforce needs and optimize staffing levels.
                12. **Health Equity and Access Improvement:** Design a web or mobile application that connects underserved populations with healthcare resources and services.
                13. **Public Health Surveillance and Outbreak Detection:** Build a system to monitor and analyze public health data to identify disease outbreaks 
                and implement early intervention measures.
                14. **Health Research and Development:** Utilize machine learning and data analytics to extract insights from clinical data and support health research advancements.
                15. **Health Economics and Outcomes Analysis:** Develop models to evaluate the cost-effectiveness and outcomes of different healthcare interventions and policies.

                Format Example for reference 2:
                1. **Solar Energy Prediction using Machine Learning:** Develop a model to predict solar energy output using historical data and machine learning algorithms.
                2. **Wind Turbine Optimization using Data Analytics:** Analyze data from wind turbines to optimize their performance and increase energy efficiency.
                3. **Smart Grid Management with IoT:** Design an IoT-based system to monitor and manage smart grids, ensuring efficient energy distribution and reducing power outages.
                4. **Grid-Connected PV System Design and Simulation:** Model and simulate a grid-connected photovoltaic system to optimize its design and maximize energy production.
                5. **Electric Vehicle Charging Infrastructure Optimization:** Develop algorithms to optimize the placement and utilization of electric vehicle charging stations based on demand and grid constraints.
                6. **Energy Storage System Design for Renewables:** Design and evaluate energy storage systems for renewable energy sources, such as batteries or 
                pumped hydro storage.
                7. **Renewable Energy Resource Assessment using Satellite Data:** Utilize satellite data to assess the potential of renewable energy sources, such as solar and wind, in different regions.
                8. **Hydroelectric Power Plant Simulation and Control:** Model and simulate a hydroelectric power plant to optimize its operation and improve energy generation efficiency.
                9. **Microgrid Design and Control for Rural Electrification:** Design and implement microgrids for rural areas, utilizing renewable energy sources to provide reliable electricity.
                10. **Biofuel Production Optimization using Computational Fluid Dynamics:** Utilize CFD simulations to optimize biofuel production processes and maximize yield.
                11. **Geothermal Energy Modeling and Simulation:** Develop models and simulations to assess the potential and optimize the extraction of geothermal energy.
                12. **Energy Efficiency in Buildings using Building Information Modeling:** Utilize BIM to design and optimize energy-efficient buildings, reducing energy consumption and carbon emissions.
                13. **Renewable Energy Policy Analysis using Data Science:** Analyze data to identify trends and patterns in renewable energy policies and their impact on energy production.
                14. **Smart Home Energy Management with AI:** Design and implement AI-powered smart home energy management systems to reduce energy consumption and optimize energy usage.
                15. **Renewable Energy Education Platform Development:** Create an online or mobile platform to provide interactive and engaging educational resources on renewable energy and its applications.
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
        context=context,
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_response_roadmap_x(question, context, domain_sector):
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:

                Agriculture, Data Analysis

                Develop a sophisticated machine learning model designed to forecast crop yields with high accuracy, leveraging environmental and agricultural data. This model aims to equip farmers with predictive insights that enable strategic planning, resource optimization, and maximization of agricultural outputs.

                - **Languages:** Deep proficiency in Python for its extensive data science ecosystem and R for statistical analysis. Both languages are essential for manipulating datasets, applying statistical models, and visualizing data insights.
                - **Machine Learning Libraries:** Expertise in scikit-learn for its comprehensive suite of machine learning tools, TensorFlow for deep learning applications critical in handling complex datasets, and Keras for building and deploying neural network models.
                - **Skills:** Advanced skills in data analysis for uncovering trends and patterns, machine learning modeling to build predictive algorithms, data preprocessing to clean and prepare data, and feature engineering to extract and select meaningful data points.
                - **Tools:** Proficiency in Jupyter Notebook for interactive development and testing, PyCharm or RStudio for robust development environments, and Tableau or Power BI for creating dynamic data visualizations for stakeholders.
                - **Resources:** A commitment to leveraging online tutorials for upskilling, documentation for understanding library functionalities, and participation in community forums for problem-solving and staying updated on industry trends.

                - **Sensors:** Implementation of a network of IoT sensors across multiple test fields to gather micro-climatic data (e.g., soil moisture levels using capacitive moisture sensors, temperature and humidity with DHT sensors) and crop health indicators (e.g., NDVI sensors for vegetation health).
                - **Drones:** drones equipped with high-resolution and multispectral cameras to capture detailed aerial imagery, enabling precise monitoring of crop growth, pest infestation, and water stress levels across vast areas.
                - **Tractors and Equipment:** Integration of smart data loggers on tractors and farming machinery to systematically collect data on planting densities, soil compaction, and harvest volumes, enhancing the dataset with operational insights.

                - **Simulation Models:** Development of complex agronomic models to simulate crop growth stages under varying environmental conditions, providing a virtual testing ground for yield predictions without the need for direct field data.
                - **Remote Sensing Data:** Adoption of satellite imagery and aerial photography services to obtain comprehensive, large-scale data on vegetation health, land use, and environmental factors impacting crop growth.
                - **Historical Data Analysis:** Compilation and analysis of extensive historical datasets from agricultural databases, research institutions, and weather stations to inform model predictions with trends and patterns observed over years.

                - **Data Acquisition:** Establish partnerships with agricultural research institutes and local farming cooperatives to access diverse datasets, including sensor data, drone imagery, and operational logs from farm equipment.
                - **Data Cleaning:** Employ sophisticated data cleaning techniques to address noise, outliers, and missing values. Techniques include temporal data interpolation for filling gaps and robust statistical methods to identify and correct anomalies.
                - **Data Exploration:** Conduct an in-depth exploratory data analysis (EDA) using advanced visualization tools to uncover underlying data structures, correlations between variables, and potential predictors of crop yield.

                - **Feature Extraction:** Apply domain-specific knowledge to extract relevant features from raw data, such as calculating vegetation indices from drone imagery or deriving soil health metrics from sensor data.
                - **Feature Construction:** Innovate by creating new features that capture the interactions between different environmental and agricultural factors, using techniques like polynomial feature combinations to model complex relationships.
                - **Feature Selection:** Implement machine learning-based feature selection methods, such as recursive feature elimination (RFE) or model-based selection, to identify and retain features with the highest predictive power.

                - **Model Selection:** Evaluate multiple machine learning models, including ensemble methods like Random Forest and gradient boosting machines (GBM), and deep learning approaches like Convolutional Neural Networks (CNNs) for image data analysis.
                - **Model Training:** Utilize advanced training techniques, including k-fold cross-validation to ensure model robustness and grid search or Bayesian optimization for hyperparameter tuning to enhance model performance.
                - **Model Evaluation:** Apply a comprehensive evaluation framework, using a mix of metrics (e.g., R^2 for model fit, RMSE for prediction accuracy) and domain-specific validation techniques, such as comparing predicted versus actual yields in controlled test plots.

                - **Documentation and Training:** Create detailed user guides and video tutorials to assist farmers in navigating the platform. Organize interactive webinars and workshops for hands-on training, aiming to enhance user confidence and encourage feedback for continuous improvement.

                - **Performance Monitoring:** Establish a system for ongoing monitoring of the model's predictive accuracy using real-world agricultural data. This includes setting up automated alerts for significant deviations in model performance metrics.
                - **Feedback Loop:** Create channels for regular feedback from the user community, including surveys, focus groups, and direct communication tools. This feedback is crucial for understanding the model's effectiveness and areas where it can be enhanced.
                - **Model Updates:** Implement a structured process for periodically updating the model with new data, insights, and user feedback. This includes refining algorithms, introducing new features, and adjusting model parameters to reflect the latest agricultural trends and technologies.
                """
                f"""
                example 2:

                Precision Agriculture, Remote Sensing

                This project seeks to revolutionize farm management by deploying drones equipped with advanced imaging technology to collect data on crop health, environmental conditions, and more. By analyzing this data with sophisticated algorithms, the project will provide actionable insights to farmers, enabling them to make informed decisions, optimize agricultural practices, and ultimately increase crop yields while promoting sustainability.

                - **Languages:** Mastery of Python for leveraging AI and machine learning libraries, and JavaScript for building interactive web applications.
                - **Remote Sensing Libraries:** In-depth knowledge of remote sensing libraries such as GDAL for geographic data manipulation, OpenCV for image processing, and PyTorch or TensorFlow for applying neural networks to image data.
                - **Skills:** Expertise in drone operation and imagery analysis, proficiency in GIS technology for mapping and spatial analysis, and strong analytical skills for data interpretation.
                - **Tools:** Proficiency with drone flight planning and monitoring software, GIS platforms like ArcGIS or QGIS for spatial data analysis, and web development environments such as Visual Studio Code or Atom.
                - **Resources:** Access to comprehensive online courses on remote sensing and GIS, specialized forums and communities for drone technology, and agricultural data science resources for continuous learning and troubleshooting.

                - **Drones:** Selection and procurement of high-capacity drones capable of carrying multispectral and thermal sensors for detailed field imagery.
                - **Ground Control Stations:** Setup of advanced ground control systems for real-time monitoring and management of drone flights.
                - **Computing Infrastructure:** Investment in high-performance computing resources for the storage, processing, and analysis of large datasets generated by drone flights.

                - **Automated Data Processing System:** Development of an automated pipeline for processing and analyzing drone-captured imagery, including features for image stitching, enhancement, and feature extraction.
                - **Predictive Analytics Engine:** Creation of predictive models using machine learning to analyze crop health indicators, predict potential yield, and identify areas requiring intervention.
                - **Farmer Dashboard:** Design and implementation of a secure, user-friendly web dashboard that provides farmers with easy access to insights, visualizations, and recommendations derived from drone data.

                - **Technical Specifications:** Define the technical specifications for drones, including sensor requirements, battery life, and payload capacity to ensure comprehensive field coverage and data collection capabilities.
                - **Software Architecture Planning:** Outline the architecture for the data processing and analysis pipeline, ensuring scalability, efficiency, and integration capability with external platforms and APIs.
                - **Pilot Area Selection:** Choose diverse agricultural regions for pilot testing to cover a range of crops, climates, and farming practices, ensuring the system's adaptability and effectiveness.

                - **Drone Flight Operations:** Conduct systematic drone flights over pilot areas to collect high-resolution and multispectral imagery, focusing on different times of day and crop stages for comprehensive data.
                - **Data Processing Workflow:** Implement the data processing workflow to clean, stitch, and enhance images, preparing them for detailed analysis.
                - **Preliminary Data Analysis:** Perform initial data analysis to identify patterns, anomalies, and insights that can inform crop health assessments and management decisions.

                - **Feature Engineering:** Utilize remote sensing data to engineer features relevant to crop health, such as vegetation indices and thermal anomalies, that serve as inputs for machine learning models.
                - **Model Training and Testing:** Train machine learning models on the engineered features to identify crop health issues, estimate yield, and detect areas needing intervention; thoroughly test models for accuracy and reliability.
                - **Validation with Experts:** Collaborate with agronomists and farming experts to validate model predictions against real-world observations and outcomes, refining models based on expert feedback.

                - **User Interface Creation:** Develop an intuitive, interactive web interface that allows farmers to access personalized insights, view aerial imagery, and receive actionable recommendations.
                - **User Training and Support:** Provide comprehensive training materials, online tutorials, and support services to assist farmers in utilizing the platform effectively.

                - **Expansion to New Regions:** Gradually expand the service to new geographical regions and crop types, adapting the system based on regional agricultural practices and challenges.
                - **Feedback Loop and Iteration:** Establish mechanisms for collecting user feedback, monitoring system performance, and iteratively improving the data analysis models and user interface based on real-world usage and evolving agricultural technologies.
                - **Stakeholder Engagement:** Engage continuously with farmers, agricultural advisors, and researchers to enhance the system's relevance and impact, fostering a community of practice
                """
                f"""
                example 3:

                Smart Agriculture, Irrigation Technology

                To create a highly efficient smart fertigation system that leverages IoT (Internet of Things) technology and advanced data analytics to precisely manage the delivery of water and nutrients to crops. This project aims to enhance crop yields, minimize resource wastage, and support sustainable farming practices by ensuring that fertilization is dynamically adjusted based on real-time soil and plant needs.

                - **Languages:** Proficiency in Python for backend development and data analysis; familiarity with JavaScript for frontend web application development.
                - **IoT Platforms:** In-depth knowledge of IoT platforms such as Arduino or Raspberry Pi for sensor integration and data collection.
                - **Data Analytics Libraries:** Expertise in data analytics and machine learning libraries, such as Pandas for data manipulation, NumPy for numerical analysis, and Scikit-learn for predictive modeling.
                - **Skills:** Strong background in IoT system design, data analytics, machine learning, and web development; understanding of agronomy and irrigation principles is essential.
                - **Tools:** Experience with IoT development environments, database management systems (e.g., PostgreSQL, MongoDB), and web development frameworks (e.g., React, Flask).

                - **Sensors:** of soil moisture sensors, nutrient level detectors, and climate sensors to monitor environmental conditions and crop health.
                - **Controllers:** Utilization of smart controllers capable of processing sensor data and managing irrigation and fertilizer distribution systems based on predefined algorithms.
                - **Networking Equipment:** Installation of reliable networking equipment to facilitate communication between sensors, controllers, and the central data management system.

                - **Data Management Platform:** Development of a centralized data management platform to aggregate, process, and analyze data collected from various sensors and controllers.
                - **Predictive Modeling Software:** Creation of predictive models to forecast crop nutrient requirements and optimize fertigation schedules.
                - **User Interface (UI):** Designing an intuitive web-based UI that allows farmers to monitor real-time data, receive alerts and recommendations, and adjust fertigation parameters manually if needed.

                - **Component Selection:** Careful selection of sensors and controllers that meet the requirements for accuracy, durability, and cost-effectiveness.
                - **Prototype Design:** Design and assemble a prototype system that integrates sensors, controllers, and networking equipment to test functionality and gather preliminary data.
                - **Software Architecture:** Outline the software architecture for the data management platform and predictive modeling software, ensuring scalability and user accessibility.

                - **Pilot Implementation:** Deploy the prototype system in a controlled pilot environment to collect data on soil moisture, nutrient levels, and other relevant agronomic factors.
                - **Data Processing and Analysis:** Implement data processing workflows to clean and analyze the collected data, identifying key patterns and relationships between soil/plant conditions and crop health/yield.

                - **Predictive Model Development:** Develop and train machine learning models to predict crop nutrient requirements and optimal fertigation schedules based on collected data and agronomic principles.
                - **System Refinement:** Refine the prototype system based on data analysis and model predictions, optimizing sensor placement, controller logic, and networking efficiency for improved performance.

                - **Data Management Platform:** Build a robust data management platform that integrates with the smart fertigation system, supporting data aggregation, processing, and analysis.
                - **UI Development:** Design and develop a user-friendly web-based UI that provides farmers with insights, alerts, and recommendations generated by the predictive models, and allows for manual system adjustments.

                - **Field Testing:** Conduct extensive field testing in diverse agricultural settings to validate system performance, model accuracy, and user satisfaction.
                - **Feedback Collection:** Gather feedback from end-users (farmers) and agronomy experts to identify areas for improvement in the system design, software functionality, and user interface.
                - **Commercial:** Finalize the smart fertigation system for commercial, incorporating feedback from field testing and ensuring scalability, reliability, and ease of use.
                """
                f"As an Educator with real-world knowledge in {domain_sector} and the most recent trends and context: {context} you possess the expertise to offer detailed and practical advice to address users' questions effectively. Drawing upon your background, you can break down complex concepts into manageable subtasks, providing actionable steps and strategies tailored to the specific project. Your insights bridge the gap between theory and practice, empowering learners with the skills and knowledge they need to succeed in real-world settings."
                f"provide me a roadmap of the project {question} using the above 3 examples as a reference on how to output the roadmap, "
                f"remember to include a project category of the project {question} exactly like in the three examples, "
                f"remember to include knowledge requirements for the the project {question} exactly like in the three examples, "
                f"remember to hardware products (if feasible) related to the project {question} exactly like in the three examples, "
                f"remember to include software alternatives (if hardware is not feasible) related to the the project {question} might have exactly like in the three examples, "
                f"remember to include the detailed phases(excluding a deployment phase) of the roadmap of the project {question} exactly like in the three examples, ",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        domain_sector=domain_sector, user_input=question, context=context
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_respone_overview_x(
    question, context, engineering_stream, career_choice, domain_sector
):

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:

                In an era where technology bridges gaps across various sectors, the legal field in India is poised for a transformation that caters to the needs of its citizens more efficiently. The "Legal Chatbot for Citizen Assistance" project stands at this juncture, aiming to leverage artificial intelligence to democratize access to legal information and assistance, especially for the marginalized and underprivileged communities.

                India's diverse population, characterized by significant disparities in income, education, and access to resources, underscores the critical need for legal assistance. Marginalized and underprivileged communities often find themselves entangled in legal issues without the means to seek justice. The digital divide further exacerbates this situation, leaving a substantial portion of the population, particularly in rural and remote areas, in a legal vacuum.

                Despite the presence of legal aid clinics and organizations, the reach is limited, often constrained by geographical, financial, and informational barriers. The burgeoning case loads on courts and legal professionals underline the pressing need for alternative solutions to legal assistance that are both effective and scalable.

                The silver lining lies in the increasing penetration of technology within the legal sector. Digital platforms and solutions are being increasingly recognized as viable means to address the systemic gaps in legal assistance delivery.

                This act provides a robust framework for the delivery of legal aid to the poor and disadvantaged, setting a precedent for initiatives aimed at enhancing access to justice.

                The policy emphasizes the integration of technology in legal aid delivery, advocating for innovative solutions like the proposed legal chatbot to streamline and enhance the accessibility of legal services.

                Aligned with the Digital India Mission's objectives, this project leverages digital technologies for citizen empowerment, ensuring that legal assistance is just a click away for anyone in need.

                By providing a platform that is accessible 24/7, the chatbot significantly lowers the barriers to legal information, making it easier for citizens to understand their legal rights and the remedies available to them.

                Automating the initial stages of legal consultation can alleviate the workload on courts and legal practitioners, allowing them to focus on more complex aspects of legal service delivery.

                The chatbot serves not just as a tool for legal assistance but also as a means for legal education, empowering citizens with the knowledge to navigate the legal system more effectively.

                By digitizing legal assistance, the project introduces a level of transparency and accountability into the system, building trust and confidence among citizens.

                The chatbot's design allows for across various platforms, including websites, mobile apps, and social media, ensuring wide accessibility.

                Potential integrations with existing government portals and legal databases can enrich the chatbot's resource base, making it a comprehensive tool for legal assistance.

                Built to scale, the chatbot can manage a vast number of inquiries simultaneously, providing timely assistance to citizens nationwide.

                Collaborations with existing legal aid clinics and organizations can provide a foundation of legal knowledge and expertise to support the chatbot's development.

                Access to government legal databases will enable the chatbot to provide accurate and up-to-date legal information, enhancing its effectiveness.

                Leveraging open-source chatbot frameworks can expedite the development process, allowing for customization and scalability according to project needs.

                Engaging legal professionals in the project can ensure that the chatbot's responses are vetted for accuracy and relevance, maintaining a high standard of legal assistance.

                The "Legal Chatbot for Citizen Assistance" project emerges as a beacon of innovation in the Indian legal landscape, promising to bridge the gap between legal services and the citizens they aim to serve. By harnessing technology, this project not only aligns with government policies but also sets a new standard for legal assistance in India. Through its scalable design and impactful delivery, it has the potential to transform legal accessibility, making justice truly accessible to all.
                """
                f"""
                example 2:

                In an era where technological innovation drives progress across various sectors, agriculture stands on the brink of a significant transformation. The "Drone-based Crop Monitoring" project seeks to leverage the power of drone technology to revolutionize how crops are monitored, managed, and optimized. This initiative is positioned to offer unprecedented insights into crop health and environmental conditions, thereby facilitating informed decision-making, enhancing productivity, and promoting sustainable agricultural practices.

                The agricultural sector is under increasing pressure to meet the global demand for food, which is set to rise substantially in the coming decades. Efficient crop management is crucial for maximizing yield, conserving resources, and minimizing environmental impact. The advent of precision agriculture, facilitated by technological advancements, offers a pathway to achieving these goals.

                Traditional crop monitoring methods are often labor-intensive, time-consuming, and prone to errors, making it difficult to respond promptly to issues. Furthermore, access to advanced agricultural technologies remains limited, especially in developing regions, exacerbating the challenges of ensuring food security and sustainable farming practices.

                The integration of technology in agriculture, particularly through the adoption of drones, presents a significant opportunity to overcome these challenges. Drones offer a unique vantage point and the ability to deploy advanced imaging technologies, making them a pivotal tool in the evolution of agricultural practices.

                Although not yet existent, a hypothetical national policy on precision agriculture could serve as a crucial framework for integrating drone technology in agricultural practices. This policy would encourage the adoption of precision farming techniques, including drone-based monitoring, to improve crop yield and resource efficiency.

                Aligned with the broader Digital India initiative, a specialized mission focusing on the digitization of agriculture could support projects like drone-based crop monitoring. Such a mission would aim to bridge the technological gap in agriculture, promoting innovation and technology adoption across the sector.

                By providing detailed, real-time data on crop health and environmental conditions, drone-based monitoring can significantly enhance agricultural productivity. This technology enables precise interventions, optimizing resource use and maximizing crop yield.

                Drones facilitate efficient water, fertilizer, and pesticide use, contributing to sustainable resource management. By identifying precisely where and how much of these inputs are needed, the technology helps reduce waste and environmental impact.

                The project contributes to sustainable agricultural practices by promoting efficient resource use and minimizing the adverse effects of farming on the environment. In the long term, this will help ensure food security and the health of agricultural ecosystems.

                The drone-based crop monitoring system is designed to be adaptable and scalable across different crops and geographical areas. This versatility ensures that the benefits of the technology can be realized in diverse agricultural settings, from small family farms to large commercial operations.

                The project envisages seamless integration with existing agricultural technologies and data management systems, enhancing the utility and impact of drone-based monitoring within the broader ecosystem of agricultural innovation.

                Given its modular nature and the decreasing cost of drone technology, the project has the potential for wide adoption. Customization options allow for the technology to be tailored to specific crops, climates, and farming practices, further enhancing its applicability and impact.

                Partnerships with academic institutions and research bodies will be crucial in refining the technology, ensuring its relevance and effectiveness for various agricultural applications.

                Collaborations with government bodies and private sector stakeholders can provide the necessary support in terms of funding, regulatory guidance, and technological expertise, facilitating the project's development and deployment.

                Engaging directly with farming communities and implementing training programs are essential for encouraging adoption and ensuring that farmers can fully leverage the technology to improve their practices.

                The "Drone-based Crop Monitoring" project stands at the forefront of agricultural innovation, poised to redefine the paradigms of crop management and sustainability. By harnessing the capabilities of drone technology, this initiative aims to empower farmers with precise, actionable data, fostering informed decision-making and optimized agricultural practices. As the project progresses, its alignment with policy initiatives and its scalable, adaptable design promise to make a significant and lasting impact on the agricultural sector, paving the way for a future where technology and tradition converge to sustainably feed the world.
                """
                f"""
                example 3:

                As global agricultural demands continue to rise, the necessity for efficient, sustainable farming practices becomes increasingly paramount. The Smart Fertigation System project aims to revolutionize the way farmers manage and apply fertilizers by utilizing advanced technology to optimize nutrient delivery. This innovative approach promises to enhance crop yield, reduce environmental impact, and save resources by ensuring that fertilization is precisely tailored to the crops' needs at optimal times.

                The agricultural sector is under growing scrutiny to adopt practices that are both productive and sustainable. Excessive and improper use of fertilizers has been linked to environmental problems such as water pollution and soil degradation. There's a clear demand for methods that can increase crop yield without exacerbating these issues.

                Farmers are continually seeking ways to optimize resource use, including water, nutrients, and labor. Traditional fertigation methods often fall short in precision, leading to wasted resources and less-than-ideal crop outcomes.

                The trend towards integrating technology into farming practices is on the rise, with more farmers recognizing the benefits of data-driven decision-making. Technologies that offer real-time insights and automated processes are particularly valued for their potential to improve efficiency and outcomes.

                Policies aimed at promoting sustainable agriculture practices could support the adoption of smart fertigation systems. These policies might include incentives for farmers who implement technologies that reduce environmental impact and improve water and nutrient use efficiency.

                Similar to the Digital India initiative, a focused mission on digital agriculture could significantly benefit projects like the Smart Fertigation System. This would promote the use of IoT, AI, and other digital tools in farming, encouraging innovation and technology adoption across the sector.

                By providing precise nutrient delivery tailored to the crops' specific needs, smart fertigation systems can significantly improve crop yield and quality. This precision ensures that plants receive the right amount of nutrients at the right time, optimizing growth conditions.

                Smart fertigation systems minimize the risk of fertilizer runoff and leaching, thereby reducing the impact of farming on local water bodies and ecosystems. This approach aligns with broader environmental goals and regulatory requirements.

                Automating the fertigation process not only saves labor but also increases the efficiency of water and fertilizer use. This is critical in regions facing water scarcity and where the cost of inputs represents a significant burden for farmers.

                The flexible design of smart fertigation systems allows for their application across a wide range of crops and environmental conditions. This adaptability is key to the technology's scalability and potential for widespread impact.

                The potential for smart fertigation systems to integrate seamlessly with existing farm management systems and digital agriculture tools enhances their utility. This integration can provide a more holistic view of farm operations, facilitating better decision-making.

                Given the modular and increasingly cost-effective nature of smart technology, there is significant potential for the broad adoption of smart fertigation systems. This potential extends from smallholder farms to large-scale agricultural operations, both in India and globally.

                Partnerships with companies specializing in smart agriculture technologies can provide access to cutting-edge solutions and expertise, ensuring the fertigation system remains at the forefront of innovation.

                Leveraging government grants, subsidies, and support programs can help overcome initial setup costs and barriers to adoption, making the technology accessible to a wider range of farmers.

                Educational initiatives and training programs are essential to ensure farmers are equipped to implement and maximize the benefits of smart fertigation systems. These programs can also foster community engagement and feedback, driving continuous improvement.

                The Smart Fertigation System project represents a forward-thinking solution to modern agricultural challenges, offering a sustainable, efficient, and technology-driven approach to fertigation. By aligning with government policies promoting sustainable and digital agriculture, and leveraging available resources and partnerships, this project has the potential to transform agricultural practices. Its impact on enhancing crop yield and quality, reducing environmental footprint, and improving resource efficiency underscores its value and necessity in today's farming landscape. As the project evolves, its adaptability, scalability, and potential for broad adoption promise to make a significant contribution to the future of agriculture.
                """
                f"You are an Educator with real-world knowledge in {engineering_stream}. "
                f"Given a student's career choice as {career_choice} and interest in {domain_sector}. "
                f"and taking into account the Indian market and recent government policies given the context of the latest trends: {context}"
                f"provide me an overview of the project {question} using the above 3 examples as a reference on how to output the overview, "
                f"remember to include a title for the project {question} exactly like in the three examples, "
                f"remember to include an introduction of the project {question} exactly like in the three examples, "
                f"remember to include the relevance in the current indian market of the project {question} exactly like in the three examples, "
                f"remember to include indian government policies that can be applied to the project {question} exactly like in the three examples, "
                f"remember to include what impact the project {question} might have exactly like in the three examples, "
                f"remember to include the scability of the project {question} exactly like in the three examples, "
                f"remember to include the available resources that will help the student to make the project {question} exactly like in the three examples, "
                f"remember to include a conclusion on the project {question} exactly like in the three examples.",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        engineering_stream=engineering_stream,
        career_choice=career_choice,
        domain_sector=domain_sector,
        user_input=question,
        context=context,
    )

    response = llm.invoke(formatted_messages)
    return response


def get_gemini_respone_final_report_x(
    question, context, engineering_stream, career_choice, domain_sector
):

    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                example 1:

                The Crop Yield Prediction Using Machine Learning project was initiated to develop a predictive model that leverages environmental and agricultural data to forecast crop yields. Through the integration of machine learning (ML) techniques with extensive datasets, the project aimed to enable farmers to make informed decisions, optimize their farming practices, and maximize yields. This report outlines the project's objectives, methodology, results, challenges, and future directions.

                The primary goal of the project was to create a robust machine learning model capable of accurately predicting crop yields based on a variety of factors, including soil properties, weather conditions, crop types, and farming practices. Key objectives included:
                - Collecting and preprocessing a comprehensive dataset of environmental and agricultural variables.
                - Developing and validating an ML model with high predictive accuracy.
                - Deploying the model in a user-friendly application for real-time crop yield predictions.

                Data was sourced from multiple channels, including IoT sensors in fields (measuring soil moisture, temperature, etc.), drones (for aerial imagery), and historical crop yield records. The data underwent extensive preprocessing, including cleaning, normalization, and feature engineering, to prepare it for model training.

                Several ML algorithms were evaluated, including linear regression, decision trees, random forests, and neural networks. The models were trained on a split dataset, with 70% used for training and 30% for validation. Performance metrics such as R-squared, mean absolute error (MAE), and mean squared error (MSE) were used to evaluate model accuracy.

                The best-performing model, a random forest algorithm with feature selection, was integrated into a web-based application. This platform provides a simple interface where farmers can input data about their fields and receive yield predictions. The application also offers insights and recommendations for optimizing crop yields.

                The random forest model demonstrated high accuracy, with an R-squared value of 0.85, MAE of 1.2 tons per hectare, and MSE of 2.4 tons per hectare in yield prediction. The user-friendly application has been successfully deployed and is currently being utilized by a pilot group of farmers, who have reported improved decision-making and increased yields as a result.

                Initial challenges included inconsistent data quality and limited access to historical yield data. These were addressed by establishing partnerships with agricultural research institutes and deploying additional sensors to enhance data collection.

                The complexity of the initial neural network model made it difficult for end-users to understand how predictions were made. By switching to a random forest model, we maintained high accuracy while improving interpretability and trust among users.

                Ensuring the system could handle increasing amounts of data required infrastructure adjustments. Cloud-based solutions and efficient data management practices were implemented to enhance scalability.

                - **Data Enrichment:** Incorporating more diverse data sources, such as satellite imagery and genetic information of crops, to further improve model accuracy.
                - **Advanced Modeling Techniques:** Exploring deep learning and ensemble methods to enhance predictive performance and adaptability to different crop types.
                - **User Engagement:** Expanding the user base through targeted outreach and incorporating user feedback to refine the application's functionality and usability.
                - **Sustainability Integration:** Developing features that predict the environmental impact of farming practices, supporting sustainable agriculture.

                The Crop Yield Prediction Using Machine Learning project represents a significant advancement in agricultural technology. By leveraging ML algorithms, the project delivers actionable insights to farmers, helping them to increase efficiency and crop yields. Although challenges remain, ongoing improvements and expansions are expected to increase the project's impact, contributing to more informed and sustainable agricultural practices worldwide.
                """
                f"""
                example 2:

                The Drone-based Crop Monitoring project sought to enhance agricultural productivity and sustainability by utilizing drone technology for detailed monitoring of crop health and environmental conditions. This initiative aimed to provide farmers with precise, real-time data to optimize agricultural practices, improve crop management, and facilitate timely interventions. This report summarizes the project's objectives, methodologies, outcomes, challenges faced, and potential future directions.

                The main objective was to deploy an advanced drone-based monitoring system capable of capturing high-resolution and multispectral imagery to assess crop health, identify potential issues early, and predict yields more accurately. Specific goals included:
                - Establishing a fleet of drones equipped with the necessary imaging technology.
                - Developing an analytical platform to process and interpret the collected data.
                - Creating a user-friendly interface for farmers to access insights and make informed decisions.

                A fleet of drones equipped with high-resolution and multispectral cameras was deployed to collect aerial imagery of agricultural fields. These drones conducted regular flights to gather data on vegetation indices, soil moisture levels, and other critical indicators of crop health.

                The collected imagery underwent processing to stitch together comprehensive field maps and extract relevant features. Advanced algorithms analyzed these features to identify signs of stress, pest infestation, or nutrient deficiencies in crops.

                A web-based platform was developed to present the analyzed data to farmers. This platform included visualization tools for easy interpretation of the data and integrated decision-support systems to advise on potential interventions.

                The of the drone-based monitoring system resulted in the successful collection and analysis of crop and field data across multiple pilot sites. The system demonstrated significant potential in detecting early signs of crop stress, improving water management, and optimizing fertilizer use. Farmers using the platform reported greater control over their agricultural practices and observed notable improvements in crop yields and resource efficiency.

                Initial challenges included the integration of drone data with the analytical platform and ensuring the reliability of data under varying weather conditions. These were overcome through the development of robust data processing pipelines and the use of drones capable of operating in diverse environmental conditions.

                Encouraging farmers to adopt this new technology presented another challenge. This was addressed by conducting workshops, providing hands-on demonstrations, and showcasing tangible benefits through case studies of early adopters.

                Scaling the system to cover larger areas and more diverse crop types required enhancements in data processing capabilities and drone fleet management. Solutions included cloud-based data storage and processing, as well as additional drones with varied sensing technologies.

                - **Enhanced Analytical Models:** Implementing AI and machine learning models to improve the accuracy of crop health assessments and yield predictions.
                - **Integration with Other Technologies:** Combining drone data with ground sensor data and satellite imagery for a more comprehensive monitoring system.
                - **Expansion to New Markets:** Extending the service to more regions and crop types, adapting the technology to meet the specific needs of different agricultural sectors.
                - **Sustainability Metrics:** Developing indicators for measuring the sustainability of farming practices based on drone data, supporting global efforts towards sustainable agriculture.

                The Drone-based Crop Monitoring project has established a foundation for transforming agricultural practices through advanced technology. By providing detailed, actionable insights into crop health and environmental conditions, the project empowers farmers to make more informed decisions, leading to increased productivity and sustainability. As the project evolves, it will continue to adapt and expand, offering new tools and insights to support the agriculture industry's future needs.
                """
                f"""
                example 3:

                The Smart Fertigation System project was conceived to revolutionize the way fertilization and irrigation are managed in agriculture. By incorporating Internet of Things (IoT) technology and data analytics, this system provides precision in the delivery of water and nutrients directly to crop roots, optimizing resource use and enhancing crop yields. This report encapsulates the project's goals, methodology, achievements, encountered challenges, and prospective future developments.

                The project aimed to develop a smart fertigation system capable of adjusting water and nutrient delivery in real-time based on the specific needs of crops. Objectives included:
                - Designing and deploying a network of soil and environmental sensors to monitor field conditions accurately.
                - Developing a data-driven decision-making platform for precise fertigation.
                - Creating an intuitive interface for farmers to monitor their crops and manage fertigation schedules efficiently.

                A comprehensive array of soil moisture, nutrient level, and climate condition sensors was installed across various agricultural fields to collect real-time data. This setup was intended to capture a detailed picture of the crop environment.

                The collected data were processed through a centralized platform that utilized advanced algorithms to analyze conditions and determine optimal fertigation schedules. This system considered factors such as crop type, growth stage, and local weather patterns.

                The decision-making logic was integrated with fertigation hardware, allowing automated adjustments to irrigation and fertilization practices. A user-friendly dashboard was developed for farmers, providing them with insights, alerts, and manual controls over the fertigation process.

                The implementation of the Smart Fertigation System demonstrated significant improvements in water and nutrient use efficiency across pilot sites. Farmers reported an increase in crop yield and quality while noting substantial reductions in water usage and fertilizer costs. The system's predictive capabilities also allowed for proactive management of field conditions, reducing the risk of over- or under-fertilization.

                Initial challenges included ensuring the reliability of sensor data and integrating various hardware components. These issues were addressed through rigorous testing, selection of high-quality sensors, and development of robust software for hardware integration.

                Promoting the adoption of the system among farmers required overcoming skepticism and unfamiliarity with the technology. Solution strategies included conducting on-site demonstrations, offering initial setup support, and providing comprehensive training materials.

                Ensuring the security and privacy of the collected agricultural data was paramount. The project team implemented advanced encryption methods and secure data storage solutions, along with clear data governance policies.

                - **Advanced Analytics Enhancement:** Incorporating machine learning models to further refine fertigation recommendations based on historical data and predictive analytics.
                - **Expansion to Additional Crops:** Tailoring the system for a wider variety of crops by incorporating specific crop models and nutrient requirements.
                - **Integration with Broader Farm Management Systems:** Creating interoperability with other agricultural technology systems, such as crop health monitoring and pest management tools, for a holistic approach to farm management.
                - **Sustainability Impact Tracking:** Developing features to monitor and report on the environmental impact of fertigation practices, aiding farmers in achieving sustainability goals.

                The Smart Fertigation System project marks a significant advancement in agricultural technology, offering a practical solution for the precise management of water and nutrients. The project not only achieves enhanced crop yields and resource conservation but also sets the stage for future innovations in sustainable farming practices. Moving forward, the project will continue to evolve, addressing new agricultural challenges and expanding its benefits to a broader farming community.
                """
                f"You are an Educator with real-world knowledge in {engineering_stream}. "
                f"Given a student's career choice as {career_choice} and interest in {domain_sector}. "
                f"provide me a final report of the project {question} with the most recent trends and context: {context} using the above 3 examples as a reference on how to output the final report, "
                f"remember to include a title for the project {question} exactly like in the three examples, "
                f"remember to include an executive summary of the project {question} exactly like in the three examples, "
                f"remember to include the project objectives of the project {question} exactly like in the three examples, "
                f"remember to include methodology of the project {question} exactly like in the three examples, "
                f"remember to include the results of the project {question} exactly like in the three examples, "
                f"remember to include the challenges and solutions of the project {question} exactly like in the three examples, "
                f"remember to include the future directions of the project {question} exactly like in the three examples, "
                f"remember to include a conclusion on the project {question} exactly like in the three examples.",
            ),
            ("human", "{user_input}"),
        ]
    )

    formatted_messages = chat_template.format_messages(
        engineering_stream=engineering_stream,
        career_choice=career_choice,
        domain_sector=domain_sector,
        user_input=question,
        context=context,
    )

    response = llm.invoke(formatted_messages)
    return response

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyDPow8LG1uOOHG5kj8a2axfdbJ4qTxZxbs"))

llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro", convert_system_message_to_human=True
)

st.header("Project Recommendation Engine")
st.write(
    "Discover personalized project opportunities tailored to your engineering stream and career goals. Explore a range of projects, from simple to complex, to enrich your learning experience and prepare for your future career."
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

fixed_question_pro = "help the student by listing 15 projects specific to the {engineering_stream} that would be relevant in the current Indian market scenario."


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

st.write("---")

context_pro = ""


user_flow_choice = st.selectbox(
    "User Flow Choice:",
    ["Generate complex projects", "Generate simple projects"],
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


if user_flow_choice == "Generate complex projects" or user_flow_choice == "Generate simple projects":
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

    # prompt_project_title =  f""" {engineering_stream} , {domain_sector}, {career_choice} """
    
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
        
        # docs = retriever.retrieve(prompt_project_title)
        # context_pro = " ".join(docs)

        if user_flow_choice == "Generate complex projects":
            context_pro = "use your extensive knowlegde on india"
            response_pro = get_gemini_response(
                fixed_question_pro, context_pro, engineering_stream, career_choice, domain_sector
            )
        else:
            context_pro = "use your extensive knowlegde on india"
            response_pro = get_gemini_response_x(
                fixed_question_pro, context_pro, engineering_stream, career_choice, domain_sector
            )
            
        x = response_pro.content
        x = x.replace("*", "")
        headings = re.findall(r"\d+\.\s(.+?):", x)
        applications = []
        for heading in headings:
            heading = heading.replace("*", "")
            applications.append(heading.strip())
 

        st.session_state.job_profile_content = response_pro.content
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
        st.subheader("Choose a job designation which interests you:")
        st.session_state.selected_subdomain = st.selectbox(
            "Select a Job:",
            st.session_state.applications,
            key="selected_sub",
        )
        st.session_state.subdomain_selected = True

    if st.session_state.subdomain_selected:
        if st.button("Generate Project Overview"):

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

            if user_flow_choice == "Generate complex projects": 
                # prompt_project_overview = f""" {st.session_state.selected_application}, {engineering_stream} , {domain_sector}, {career_choice} """

                # docs = retriever.retrieve(prompt_project_overview)
                # context_pro = " ".join(docs)
                response_coursess = get_gemini_respone_overview(
                    st.session_state.selected_subdomain,
                    context_pro,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                )
                response_roadmap = get_gemini_response_roadmap(
                    st.session_state.selected_subdomain, context_pro, domain_sector
                )
                response_marketing = get_gemini_respone_final_report(
                                    st.session_state.selected_subdomain,
                                    context_pro,
                                    engineering_stream,
                                    career_choice,
                                    domain_sector,
                )
            else:
                # prompt_project_overview = f""" {st.session_state.selected_application}, {engineering_stream} , {domain_sector}, {career_choice} """

                # docs = retriever.retrieve(prompt_project_overview)
                # context_pro = " ".join(docs)
                response_coursess = get_gemini_respone_overview_x(
                    st.session_state.selected_subdomain,
                    context_pro,
                    engineering_stream,
                    career_choice,
                    domain_sector,
                )
                response_roadmap = get_gemini_response_roadmap_x(
                    st.session_state.selected_subdomain, context_pro, domain_sector
                )
                response_marketing = get_gemini_respone_final_report_x(
                                    st.session_state.selected_subdomain,
                                    context_pro,
                                    engineering_stream,
                                    career_choice,
                                    domain_sector,
                )
            


            # st.session_state.success = response_success.content
            st.session_state.roadmap = response_roadmap.content
            st.session_state.marketing = response_marketing.content
            # st.session_state.strategy = response_strategies.content
            # st.session_state.data_insights = response_data.content
            st.session_state.courses_list = response_coursess.content
            st.session_state.courses_list_shown = True

    if st.session_state.courses_list:
        st.write("---")
        st.subheader("Overview")
        st.write(st.session_state.courses_list)
        st.write("---")
        st.subheader("Roadmap")
        st.write(st.session_state.roadmap)
        st.write("---")
        st.subheader("Final Report")
        st.write(st.session_state.marketing)
        st.write("---")

        if st.button("Save Generated Text"):
            email = st.session_state.email
            bruh(email, "Project Engine", user_flow_choice, career_choice)




