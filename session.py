import os
from snowflake.snowpark import Session
from snowflake.snowpark.exceptions import *
import streamlit as st

@st.cache_resource
def create_session():
    from snowflake.snowpark import Session
    session = Session.builder.config("connection_name", "<YOUR_CONNECTION>").create()
    return session