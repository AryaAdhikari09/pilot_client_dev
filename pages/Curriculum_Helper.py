import streamlit as st
import PyPDF2
import random
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from MCQ import get_all_topics_from_pdf, get_questions_from_topics_custom, weak_topics_from_answers, get_overview_of_topic_using_interest, just_get_text_from_pdf
import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.set_page_config(page_title="Curriculum Helper", page_icon=":books:")

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

def main():

    

    if "topics_extracted" not in st.session_state:
        st.title("Curriculum - Helper")

        pdf_file = st.file_uploader("Upload a pdf of your syllabus", type=["pdf"])

        given_pdf_content = st.file_uploader("Upload content", type=["pdf"])

        student_interest = st.text_input("Enter your interest", placeholder="Football")

        if given_pdf_content:
            if "retriever" not in st.session_state:
                # Define the FAISSRetriever class
                class FAISSRetriever:
                    def __init__(self, index, model, doc_texts):
                        self.index = index
                        self.model = model
                        self.doc_texts = doc_texts

                    def retrieve(self, query, top_k=1):
                        query_embedding = self.model.encode([query], convert_to_tensor=True)
                        query_embedding_cpu = query_embedding.cpu().numpy().astype(np.float16)
                        distances, indices = self.index.search(query_embedding_cpu, top_k)
                        return [self.doc_texts[i] for i in indices[0]]


                given_pdf_file_path = given_pdf_content.name
                with open(given_pdf_file_path, "wb") as f:
                    f.write(given_pdf_content.getbuffer())

                all_text = just_get_text_from_pdf(given_pdf_file_path)

                # print(all_text)
                # st.write(all_text)

                # Example: Split into chunks of 1000 characters
                chunk_size = 2000
                chunks = [all_text[i:i+chunk_size] for i in range(0, len(all_text), chunk_size)]

                # print(chunks)
                # st.write(chunks)

                model = SentenceTransformer("all-MPNet-base-v2")

                embeddings = model.encode(chunks, convert_to_tensor=True, batch_size=8)

                embeddings_cpu = embeddings.cpu().numpy().astype(np.float16)
                embedding_matrix = np.array(embeddings_cpu)

                index = faiss.IndexFlatL2(embedding_matrix.shape[1])
                if faiss.get_num_gpus() > 0:
                    res = faiss.StandardGpuResources()
                    index = faiss.index_cpu_to_gpu(res, 0, index)

                index.add(embedding_matrix)

                # Store the retriever in session state if not already present
                st.session_state.retriever = FAISSRetriever(index, model, chunks)

        if st.button("Explain everything 🚀"):
            if pdf_file and student_interest:
                pdf_file_path = pdf_file.name
                with open(pdf_file_path, "wb") as f:
                    f.write(pdf_file.getbuffer())

                topics = get_all_topics_from_pdf(pdf_file_path)

                while topics.content == '':
                    topics = get_all_topics_from_pdf(pdf_file_path)


                st.session_state["topics_extracted"] = topics
                st.session_state["student_interest"] = student_interest

                st.rerun()

    else:
        st.title("Explanation:")

        # attempted_questions = st.session_state["attempted_questions"]
        topics = st.session_state["topics_extracted"]
        student_interest = st.session_state["student_interest"]


        actual_topics = eval(topics.content)

        prompt_for_rag_first = """"""

        for i in range (len(actual_topics)):
            prompt_for_rag_first += f"{actual_topics[i]}," 

        retriever = st.session_state.retriever

        docs_first = retriever.retrieve(prompt_for_rag_first)
        topics_context = " ".join(docs_first)

        content_to_be_printed = []

        k=0
        for i in actual_topics:
            topic_overview = get_overview_of_topic_using_interest(i, student_interest, topics_context)
            content_to_be_printed.append(topic_overview.content)
            k+=1
            if (k==10):
                break
            
        # actual_topics = eval(topics.content)
        j=0
        for i in actual_topics:
            st.write("---")
            st.header(f"{i}")
            st.write(content_to_be_printed[j])
            # topic_overview = get_overview_of_topic_using_interest(i, student_interest, topics_context)
            # st.write(topic_overview.content)
            st.write("---")
            j+=1
            if (j==10):
                break


        del st.session_state["topics_extracted"]
        del st.session_state["student_interest"]

        if st.button("Back to Home"):
            st.session_state.clear()
            st.experimental_rerun()
if __name__ == "__main__":
    main()