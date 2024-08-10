import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import asyncio
import aiohttp
# import faiss
import numpy as np
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

# from navigation import make_sidebar
import time
import requests

# from navigation import make_sidebar
import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.set_page_config(page_title="Home", page_icon=":smile:")


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
        # st.experimental_rerun()
        st.switch_page("login.py")


def logout():
    st.session_state.logged_in = False
    st.session_state.token = None
    st.session_state.email = ""
    st.info("Logged out successfully!")
    # st.experimental_rerun()
    st.switch_page("login.py")


make_sidebar()


# make_sidebar()


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


# # Define the FAISSRetriever class
# class FAISSRetriever:
#     def __init__(self, index, model, doc_texts):
#         self.index = index
#         self.model = model
#         self.doc_texts = doc_texts

#     def retrieve(self, query, top_k=1):
#         query_embedding = self.model.encode([query], convert_to_tensor=True)
#         query_embedding_cpu = query_embedding.cpu().numpy().astype(np.float16)
#         distances, indices = self.index.search(query_embedding_cpu, top_k)
#         return [self.doc_texts[i] for i in indices[0]]


# # Function to fetch webpages
# async def fetch_webpage(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()


# # Function to fetch all webpages
# async def fetch_all_webpages(urls):
#     tasks = [fetch_webpage(url) for url in urls]
#     return await asyncio.gather(*tasks)


# # Function to extract text from HTML
# def extract_text_from_html(html_content):
#     soup = BeautifulSoup(html_content, "html.parser")
#     paragraphs = soup.find_all("p")
#     return " ".join([para.get_text() for para in paragraphs])


# urls = [
#     "https://www.ibef.org/industry/healthcare-india",
#     "https://www.ibef.org/industry/agriculture-india",
#     "https://www.ibef.org/industry/autocomponents-india",
#     "https://www.ibef.org/industry/india-automobiles",
#     "https://www.ibef.org/industry/indian-aviation",
#     "https://www.ibef.org/industry/banking-india",
#     "https://www.ibef.org/industry/biotechnology-india",
#     "https://www.ibef.org/industry/cement-india",
#     "https://www.ibef.org/industry/chemical-industry-india",
#     "https://www.ibef.org/industry/indian-consumer-market",
#     "https://www.ibef.org/industry/defence-manufacturing",
#     "https://www.ibef.org/industry/ecommerce",
#     "https://www.ibef.org/industry/education-sector-india",
#     "https://www.ibef.org/industry/electric-vehicle",
#     "https://www.ibef.org/industry/electronics-system-design-manufacturing-esdm",
#     "https://www.ibef.org/industry/engineering-india",
#     "https://www.ibef.org/industry/financial-services-india",
#     "https://www.ibef.org/industry/fmcg",
#     "https://www.ibef.org/industry/food-processing",
#     "https://www.ibef.org/industry/infrastructure-sector-india",
#     "https://www.ibef.org/industry/insurance-sector-india",
#     "https://www.ibef.org/industry/information-technology-india",
#     "https://www.ibef.org/industry/manufacturing-sector-india",
#     "https://www.ibef.org/industry/media-entertainment-india",
#     "https://www.ibef.org/industry/medical-devices",
#     "https://www.ibef.org/industry/metals-and-mining",
#     "https://www.ibef.org/industry/msme",
#     "https://www.ibef.org/industry/oil-gas-india",
#     "https://www.ibef.org/industry/paper-packaging",
#     "https://www.ibef.org/industry/pharmaceutical-india",
#     "https://www.ibef.org/industry/ports-india-shipping",
#     "https://www.ibef.org/industry/power-sector-india",
#     "https://www.ibef.org/industry/indian-railways",
#     "https://www.ibef.org/industry/real-estate-india",
#     "https://www.ibef.org/industry/renewable-energy",
#     "https://www.ibef.org/industry/retail-india",
#     "https://www.ibef.org/industry/science-and-technology",
#     "https://www.ibef.org/industry/services",
#     "https://www.ibef.org/industry/steel",
#     "https://www.ibef.org/industry/telecommunications",
#     "https://www.ibef.org/industry/textiles",
#     "https://www.ibef.org/industry/tourism-hospitality-india",
#     "https://www.ibef.org/industry/roads-india",
# ]


