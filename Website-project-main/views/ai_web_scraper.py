import streamlit as st

from views.utils.scrape import scrape_website, extract_body_content, clean_body_content, split_content
from views.utils.parse import parse_with_gemini

st.title("AI Web Scraper")
url = st.text_input("Enter Website Url")

if st.button("Scrape Website"):
    if url:
        st.write("Scraping Website...")
        html: str = scrape_website(url)
        body: str = extract_body_content(html)
        content: str = clean_body_content(body)

        st.session_state.content = content

if st.session_state.get("content"):
    with st.expander("View Content"):
        st.text_area("Content", st.session_state["content"], height=300)
    parse_desc = st.text_area("Describe what you want to parse")

    model_options = [
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro"
    ]
    selected_model = st.selectbox("Choose Gemini Model", options=model_options, index=0)

    if st.button("Parse Content"):
        if parse_desc:
            st.write("Passing the output ...")
            chunks: list[str] = split_content(st.session_state.content)
            parse_result = parse_with_gemini(chunks, parse_desc)
            st.write(parse_result)
