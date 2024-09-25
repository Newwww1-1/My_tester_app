import streamlit as st
from PIL import Image
import data_coll

# Set page configuration and title
st.set_page_config(page_title="Participants Important Information Collection Form", layout="centered", page_icon="🎯")


# UI Elements - Form in Streamlit
with st.form("participant_form", clear_on_submit=True):
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)  # Wrap the form in a styled div
    
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

    st.markdown("</div>", unsafe_allow_html=True)  # End of styled div

# Form validation and submission logic
if submitted:
    if not all([name, email, mobile_no, age_group, cnic, team_name, challenge_name, institute_name]):
        st.warning("Please fill out all fields.")
    elif not mobile_no.isdigit() or not cnic.isdigit():
        st.warning("Mobile No and CNIC must contain only numeric values.")
    else:
        if data_coll.insert_data_if_cnic_not_exists(p_name=name,p_cnic=cnic,cell_=mobile_no,age_g=age_group,email=email, g_email=guardian_email,t_name=team_name,c_name=challenge_name,institute_name=institute_name) == 1:
            st.success("Your data has been submitted successfully!")
            st.experimental_rerun()
        else:
            st.success("CNIC is Already Registered")
            st.experimental_rerun()
# Footer with Exit button
if st.button("Exit"):
    st.stop()
