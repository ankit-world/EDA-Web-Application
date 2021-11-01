import pandas as pd
import numpy as np
import streamlit as stream
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from PIL import Image

# Title of your web APP
stream.markdown('''

# **EDA APPLICATION**

Explore your data using **Pandas Profiling** Library

''')

# Upload the csv file for which you need to perform EDA

with stream.sidebar.header('Upload your csv file'):
    uploaded_data = stream.sidebar.file_uploader('Upload your csv file here', type=["csv"])

    stream.sidebar.markdown("""

[Dummy csv file](https://raw.githubusercontent.com/ankit-world/ML_Hyperparameter-Optimization-APP/main/insurance.csv)
""")

# Pandas Profiling Report
if uploaded_data is not None:

    @stream.cache
    def csv_load():
        csv_data = pd.read_csv(uploaded_data)
        return csv_data


    data = csv_load()

    profile_report = ProfileReport(data, explorative=True)

    stream.header('**Input Data**')

    stream.write(data)

    stream.write('---')

    stream.header('**Pandas Profiling Report**')

    st_profile_report(profile_report)

else:

    stream.info('Waiting for csv file to be uploaded.')
    if stream.button('Press to use Example Dataset'):
        # Example dataset
        @stream.cache
        def data_load():
            d = pd.read_csv(
                'https://raw.githubusercontent.com/ankit-world/ML_Hyperparameter-Optimization-APP/main/insurance.csv')
            d1 = pd.DataFrame(d)

            return d1

        df = data_load()

        profile_report = ProfileReport(df, explorative=True)

        stream.header('**Input csv Dataset**')

        stream.write(df)

        stream.write('---')

        stream.header('**Pandas Profiling Report**')

        st_profile_report(profile_report)
