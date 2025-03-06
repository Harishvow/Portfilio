import streamlit as st
from contact import send_email
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

st.header("Contact Me")
with st.form(key="email_forms"):
    user_email=st.text_input("your Email")
    msg=st.text_area("Your Message")
    message=f"""\
Subject:New Email{user_email}
From:{user_email}
{msg}"""
    buttton_msg=st.form_submit_button("submit")
    if buttton_msg:
        send_email(message)



