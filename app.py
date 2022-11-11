import streamlit as st
from view.tab_view_2 import tab_2
from view.tab_view_1 import tab_1


username = "OtarioTopez"
password = "Qwertyuiop@890"
serch = "marketing agencies"

def main():
    st.set_page_config(layout="wide")
    st.title("Twitter Scraper Bot 🤖")
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["Home","Twitter Handle Scraper","Tweet Scraper","Profile Scraper","CSV"])
    with tab1:
        tab_1()
    with tab2:
        tab_2()
                
if __name__ == "__main__":
    main()