import streamlit as st
import re

st.set_page_config(page_title="password strength Checker", page_icon="🔐")

st.title("🔐Password Strength Chacker")

st.markdown("""
## welcome to the ultimate password strength checker!👏
use this simple tool to check the strength of your password and get suggestions on how to make it strong.
          we will give you helpful tips to creat a **strong password** 🔐""")

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
       feedback.append("❌password should be at least 8 charactors long.")
            
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
    else:
        feedback.append("❌password should contain both upper and lower case charactors.")
    
    if re.search(r"[!#@$%&']", password):
        score += 1
    else:
        feedback.append("❌password should contain at least one digit character[!#@$%&'].")
    if score == 10:
        feedback.append("✔️Your password is strong!")
    elif score == 3:
        feedback.append("🔴your password is medium strength. it could be stronger.")
    else:
        feedback.append("🟡your password is weak. please make it stronger.")
        
st.write("Uncomplete code")
        


        
                  
        
    
        