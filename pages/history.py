import streamlit as st
import pandas as pd
import requests
# from navigation import make_sidebar
# from navigation import make_sidebar
from datetime import datetime

# st.set_page_config(page_title="Flexible Table", page_icon=":books:")
import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.set_page_config(page_title="Course Engine", page_icon=":smile:")

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
    if st.button("Login",key="sdfsdfsdfsdfsdggfth"):
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



def linemaker(broh):
    # Ensure the text is in normal case but capitalize the first letter
    if len(broh) > 0:
        normal_text = (
            broh[0].upper() + broh[1:].lower()
        )  # Capitalize first letter, rest in lowercase
    else:
        normal_text = broh

    # Limit the text length
    if len(normal_text) > 15:
        display_text = normal_text[:15] + "......"
    else:
        display_text = normal_text

    # Reduce text size using Markdown
    reduced_size_text = f"<small>{display_text}</small>"

    return reduced_size_text


def project_getter(module_content):
    # Get the values of all content keys
    engineering_stream = module_content.get("engineering_stream", "Content not found")
    domain_sector = module_content.get("domain_sector", "Content not found")
    career_choice = module_content.get("career_choice", "Content not found")
    selected_application = module_content.get(
        "selected_application", "Content not found"
    )
    user_flow_choice = module_content.get("user_flow_choice", "Content not found")
    projects_content = module_content.get("projects_content", "Content not found")
    overview_content = module_content.get("overview_content", "Content not found")
    roadmap_content = module_content.get("roadmap_content", "Content not found")
    final_report_content = module_content.get(
        "final_report_content", "Content not found"
    )

    # Combine all content
    # all_data = "You chose to: "+user_flow_choice+"\n\n"+engineering_stream+"\n\n"+domain_sector+"\n\n"+career_choice+"\n\n"+"aalu"+"\n\n"+projects_content +"\n\n"+"You chose this project: "+selected_application+"\n\n"+ overview_content +"\n\n"+ roadmap_content +"\n\n"+ final_report_content
    all_data = (
        "\n\n---\n\n"
        "##### Your choice is: " + user_flow_choice + "\n\n"
        "\n\n---\n\n"
        + "##### Engineering Stream: "
        + engineering_stream
        + "\n\n"
        + "##### Domain Sector: "
        + domain_sector
        + "\n\n"
        + "##### Career Choice: "
        + career_choice
        + "\n\n"
        "\n\n---\n\n"
        "### 15 projects for hands-on experience: " + "\n\n" + projects_content + "\n\n"
        "\n\n---\n\n"
        "##### You chose this project: " + selected_application + "\n\n"
        "\n\n---\n\n"
        "### Project Overview: " + "\n\n" + overview_content + "\n\n"
        "\n\n---\n\n"
        "### Project Roadmap: " + "\n\n" + roadmap_content + "\n\n"
        "\n\n---\n\n"
        "### Project Final Report   : " + "\n\n" + final_report_content + "\n\n---\n\n"
    )

    return all_data


