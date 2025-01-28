import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit UI Setup
st.title("📊 Interactive Data Visualization Tool")
st.sidebar.header("Upload your CSV file")

# Upload CSV File
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    # Select columns
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    
    if numeric_columns:
        st.sidebar.header("Select Columns for Visualization")
        x_axis = st.sidebar.selectbox("Select X-axis", options=numeric_columns + categorical_columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", options=numeric_columns)
        
        # Visualization Type
        st.sidebar.header("Select Visualization Type")
        plot_type = st.sidebar.radio("Choose a chart type", ["Line Chart", "Bar Chart", "Scatter Plot", "Heatmap"])
        
        # Generate Charts
        if plot_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart: {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        
        elif plot_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart: {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        
        elif plot_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot: {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        
        elif plot_type == "Heatmap":
            fig, ax = plt.subplots()
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
    
    else:
        st.warning("No numeric columns found. Please upload a dataset with numeric values.")

else:
    st.info("Upload a CSV file to begin.")
