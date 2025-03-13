import streamlit as st

about_page = st.Page(
    "./views/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True
)

project_1_page = st.Page(
    "./views/chat_bot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:",
)
project_2_page = st.Page(
    "views/ai_web_scraper",
    title = "AI Web Scraper",
    iron = ":material/search:"
)
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page],
    }
)
st.sidebar.text("Made with ❤️ by Mati")

pg.run()

#streamlit run streamlit_app.py