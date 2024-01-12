import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Matilda Huang - UX Designer, Technology Innovator",
    page_icon="⚡️",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    profile_image = Image.open('memoji.PNG')
    st.image(profile_image)

with col2:
    st.markdown(
    """
    ## Matilda Huang
     Language Enthusiast. Tech Lover.
    """
)

st.markdown(
    """

    ## 📚 Education

    - **MS in Technology Innovation** @ University of Washington
    - **BA in English** @ National Taiwan Normal University

    &nbsp;

    ## 👩🏻‍💻 Professional Experience

    - **User Support Intern** @ PicCollage
    - **Research & Teaching Assistant** @ National Taiwan Normal University
    - **Linguistic Intern** @ Glossika
"""
)