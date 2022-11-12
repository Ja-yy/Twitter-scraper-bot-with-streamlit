import streamlit as st
from layout.layout_for_handle_form import layout_for_handle_form,expander_layout
from helper.download_button import convert_df
from  selenium_script.get_driver import redirect
from selenium_script.selenium_script_main import sc_main
from pathlib import Path
import numpy as np

def tab_2():
    intro_markdown = Path("view/tab2.md").read_text()
    st.markdown(intro_markdown, unsafe_allow_html=True)
    submit_button,email,password,search_term,select_tab,headless,browser_name,scroll = layout_for_handle_form()
    try:
        if submit_button:
                if not email:
                    st.warning(" Please, Enter Email!!",icon="⚠️")
                    st.stop()
                if not password:
                    st.warning(" Please, Enter Password!!!",icon="⚠️")
                    st.stop()
                if not search_term:
                    st.warning(" Can't select tab without search tearm, Please, Enter search tearm!!!", icon="⚠️")
                    st.stop()
                if headless == "Yes":
                    driver = redirect(browser_name=browser_name,headless=True)
                else:
                    driver = redirect(browser_name=browser_name,headless=False)
                df = sc_main(driver=driver, username=email,password=password,search_term=search_term,tab=select_tab,max_scroll=scroll)
                st.snow()
                st.success("Completed", icon="✅")   
                st.download_button(
                        label="Download",
                        data=convert_df(df),
                        file_name='Scrape-Twitter-Handlers.csv',
                        mime='text/csv',
                    )
                expander_layout(df)
    except Exception as e:
        print(e)
        st.error("Something Went Wrong!!!,Please try again...",icon="⚠️")
        st.stop()