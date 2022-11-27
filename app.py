import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError
import requests

streamlit.title('My Amazing Athleisure Catalog')
streamlit.header('Pick a sweatsuit color or style')
