import pandas as pd
import streamlit as st

#normal way 

st.write("Hello **World!**")

#magic command

"Hello  **World!**"

#st.caption("Command)

st.caption("Command")

#st.code

code = '''
def new():
    print("Hello)'''

st.code(code,language='python')

#st.text

st.text('loreum epsium')

