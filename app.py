import streamlit as st

import pandas as pd

view = [100, 150, 30]
st.write("# Like counts!")
# st.write("## raw")
# view
st.write("## bar chart")
st.bar_chart(view)

sview = pd.Series(view)
sview