import pandas as pd
import streamlit as st
import numpy as np

#Dataframes

df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))

st.table(df)