import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# Title
st.title("📊 Simple Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")

# If a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show data preview
    st.subheader("🔍 Data Preview")
    st.write(df.head())

    # Show summary statistics
    st.subheader("📈 Data Summary")
    st.write(df.describe())

    # Filtering options
    st.subheader("🔎 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    # Apply filter
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plotting section
    st.subheader("📊 Plot Data")

    chart_type = st.selectbox("Choose chart type", ["Line", "Bar", "Scatter"])
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        if chart_type == "Line":
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        elif chart_type == "Bar":
            st.bar_chart(filtered_df.set_index(x_column)[y_column])
        elif chart_type == "Scatter":
            fig, ax = plt.subplots() # type: ignore
            ax.scatter(filtered_df[x_column], filtered_df[y_column], color='purple')
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"{y_column} vs {x_column}")
            st.pyplot(fig)
else:
    st.write("👈 Upload a CSV file to get started!")
