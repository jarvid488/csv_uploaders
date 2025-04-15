import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.set_page_config(page_title='csv file reader',layout='wide')
st.title(f"Example Streamlit App :balloon: {st.__version__}")
session = get_active_session()
st.header('single fike upload')
upload_file=st.file_uploader('Upload your CSV-file')
df=pd.read_csv(upload_file)
st.dataframe(df,width=1800, height=1200)
