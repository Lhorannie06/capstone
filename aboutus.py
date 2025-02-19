#import pandas
#import streamlit as st
#import pandas as pd

#data=pd.read_csv("CAPSTONEDATA.csv")
#st.title("Data Table")
#st.table(data)
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data=pd.read_csv("CAPSTONEDATA.csv")

st.write("Country Tax")
st.bar_chart(data,x="COUNTRY",y="TAXDUE", color="#F8B6EF")
#plt.bar(data["COUNTRY"], bins=10, color="PINK", edgecolor="white")
st.divider()

st.write("Country Sales")
st.line_chart(data,x="COUNTRY",y="NETSALES", color="#E3978D")
st.divider()

st.write("Profit")
fig, ax= plt.subplots()
ax.hist(data["PROFITAFTERTAX"], color="RED")
st.pyplot(fig)
st.divider()