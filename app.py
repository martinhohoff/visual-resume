import streamlit as st
import pandas as pd
import plotly.express as px

# Load your exported LinkedIn CSVs
positions = pd.read_csv('Positions.csv')
education = pd.read_csv('Education.csv')

st.title("📊 Martinho's Data Science Resume")

# Experience timeline
st.header("💼 Experience Timeline")
positions['Start Date'] = pd.to_datetime(positions['Start Date'])
fig = px.timeline(positions, x_start='Start Date', x_end='End Date', y='Company Name', color='Title', hover_name='Description')
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig)

# Education section
st.header("🎓 Education")
for _, row in education.iterrows():
    st.subheader(f"{row['School Name']}")
    st.write(f"{row['Degree Name']} • {row['Field of Study']}")
    st.write(f"{row['Start Date']} — {row['End Date']}")

# Skills wordcloud or tags
st.header("🛠️ Skills")
st.write("Python, SQL, Pandas, AWS, Data Engineering, ETL, Dashboards, APIs")

# Download CV
st.download_button("📄 Download my CV", data=open("cv.pdf", "rb"), file_name="martinho_cv.pdf")