def course_getter(module_content):
    # Get the values of all content keys
    user_flow_choice = module_content.get("user_flow_choice", "Content not found")
    Stream = module_content.get("Stream")
    Sector = module_content.get("Sector", "Content not found")
    Career = module_content.get("Career", "Content not found")
    Selected_job = module_content.get("Selected_job", "Content not found")
    job_designation = module_content.get("job_designation", "\n")
    job_profile_content = module_content.get("job_profile_content", "\n")
    courses_list = module_content.get("courses_list", "Content not found")
    course_outline_content = module_content.get(
        "course_outline_content", "Content not found"
    )
    youtube = module_content.get("youtube", [])
    google = module_content.get("google", [])

    youtube_data = ""
    for item in youtube:
        title = item.get("title", "No title")
        link = item.get("link", "#")
        youtube_data += f"- [{title}]({link})\n"

    # Convert Google data to string with hyperlinks
    google_data = ""
    for item in google:
        title = item.get("title", "No title")
        link = item.get("link", "#")
        google_data += f"- [{title}]({link})\n"

    if Stream:
        all_data = (
            "---\n\n"
            "##### You chose to : " + user_flow_choice + "\n\n"
            "---\n\n"
            "##### Selected Stream: " + Stream + "\n\n"
            "##### Selected Domain: " + Sector + "\n\n"
            "##### Selected Career Choice: " + Career + "\n\n"
            "---\n\n"
            "### Here are 15 Job Profiles for you:\n\n"
            + job_designation
            + "\n\n"
            + job_profile_content
            + "\n"
            "---\n\n"
            "##### Selected Job: " + Selected_job + "\n\n"
            "---\n\n"
            "### Here are 15 Courses Necessary for the Job:\n\n" + courses_list + "\n"
            "---\n\n"
            "### Course Outline:\n\n" + course_outline_content + "\n"
            "---\n\n"
            "### Here are some additional links that might help you:\n\n"
            + youtube_data
            + google_data
            + "---\n\n"
        )

    else:
        all_data = (
            "---\n\n"
            "##### You chose to : " + user_flow_choice + "\n\n"
            "---\n\n"
            "##### Job Designation: " + job_designation + "\n\n"
            "---\n\n" + job_profile_content + "\n\n"
            "### Courses List\n\n" + courses_list + "\n\n"
            "---\n\n"
            "### Course Outline\n\n" + course_outline_content + "\n\n"
            "---\n\n"
            "### Here are some additional links that might help you:\n\n"
            + youtube_data
            + google_data
            + "---\n\n"
        )

    return all_data


