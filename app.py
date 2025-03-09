import streamlit as st
import re
import random
import string

def evaluate_password(password):
    score = 0
    feedback = []
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Password Input and Generation Button
password = st.text_input("Enter your password", type="password")
if st.button("Generate Strong Password"):
    password = generate_password()
    st.text_input("Generated Password", password, type="default")

if password:
    strength, feedback = evaluate_password(password)
    
    st.subheader(f"Password Strength: {strength}")
    
    if strength == "Weak":
        st.warning("Your password is weak. Consider these improvements:")
        for tip in feedback:
            st.write(f"- {tip}")
    elif strength == "Moderate":
        st.info("Your password is moderate. Try adding more security elements.")
    else:
        st.success("Great! Your password is strong.")
