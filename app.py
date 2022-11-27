import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError
import requests

streamlit.title('My Amazing Athleisure Catalog')
streamlit.header('Pick a sweatsuit color or style')


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
