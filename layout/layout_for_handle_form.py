import streamlit as st

def layout_for_handle_form():
     with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        with st.form(key="myform"):
            with st.container():
                col1, col2 ,col3 = st.columns(3)
                with col1:
                    st.header("Configuration")
                    browser_name = st.selectbox('Which browser would you like to select?',('Chrome', 'Firefox'))
                    headless = st.radio("Do you want hide browser window",('Yes', 'No'))
                with col2:
                    st.header("Credential")
                    email = st.text_input("Enter your email")
                    password = st.text_input("Enter your password",type="password")
                with col3:
                    st.header("Filter Options")
                    search_term = st.text_input("Enter search term")
                    select_tab = st.radio("Which tab do you want to scrap?",('People','Top', 'Photos','Latest','Videos'))
                    scroll = st.slider('How many times you want to scroll?', 0, 50, 5)
            submit_button = st.form_submit_button(label="Scrap")
        
        return submit_button,email,password,search_term,select_tab,headless,browser_name,scroll