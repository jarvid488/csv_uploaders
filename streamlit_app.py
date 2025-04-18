# Import python packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.set_page_config(page_title='csv file reader',layout='wide')
st.title(f"Example Streamlit App :balloon: {st.__version__}")
session = get_active_session()
st.header('single file upload')
upload_file=st.file_uploader('Upload your CSV-file')
#st.write(upload_file)
if upload_file:
    df=pd.read_csv(upload_file)
    #st.write(df)
    pd_df=pd.DataFrame(df)
    st.write(pd_df)
    str=''
    #st.dataframe(df,width=1800, height=1200)
    #for index, row in pd_df.iterrows():
        #st.write(row['country_Code'])
        #str=','.join(f"{row['country_Code']} VARCHAR")

    #st.write(str)
    #for col in df.columns:
        #st.write(col)
    create_table_sql = f"""
    CREATE OR REPLACE TABLE smoothies.public.currency_tables (
        {', '.join([f"{row['country_Code']} {row['Country_number']}" for index,row in pd_df.iterrows()])}
    )
    """
    st.write(create_table_sql)
    session.sql(create_table_sql).collect()
    #{', '.join([f"{col} VARCHAR" for col in df.columns])}
    


#snow://streamlit/SMOOTHIES.PUBLIC.TQ7W2WHV3PBEL7LW/versions/live/environment.yml
#snow://streamlit/SMOOTHIES.PUBLIC.TQ7W2WHV3PBEL7LW/versions/live/streamlit_app.py
