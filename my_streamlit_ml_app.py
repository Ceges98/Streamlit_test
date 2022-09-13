import streamlit as st

st.title('This is the app title')
st.header('this is the markdown')
st.markdown('this is the header')
st.subheader('this is the subheader')
st.caption('this is the caption')
st.code('x=2021')
st.latex('a+a r^1+a r^2+a r^3')


import altair as alt
import numpy as np
import pandas as pd

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

c1 = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)

st.altair_chart(c1, use_container_width=True)


import streamlit as st

st.title('Semantic similarity Application')
sentences1 = st.text_input('insert sentences1:')
sentences2 = st.text_input('insert sentences2:')

if st.button('Submit'):
    st.write('Sentences1 is:', sentences1)
    st.write('Sentences2 is:', sentences2)