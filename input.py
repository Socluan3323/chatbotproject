import streamlit as st

with st.form(key="my_form"):
    user_input = st.text_input("Enter topic")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state["topic"] = user_input
        st.switch_page("pages/mirror.py")