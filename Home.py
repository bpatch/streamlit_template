import streamlit as st
import pandas as pd
from background_tools import ExampleAnalysis, DatabaseConnector # Adapt contents of these packages for real app
import lorem # Delete this and remove lorem from pyproject.toml for real app

# Add the title and image for web browser tabs (must be first streamlit command)
st.set_page_config(page_title='Iris Analytics', 
                   page_icon='files/favicon.ico')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
            content:'Iris Analytics acknowledges Aboriginal and Torres Strait Islander people as the Traditional Custodians of the land and acknowledges and pays respect to their Elders, past and present. This web page is for internal use only. This page contains data that is not permitted for public or third-party release.'; 
            visibility: visible;
            display: block;
            position: relative;
            padding: 5px;
            top: 2px;
        }
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# Display VCDI logo at top of app
st.image('files/logo.png')

EA = ExampleAnalysis()

# Markdown text can be included like this:
text_string = """
This is an important description of the app that has 
been placed at the top of the page. 
"""
st.markdown(lorem.paragraph())

# Images can be included like this:
st.pyplot(EA.output_figure)

# Create an example dataframe to be displayed
example_df = pd.DataFrame(EA.X[1:5,:],
                         columns=['Length', 'Width'])

# Create a function which highlights every second row of displayed table
def highlight_everyother(s):
    return [f'background-color: #d0adf7' if x%2==1 else ''
            for x in range(len(s))]

st.dataframe(example_df.style.format("{:.2f}").apply(highlight_everyother))

# To obtain data from a PostgreSQL database: 

# D = DatabaseConnector() 

# session = D.get_db_sessionmaker()

# sql_query = """
# SELECT * FROM 
# {table_name}
# """

# df = pd.read_sql_query(sql_query.format(table_name='your_table_name'),
#                        session.bind)
