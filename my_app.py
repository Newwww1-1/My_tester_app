import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Participants Tracking Application", layout="centered")

# Apply custom CSS for fonts and styling
st.markdown(
    """
    <style>
    .title {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: #333333;
        margin-top: 20px;
    }
    .label {
        font-family: 'Times New Roman', Times, serif;
        font-size: 14px;
        font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Add the main heading
st.markdown('<div class="title">Participants Important Required!</div>', unsafe_allow_html=True)

# Create the form fields
with st.form("participant_form"):
    st.markdown('<span class="label">Name:</span>', unsafe_allow_html=True)
    name = st.text_input(" ", key="name")

    st.markdown('<span class="label">Email:</span>', unsafe_allow_html=True)
    email = st.text_input(" ", key="email")

    st.markdown('<span class="label">Mobile No (Without Dash):</span>', unsafe_allow_html=True)
    mobile_no = st.text_input(" ", key="mobile_no")

    st.markdown('<span class="label">Age Group:</span>', unsafe_allow_html=True)
    age_group = st.selectbox(" ", ["Below 10", "Between 10 to 14", "Between 15 to 18", "18 or Above 18"], key="age_group")

    st.markdown('<span class="label">CNIC No (Without Dashes):</span>', unsafe_allow_html=True)
    cnic = st.text_input(" ", key="cnic")

    st.markdown('<span class="label">Guardian/Receiver Email:</span>', unsafe_allow_html=True)
    guardian_email = st.text_input(" ", key="guardian_email")

    st.markdown('<span class="label">Team Name:</span>', unsafe_allow_html=True)
    team_name = st.text_input(" ", key="team_name")

    st.markdown('<span class="label">Challenge Name:</span>', unsafe_allow_html=True)
    challenge_name = st.text_input(" ", key="challenge_name")

    st.markdown('<span class="label">Institute Name:</span>', unsafe_allow_html=True)
    institute_name = st.text_input(" ", key="institute_name")

    # Form submission button
    submitted = st.form_submit_button("Submit")

    # Handle form submission
    if submitted:
        if not name or not email or not mobile_no or not cnic or not age_group or not challenge_name or not institute_name:
            st.warning("Please fill out all the required fields.")
        else:
            # Call the data_coll.insert_data_if_cnic_not_exists function
            import data_coll  # Assuming data_coll is a Python module available in your project

            # Attempt to insert the data and check the result
            result = data_coll.insert_data_if_cnic_not_exists(
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

            if result == 1:
                st.success("Data submitted successfully!")
                # Optionally clear the fields by resetting the form if needed
            else:
                st.error("Data could not be submitted. CNIC might already exist.")