def research_getter(module_content):
    user_flow_choice = module_content.get("user_flow_choice")
    career_choice = module_content.get("career_choice", "Content not found")

    if user_flow_choice == "Generate Ideas":
        engineering_stream = module_content.get("Stream", "Content not found")
        domain_sector = module_content.get("Sector", "Content not found")
        job_profile_content = module_content.get(
            "job_profile_content", "Content not found"
        )
        courses_list = module_content.get("courses_list", "Content not found")

        if career_choice == "Entrepreneurship":
            data_insights = module_content.get("data_insights", "Content not found")
            strategy = module_content.get("strategy", "Content not found")
            marketing = module_content.get("marketing", "Content not found")
            roadmap = module_content.get("roadmap", "Content not found")
            success = module_content.get("success", "Content not found")
            # all_data = "\n\n---\n\n"+"You chose to: "+user_flow_choice+"\n\n---\n\n"+"\n\n"+"Career Choice: "+career_choice+"\n\n"+"Engineering Stream: "+engineering_stream+"\n\n"+"Domain Sector: "+domain_sector +"\n\n---\n\n"+"\n\n"+"Here are 15 Subdomains for you:"+"\n\n"+job_profile_content+"\n\n"+courses_list+"\n\n"+ data_insights +"\n\n"+ strategy +"\n\n"+ marketing+"\n\n"+roadmap+"\n\n"+success
            all_data = (
                "\n\n---\n\n"
                "##### You chose to: " + user_flow_choice + "\n\n"
                "---\n\n"
                "\n\n"
                "##### Engineering Stream: " + engineering_stream + "\n\n"
                "##### Domain Sector: " + domain_sector + "\n\n"
                "##### Career Choice: " + career_choice + "\n\n"
                "---\n\n"
                "\n\n"
                "### Here are 15 Subdomains for you:\n\n" + job_profile_content + "\n\n"
                "\n\n---\n\n"
                "### Target audience Analysis:\n\n" + courses_list + "\n\n"
                "\n\n---\n\n"
                "### Data Insights:\n\n" + data_insights + "\n\n"
                "\n\n---\n\n"
                "### Strategies to Address Pain Points:\n\n" + strategy + "\n\n"
                "\n\n---\n\n"
                "### Marketing and Engagement Strategies:\n\n" + marketing + "\n\n"
                "\n\n---\n\n"
                "### Roadmap:\n\n" + roadmap + "\n\n"
                "\n\n---\n\n"
                "### Success Factors and Metrics:\n\n" + success + "\n\n---\n\n"
            )

        elif career_choice == "Placements":
            job_titles = module_content.get("job_titles", "Content not found")
            industry = module_content.get("industry", "Content not found")
            roadmap_attributes = module_content.get(
                "roadmap_attributes", "Content not found"
            )
            all_data = (
                "\n\n---\n\n"
                "##### You chose to: " + user_flow_choice + "\n\n"
                "\n\n---\n\n"
                "##### Engineering Stream: " + engineering_stream + "\n\n"
                "##### Domain Sector: " + domain_sector + "\n\n"
                "##### Career Choice: " + career_choice + "\n\n"
                "\n\n---\n\n"
                "### Here are 15 Subdomains for you:\n\n" + job_profile_content + "\n\n"
                "\n\n---\n\n"
                "### Higher Education Program Attributes:\n\n" + courses_list + "\n\n"
                "\n\n---\n\n"
                "### Market and Economic Attributes:\n\n" + job_titles + "\n\n"
                "\n\n---\n\n"
                "### Academic Skills and Knowledge Attributes:\n\n" + industry + "\n\n"
                "\n\n---\n\n"
                "### Roadmap Attributes:\n\n" + roadmap_attributes + "\n\n---\n\n"
            )
        else:
            job_titles = module_content.get("job_titles", "Content not found")
            market = module_content.get("market", "Content not found")
            academic = module_content.get("academic", "Content not found")
            roadmap_attributes = module_content.get(
                "roadmap_attributes", "Content not found"
            )
            success = module_content.get("success", "Content not found")
            all_data = (
                "\n\n---\n\n"
                "##### You chose to: " + user_flow_choice + "\n\n"
                "\n\n---\n\n"
                "##### Engineering Stream: " + engineering_stream + "\n\n"
                "##### Domain Sector: " + domain_sector + "\n\n"
                "##### Career Choice: " + career_choice + "\n\n"
                "\n\n---\n\n"
                "### Here are 15 Subdomains for you:\n\n" + job_profile_content + "\n\n"
                "\n\n---\n\n"
                "### Higher Education Program Attributes:\n\n" + courses_list + "\n\n"
                "\n\n---\n\n"
                "### Market and Economic Attributes:\n\n" + market + "\n\n"
                "\n\n---\n\n"
                "### Academic Skills and Knowledge Attributes:\n\n" + academic + "\n\n"
                "\n\n---\n\n"
                "### Roadmap Attributes:\n\n" + roadmap_attributes + "\n\n---\n\n"
                "### Success Factors and Metrics:\n\n" + success + "\n\n---\n\n"
            )

    else:
        subdomain = module_content.get("subdomain", "Content not found")
        courses_list = module_content.get("courses_list", "Content not found")
        if career_choice == "Entrepreneurship":
            job_designation = module_content.get("job_designation", "Content not found")
            goals = module_content.get("goals", "Content not found")
            data_insights = module_content.get("data_insights", "Content not found")
            strategy = module_content.get("strategy", "Content not found")
            marketing = module_content.get("marketing", "Content not found")
            roadmap = module_content.get("roadmap", "Content not found")
            success = module_content.get("success", "Content not found")
            # all_data = "You chose to: "+user_flow_choice+"\n\n"+career_choice+"\n\n"+job_designation +"\n\n"+goals+"\n\n"+subdomain+"\n\n"+ courses_list +"\n\n"+ data_insights +"\n\n"+ strategy+"\n\n"+marketing+"\n\n"+roadmap+"\n\n"+success
            all_data = (
                "\n\n---\n\n"
                "##### You chose to: " + user_flow_choice + "\n\n" + "\n\n---\n\n"
                "##### Career Choice: " + career_choice + "\n\n" + "\n\n---\n\n"
                "##### Enter Business Idea: " + job_designation + "\n\n"
                # +"\n\n---\n\n"
                "##### Enter your goals: " + goals + "\n\n"
                # +"\n\n---\n\n"
                # +"\n\n---\n\n"
                "##### Enter the subdomain: " + subdomain + "\n\n" + "\n\n---\n\n"
                "### Target audience Analysis:\n\n"
                + courses_list
                + "\n\n"
                + "\n\n---\n\n"
                "### Data Insights:\n\n" + data_insights + "\n\n" + "\n\n---\n\n"
                "### Strategies to Address Pain Points:\n\n"
                + strategy
                + "\n\n"
                + "\n\n---\n\n"
                "### Marketing and Engagement Strategies:\n\n"
                + marketing
                + "\n\n"
                + "\n\n---\n\n"
                "### Roadmap:\n\n" + roadmap + "\n\n" + "\n\n---\n\n"
                "### Success Factors and Metrics:\n\n" + success + "\n\n---\n\n"
            )

        elif career_choice == "Higher Studies":
            degree_and_field_of_study = module_content.get(
                "degree_and_field_of_study", "Content not found"
            )
            preferred_location = module_content.get(
                "preferred_location", "Content not found"
            )
            budget = module_content.get("budget", "Content not found")
            academic = module_content.get("academic", "Content not found")
            roadmap_attributes = module_content.get(
                "roadmap_attributes", "Content not found"
            )
            success = module_content.get("success", "Content not found")
            # all_data = "You chose to: "+user_flow_choice+"\n\n"+career_choice+"\n\n"+degree_and_field_of_study +"\n\n"+subdomain+"\n\n"+preferred_location+"\n\n"+ budget +"\n\n"+ courses_list +"\n\n"+ academic +"\n\n"+ roadmap_attributes +"\n\n"+success
            all_data = (
                "\n\n---\n\n"
                "##### You chose to: " + user_flow_choice + "\n\n"
                "\n\n---\n\n"
                "##### Career Choice: " + career_choice + "\n\n"
                "\n\n---\n\n"
                "##### Engineering Stream: " + degree_and_field_of_study + "\n\n"
                "##### Enter Subdomain: " + subdomain + "\n\n"
                "##### Enter your Desired Industry: " + preferred_location + "\n\n"
                "##### Enter your Career Goals: " + budget + "\n\n"
                "\n\n---\n\n"
                "### Higher Education Program Attributes:\n\n" + courses_list + "\n\n"
                "\n\n---\n\n"
                "### Market and Economic Attributes:\n\n" + academic + "\n\n"
                "\n\n---\n\n"
                "### Academic Skills and Knowledge Attributes:\n\n"
                + roadmap_attributes
                + "\n\n"
                "\n\n---\n\n"
                "### Success Factors and Metrics:\n\n" + success + "\n\n---\n\n"
            )
        else:  # placements
            degree_and_field_of_study = module_content.get(
                "degree_and_field_of_study", "Content not found"
            )
            desired_industry = module_content.get(
                "desired_industry", "Content not found"
            )
            career_goals = module_content.get("career_goals", "Content not found")
            roadmap_attributes = module_content.get(
                "roadmap_attributes", "Content not found"
            )
            job_titles = module_content.get("job_titles", "Content not found")
            industry = module_content.get("industry", "Content not found")
            all_data = (
                "\n\n---\n\n"
                "##### You chose to: " + user_flow_choice + "\n\n"
                "\n\n---\n\n"
                "##### Career Choice: " + career_choice + "\n\n"
                "\n\n---\n\n"
                "##### Engineering Stream: " + degree_and_field_of_study + "\n\n"
                "##### Enter Subdomain: " + subdomain + "\n\n"
                "##### Enter your Desired Industry: " + desired_industry + "\n\n"
                "##### Enter your Career Goals: " + career_goals + "\n\n"
                "\n\n---\n\n"
                "### Industry Requirements:\n\n" + courses_list + "\n\n"
                "\n\n---\n\n"
                "### Job Roles and Descriptions:\n\n" + job_titles + "\n\n"
                "\n\n---\n\n"
                "### Industry Trends and Outlook:\n\n" + industry + "\n\n"
                "\n\n---\n\n"
                "### Roadmap Attributes:\n\n" + roadmap_attributes + "\n\n---\n\n"
            )

    return all_data


