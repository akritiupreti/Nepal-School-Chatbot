import streamlit as st
import requests

st.set_page_config(page_title="School Finder", page_icon="🎓")

st.title("🎓 School & College Finder")
st.write("Ask questions about schools, hostels, A Levels, locations, and programs.")

query = st.text_input("Your Question")

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        res = requests.post(
            "http://localhost:8000/query",
            json={"query": query}
        )
        data = res.json()

        st.subheader("Answer")
        st.write(data["answer"])