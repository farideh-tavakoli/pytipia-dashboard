import streamlit as st
from io import StringIO
import json

st.title(":zap: Pytopia Dashboard")

uploaded_file = st.file_uploader("Choose a file")

with st.expander('Statistics'):
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)


        data = json.loads(string_data)
        st.json(data)