def bruh():
    BASE_URL = "https://pilot-server-12yj.vercel.app"

    # Ensure the user is logged in and the token is available
    if "token" not in st.session_state:
        st.error("No token available. Please log in first.")
        return

    token = st.session_state.token
    try:
        # Fetch user data from API
        response = requests.get(
            f"{BASE_URL}/getuserData", headers={"Authorization": token}
        )

        if response.status_code == 200:
            user_data = response.json()
            st.success("User data fetched successfully!")

            # Initialize DataFrame
            df = pd.DataFrame(columns=["Date & Time", "Module", " "])
            all_modules_data = []

            if user_data:
                rows = []
                for i in range(len(user_data)):
                    element = user_data[i]  # Get the first dictionary in the list

                    # Access the first key of the first dictionary
                    module_content = list(element.keys())[
                        1
                    ]  # Get the first key (e.g., "Module 1")

                    date_time_element = list(element.keys())[0]
                    date_and_time = element[date_time_element]
                    # st.write(date_and_time)
                    # Parse the timestamp string into a datetime object
                    dt = datetime.fromisoformat(date_and_time)

                    # Format the datetime object into the desired string format
                    formatted_date = dt.strftime("%d/%m/%Y %H:%M:%S")

                    # Access the value of the first key
                    module_key = element[module_content]
                    # st.write(user_data)

                    engine = list(element.keys())[2]
                    engine_data = element[engine]
                    # st.write(engine_data)

                    if module_key == "Project Engine":
                        # Add the row to the list for Module 1
                        rows.append(
                            {
                                "Date & Time": formatted_date,
                                "Module": module_key,
                                " ": "Click to view more",
                            }
                        )
                        all_modules_data.append(
                            (module_key, project_getter(engine_data))
                        )

                    elif module_key == "Course Engine":
                        # Add the row to the list for Module 1
                        # st.write(engine_data)
                        rows.append(
                            {
                                "Date & Time": formatted_date,
                                "Module": module_key,
                                " ": "Click to view more",
                            }
                        )
                        all_modules_data.append(
                            (module_key, course_getter(engine_data))
                        )
                    else:
                        rows.append(
                            {
                                "Date & Time": formatted_date,
                                "Module": module_key,
                                " ": "Click to view more",
                            }
                        )
                        all_modules_data.append(
                            (module_key, research_getter(engine_data))
                        )

                # Populate DataFrame
                df = pd.DataFrame(rows)

                # Display the table with proper formatting
                table_container = st.container()
                with table_container:
                    # Display the column headers
                    col1, col2, col3, col4 = st.columns([3, 3, 7, 2])
                    with col1:
                        st.write("Date & Time")
                    with col2:
                        st.write("Module")
                    with col3:
                        st.write(" ")
                    with col4:
                        st.write("")  # Empty column for buttons

                    for index, row in df.iterrows():
                        col1, col2, col3, col4 = st.columns([3, 3, 7, 2])
                        with col1:
                            st.write(row["Date & Time"])
                        with col2:
                            st.write(row["Module"])
                        with col3:
                            st.markdown(row[" "], unsafe_allow_html=True)
                        with col4:
                            if st.button("View More", key=index):
                                st.session_state.selected_module = index

                # Display the full content below the table in an expander
                if "selected_module" in st.session_state:
                    selected_index = st.session_state.selected_module
                    with st.expander(
                        f"Full Content for {df.iloc[selected_index]['Module']}",
                        expanded=True,
                    ):
                        st.markdown(
                            all_modules_data[selected_index][1], unsafe_allow_html=True
                        )

            else:
                error_message = response.json().get(
                    "message", "Failed to fetch user data."
                )
                st.error(error_message)
        else:
            st.error("Failed to fetch user data. Please try again.")
    # except:
    #     st.subheader("No data saved.")
    except Exception as e:
        # st.error(f"An error occurred: {str(e)}")
        st.error(f"No data saved yet.")



# Calling the function to display user data
bruh()
