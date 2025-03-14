import streamlit as st
import pandas as pd
from modules.Handler import Handler

data = "resp.json"

class WebView:

    st.title("test beta")

    def get_data(self):

        dataset = pd.read_json(data)
        print(dataset)

       



   