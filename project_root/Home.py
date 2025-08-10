import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Automation Suite - Siddharth Singh", layout="wide")

# Title and Banner with photo at top right
col_title, col_photo = st.columns([4, 1])

with col_title:
    st.title("Automation & Cloud Suite")
    st.markdown(
        """
        Welcome to my integrated automation suite that combines AWS, Docker, Kubernetes, ML, Linux,
        Python,Blogs,System,Git_and_Github ,and more — 
        designed to streamline your cloud and development workflows.
        """
    )

with col_photo:
    try:
        # Load your photo sidd.jpeg from assets folder
        img = Image.open("assets/sidd.jpeg")
        st.image(img, width=120, caption="Siddharth Singh")
    except Exception:
        st.warning("Photo sidd.jpeg not found in assets folder.")

# About Me Section
st.markdown("---")
st.header("About Me")

# You can keep the favicon or remove if photo above suffices
profile_image_url = "https://siddsingh.mystrikingly.com/favicon.ico"  # fallback image
try:
    response = requests.get(profile_image_url)
    img_favicon = Image.open(BytesIO(response.content))
    st.image(img_favicon, width=150)
except Exception:
    pass

st.markdown(
    """
    **Siddharth Singh** — Aspiring Cyber Security Professional, Computer Science Engineering student passionate about Digital Asset Protection.  
    Skilled in cloud automation, containerization, AI/ML-driven solutions, and Linux systems with hands-on experience in AWS, Docker, Kubernetes, and Python scripting.

    I strive to build efficient, scalable, and secure automation tools to empower businesses in the digital era.
    """
)

# Contact Me Section with icons
st.markdown("---")
st.header("Contact Me")

st.markdown(
    """
    Feel free to connect on any of these platforms or visit my personal website:
    """
)

# Define social links with emojis as icons
contacts = {
    "LinkedIn": ("🔗", "https://www.linkedin.com/in/siddharth-singh-7a2b7a240/"),
    "Instagram": ("📸", "https://www.instagram.com/sidd___009_/?next=%25"),
    "Facebook": ("📘", "https://www.facebook.com/profile.php?id=100089825111015"),
    "Twitter (X)": ("🐦", "https://x.com/Sidd935"),
    "GitHub": ("🐙", "https://github.com/sidd2005singh"),
    "Personal Website": ("🌐", "https://siddsingh.mystrikingly.com/")
}

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"[{contacts['LinkedIn'][0]} LinkedIn]({contacts['LinkedIn'][1]})")
    st.markdown(f"[{contacts['Instagram'][0]} Instagram]({contacts['Instagram'][1]})")

with col2:
    st.markdown(f"[{contacts['Facebook'][0]} Facebook]({contacts['Facebook'][1]})")
    st.markdown(f"[{contacts['Twitter (X)'][0]} Twitter (X)]({contacts['Twitter (X)'][1]})")

with col3:
    st.markdown(f"[{contacts['GitHub'][0]} GitHub]({contacts['GitHub'][1]})")
    st.markdown(f"[{contacts['Personal Website'][0]} Website]({contacts['Personal Website'][1]})")

st.markdown(
    """
    ---
    *Thank you for visiting! My automation platform is tailored to bring cloud and Python power right to your fingertips.*
    """
)