# async def main():
#     html_contents = await fetch_all_webpages(urls)
#     doc_texts = [extract_text_from_html(html_content) for html_content in html_contents]
#     return doc_texts


# if "retriever" not in st.session_state:

#     doc_texts = asyncio.run(main())

#     all_text = " ".join(doc_texts)

#     model = SentenceTransformer("all-MPNet-base-v2")

#     embeddings = model.encode(doc_texts, convert_to_tensor=True, batch_size=8)

#     embeddings_cpu = embeddings.cpu().numpy().astype(np.float16)
#     embedding_matrix = np.array(embeddings_cpu)

#     index = faiss.IndexFlatL2(embedding_matrix.shape[1])
#     if faiss.get_num_gpus() > 0:
#         res = faiss.StandardGpuResources()
#         index = faiss.index_cpu_to_gpu(res, 0, index)

#     index.add(embedding_matrix)

#     # Store the retriever in session state if not already present
#     st.session_state.retriever = FAISSRetriever(index, model, doc_texts)

#     retriever = st.session_state.retriever


# Create columns for title and buttons
st.title("Daira Edtech Portal")
st.markdown("#### Empowering Engineering Futures")
st.write("---")
st.markdown("""

##### Welcome to Daira EdTech: Empowering Engineering Futures

At Daira EdTech, we are dedicated to transforming the educational landscape for engineering students. Our innovative platform bridges the gap between academia and industry, providing students with the tools they need to succeed in their careers. Through our comprehensive suite of portals, we offer personalized guidance and insights tailored to individual aspirations and academic goals.

---

#### Our Portals

##### *1. Project Recommendation System: Bridging Theory and Practice*

Our Project Recommendation System empowers engineering students by offering tailored project opportunities that align with their engineering streams, interests, and career goals. Whether you're a first-year student or nearing graduation, our platform curates projects ranging from simple to complex, ensuring a rich and engaging learning experience.

- *Streamlined Exploration:* Discover projects that match your interests and academic background.
- *Personalized Recommendations:* Get project suggestions aligned with your career aspirations.
- *Diverse Complexity:* Access projects of varying complexity to suit your skill level.
- *Career-Focused Opportunities:* Enhance your portfolio and industry readiness.

##### *2. Course Recommendation System: Empowering Career Pathways*

Our Course Recommendation System guides students in making informed educational choices, offering personalized course suggestions that align with career goals and academic backgrounds. This portal ensures students are well-prepared for the job market by aligning course content with industry standards.

- *Tailored Course Recommendations:* Find courses that match your domain and career aspirations.
- *Industry-Ready Focus:* Align your learning with current industry requirements.
- *Informed Educational Decisions:* Explore potential career trajectories with confidence.

##### *3. Research Portal: Navigating Academic and Professional Paths*

The Research Portal is a comprehensive resource designed to assist students in exploring academic and professional opportunities. From entrepreneurship insights to higher education options and industry reports, this portal provides the knowledge and tools students need to succeed.

- *Entrepreneurship Insights:* Access market reports and industry dynamics for aspiring entrepreneurs.
- *Higher Education Opportunities:* Explore advanced academic programs and funding options.
- *Industry Reports for Placements:* Stay informed about industry trends and job roles.

---

#### About Us

Daira EdTech is committed to redefining engineering education by integrating real-world applications into academic learning. Our platform equips students with the skills and knowledge necessary to thrive in today's competitive job market. By connecting students with personalized learning paths and practical experiences, we prepare future engineers to become leaders and innovators in their fields.

Explore our platform and discover how Daira EdTech can help you unlock your full potential and achieve your career aspirations.

---""")
# make_sidebar()
