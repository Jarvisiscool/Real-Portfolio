from pathlib import Path

import streamlit as st 
from PIL import Image

# ----Path Settings-----
current_dic = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dic/ "styles" / "main.css"
resume_file = current_dic/ "assets" / "Resume.pdf"
profile_pic = current_dic / "assets"/ "profile-pic.png"

# ----General Settings----
PAGE_TITLE = "Digital CV | Naveen Indraj"
PAGE_ICON = ":wave:"
NAME = "Naveen Indraj"
DESCRIPTION = """ Aspiring Computer Scientist, wanting to dive into the field of AI and Data Engineering"""

EMAIL = "indnav33@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com"
}

PROJECTS = {
    "- 🏆 CHATCLONE - Creating a Streamlit website that is you can converse with like CHATGPT",
    "- 🏆 PDF READER - Uses LangChain, ChatGPT, and Pinecone Vector Database to create a website allows you to upload a pdf and ask a specialized chatbot questions about the pdf",
    "- 🏆 UNIVERSAL AI AGENT - A universal web scrapper that can be modified; can scrape websites and gives markdown, JSON, and a google sheets format of the scraped data",
    "- 🏆 GOOGLE SHEET READER - Streamlit website that allows users to type in specific fileds that will then generate a google sheet with all the fields"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ----Load CSS, PDF, and PROFIL PIC----
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---Hero Scetion---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= ":file_folder: Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# ----Social Links----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#----Experience and Qualifications----
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """ 
    - ✅Introduction to Python Programming - Completed a course on the fundamentals of Python programming and understanding when and where to implement this tool.
    - ✅Python Programming Essentials - Completed a course on Python programming and learned how to debug code and learned how to complete a project in Python
    - ✅Programming for Everybody (Getting Started with Python) - Completed a course on Python programming that helped with practicing Python essential skills for real-world coding applications.
    - ✅Creative Interactive Dashboard with Streamlit and Python - Completed a course on the use of Python in the creation of a Streamlit Dashboard that uses a query to render the data onto the dashboard.
    - ✅ChatGPT and LangChain: The Complete Developer's Masterclass Completed a course on LangChain and ChatGPT and created a fully functioning website that allows you to upload a pdf and ask a specialized ChatBot questions about the pdf like a specialized ChatGPT. 
    """
)


#----Skills----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """ 
    - 👨‍💻Programming: Python (Streamlit, Pandas), SQL, Java
    - 📊Data Visualization: Microsoft Office, Google Sheet
    - 🎛 DataBases: Vector Databases (Pinecone & ChromaDB), MySQL
    - 🤖 AI: ChatGPT, Firecrawl, and API's
    """
)

#----Work History----
st.write("#")
st.subheader("Work History")
st.write("---")

#---Job 1
st.write("#")
st.write("⛑ Non-Profit Initiative")
st.write(
    """ 
    Part of a team of teenagers led by a teacher. Helping initiate a website that allows young adults to voice their opinions about problems worldwide.
    """
)

#---Job 2
st.write("#")
st.write("🔬 Sci-Tech Discovery Center,")
st.write(
    """ 
    Volunteer at the Sci-Tech Discovery Center, helping customers find their way and navigate the area, helping with cleaning, and monitoring kids in the playroom or party room.
    """
)

#---Job 3
st.write("##")
st.write("📚 Frisco Public Library")
st.write(
    """ 
    Volunteer at the Frisco Public Library under the VolunTEEN Corps.   
    """
)

#---Job 4
st.write("#")
st.write("🥫 North Texas Food Bank")
st.write(
    """ 
    Volunteer at the North Texas Food Bank. Helped package food and create boxes to carry food. 
    """
)

#----Projects
st.write("#")
st.subheader("Projects")
st.write("---")
for project in PROJECTS:
    st.write(f"[{project}]")