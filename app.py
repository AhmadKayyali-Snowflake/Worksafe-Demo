import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("🔗 Data Lineage Graph")

# Center the iframe using Streamlit layout
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.empty()
with col2:
    components.iframe("http://localhost:8050", height=850, width=1200, scrolling=False)
with col3:
    st.empty()
