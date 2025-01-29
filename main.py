
import streamlit as st
import scrape
import clean
import parse

st.title("AI Web Scrapper")
url= st.text_input("Enter a website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping the website")
    dom_content = scrape.get_page_source(url)
    cleaned_content= clean.extract_cleaned_content(dom_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    
if "dom_content" in st.session_state:
    user_input= st.text_area("Describe what you want to parse")

    if st.button("Parse content"):
        if user_input:
            st.write("Parsing content")

            dom_chunks= clean.split_dom_content(st.session_state.dom_content)
            result = parse.parse_with_ollama(dom_chunks, user_input)
            st.write(result)

