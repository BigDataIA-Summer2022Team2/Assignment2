import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import altair as alt

 #Creating the dataset
data = {'Team 1':20, 'Team 3':15, 'Team 4': 30, 'Admin': 66}
Courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(Courses, values)
plt.xlabel("Teams")
plt.ylabel("Number of API functions calling")
plt.title("API Functions Call Bar Chart")
st.pyplot(fig)


###############################################################
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Team 1', 'Team 3', 'Team4', 'admin'
sizes = [3, 4, 5, 16]
explode = (0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('API functions Call Pie Chart')
st.pyplot(fig1)



source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
                    columns=['alcohol', 'beer', 'coke'], index=pd.RangeIndex(100, name='x'))
source = source.reset_index().melt('x', var_name='category', value_name='y')

line_chart = alt.Chart(source).mark_line(interpolate='basis').encode(
    alt.X('x', title='Year'),
    alt.Y('y', title='Amount in liters'),
    color='category:N'
).properties(
    title='Sales of consumer goods'
)

st.altair_chart(line_chart)
