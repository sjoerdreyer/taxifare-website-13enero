import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

result_checkbox = st.checkbox('this is a checkboxx')

if result_checkbox:
    st.write('checkbox has been checked!!')
else:
    st.text('checkbox not checked!!!!!!')

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

# csv = pd.read_csv('data.csv')

# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name='large_df.csv',
#     mime='text/csv',
# )

st.button("Reset")
if st.button('Say hello'):
    st.write('Hello!')
else:
    st.write('Goodbye')
