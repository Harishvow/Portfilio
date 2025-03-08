import pandas
import streamlit as st
import pandas as df

st.set_page_config(layout="wide")
st.title("My Portfolio")
pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/EjbeWm8_d.webp?maxwidth=1520&fidelity=grand");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
background-color: rgba(0,0,0,0.20);
}}
</style>
"""
st.markdown(pg_bg_img, unsafe_allow_html=True)
col1,col2=st.columns(2)
with col1:
    st.image("images/pic.jpeg")
with col2:
   st.header("👋Hii I'm Harish")
   content="I’m Harish Chidamparam, a CSBS student passionate about web development, cybersecurity, and digital marketing. I have completed certifications in Cybersecurity Analysis and Web Development and enjoy building secure and efficient applications"
   st.info(content)
   st.subheader("Skills")
   st.header("⭐️ Python")
   st.header("⭐️ SQL")


col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df=pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:1].iterrows():
         st.header(row["title"])
         st.write(row["description"])
         st.image("images/" + row["image"])
         st.write(f"[🔗source]({row["url"]})")


with col4:
    for index,row in df[1:].iterrows():
         st.header(row["title"])
         st.write(row["description"])
         st.image("images/"+row["image"])
         st.write(f"[🔗source]({row["url"]})")
st.header("📖Education")
st.header("🎓B.Tech Computer Science-Engineering: Spec in Computer Science Business System")
st.success("""Current Year: 2nd Year\n
Year of Enrollment: 2023\n
Expected Year of Graduation: 2027
        """)
col5,col6=st.columns(2)
with col5:
    st.header("🏏hobbies")
    st.info("music")
    st.info("cricket")
    st.info("coding")
    st.info("travel")
    st.info("Gaming")


with st.sidebar:
    st.link_button(label="LinkedIn",url="https://www.linkedin.com/in/harish-chidamparam-g-1389a6297/",icon="💻")
    st.link_button(label="Github",url="https://github.com/Harishvow",icon="🔗")




