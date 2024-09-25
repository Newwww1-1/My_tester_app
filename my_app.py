import streamlit as st
from PIL import Image
import data_coll

# Set page configuration and title
st.set_page_config(page_title="Participants Tracking Application", layout="centered", page_icon="🎯")

# Load and set the background image (Streamlit doesn't support a true background image, but you can display it in the page header)
bg_image = Image.open("E:/Nasa Space Apps Challenge/BG.jpg")  # Replace with your image file path

# Display header image and title
st.image(bg_image, use_column_width=True)
st.markdown("<h1 style='text-align: center; color: #333333;'>Participant Information Collection Form</h1>", unsafe_allow_html=True)

# Helper function to show message
def show_message(title, msg, type_="info"):
    if type_ == "info":
        st.info(f"{title}: {msg}")
    elif type_ == "warning":
        st.warning(f"{title}: {msg}")
    elif type_ == "error":
        st.error(f"{title}: {msg}")
    elif type_ == "success":
        st.success(f"{title}: {msg}")

# Validation for numeric input
def validate_numeric_input(value, field_name):
    if value and not value.isdigit():
        show_message("Input Error", f"{field_name} must contain only numeric values.", type_="warning")
        return False
    return True

# UI Elements - Form in Streamlit
with st.form("participant_form"):
    st.write("Please fill out the form below to register:")
    
    # Form fields
    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    mobile_no = st.text_input("Mobile No (Without Dash)", "")
    age_group = st.selectbox("Age Group", ["Below 10", "Between 10 to 14", "Between 15 to 18", "18 or Above 18"])
    cnic = st.text_input("CNIC No (Without Dashes)", "")
    
    # Conditionally enable/disable Guardian Email field
    if age_group in ["Below 10", "Between 10 to 14", "Between 15 to 18"]:
        guardian_email = st.text_input("Guardian/Receiver Email", "")
    else:
        guardian_email = st.text_input("Guardian/Receiver Email", "N/A", disabled=True)
    
    team_name = st.text_input("Team Name", "")
    challenge_name = st.text_input("Challenge Name", "")
    institute_name = st.text_input("Institute Name", "")

    # Submit button
    submitted = st.form_submit_button("Submit")

# Form validation and submission logic
if submitted:
    # Basic validation
    if not all([name, email, mobile_no, age_group, cnic, team_name, challenge_name, institute_name]):
        show_message("Input Error", "Please fill out all fields.", type_="warning")
    elif not validate_numeric_input(mobile_no, "Mobile No") or not validate_numeric_input(cnic, "CNIC No"):
        pass  # Error messages are already handled in the validation function
    else:
        # Insert the data into the database if validation passes
        data_coll.insert_data_if_cnic_not_exists(
            p_name=name,
            p_cnic=cnic,
            cell_=mobile_no,
            age_g=age_group,
            email=email,
            g_email=guardian_email,
            t_name=team_name,
            c_name=challenge_name,
            institute_name=institute_name
        )
        
        # Show success message and reset form (simulated by reloading the page)
        show_message("Success", "Your data has been submitted successfully!", type_="success")
        st.experimental_rerun()  # This will reload the app and reset the form

# Footer with Exit button (In Streamlit, we usually don't have an "exit" button like in desktop apps)
st.markdown("<hr>", unsafe_allow_html=True)
if st.button("Exit"):
    st.stop()

# Make UI adjustments for Streamlit's overall look
st.markdown("""
    <style>
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        padding: 10px;
        font-size: 16px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #007BFF;
    }
    .stTextInput>div>input {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)
