import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set page config
st.set_page_config(page_title="Data Sweeper", layout="wide", initial_sidebar_state="expanded")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Summary", "Visualization", "Conversion"])

# Sidebar instructions
st.sidebar.info(
    """
    **Instructions:**
    1. Upload your CSV or Excel files.
    2. Clean your data using the provided options.
    3. View a summary and visualize the data.
    4. Convert your cleaned data to a preferred format.
    """
)

# Main title and description
st.title("Datasweeper Sterling Integrator By Anam Zeeshan Shergill")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

# File uploader
st.markdown("## 📀 **Upload your files (accepts CSV, XLSX, XLS):**")
uploaded_files = st.file_uploader(
    label="Upload your files",
    type=["csv", "xlsx", "xls"],
    accept_multiple_files=True
)


if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext in [".xlsx", ".xls"]:
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading file {file.name}: {e}")
            continue

        st.markdown(f"### File: {file.name}")

        # Display file preview
        st.write("🔎 **Preview the DataFrame**")
        st.dataframe(df.head())

        # Data cleaning options
        st.subheader("📟 Data Cleaning Options!")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove duplicates from {file.name}"):
                    before = df.shape[0]
                    df.drop_duplicates(inplace=True)
                    after = df.shape[0]
                    st.success(f"Removed {before - after} duplicate rows.")
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    if len(numeric_cols) > 0:
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.success("Missing numeric values have been filled with column means.")
                    else:
                        st.warning("No numeric columns to fill missing values.")

        # Column selection
        st.subheader("🎯👈 Select Columns to Keep!")
        selected_columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Sidebar: Data summary
        if page == "Data Summary":
            st.markdown("## 🧾 Data Summary")
            st.write("**Shape:**", df.shape)
            st.write("**Columns:**", list(df.columns))
            st.write("**Data Types:**")
            st.write(df.dtypes)
            st.write("**Statistical Summary:**")
            st.dataframe(df.describe())

        # Visualization
        if page == "Visualization":
            st.markdown("## 📊 Data Visualization!")
            numeric_df = df.select_dtypes(include="number")
            if numeric_df.empty:
                st.warning("No numeric data available for visualization.")
            else:
                # Let user choose the type of visualization
                viz_type = st.selectbox("Select Visualization Type", ["Bar Chart", "Line Chart", "Area Chart"])
                # Let user select which columns to plot
                numeric_cols = list(numeric_df.columns)
                cols_to_plot = st.multiselect("Select columns to visualize", numeric_cols, default=numeric_cols[:min(2, len(numeric_cols))])
                if cols_to_plot:
                    if viz_type == "Bar Chart":
                        st.bar_chart(numeric_df[cols_to_plot])
                    elif viz_type == "Line Chart":
                        st.line_chart(numeric_df[cols_to_plot])
                    elif viz_type == "Area Chart":
                        st.area_chart(numeric_df[cols_to_plot])
                else:
                    st.info("Select at least one numeric column for visualization.")

        # Conversion options
        if page == "Conversion":
            st.markdown("## 🔁 Conversion Options!")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                try:
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False)
                        file_name = file.name.replace(file_ext, ".csv")
                        mime_type = "text/csv"
                    elif conversion_type == "Excel":
                        df.to_excel(buffer, index=False)
                        file_name = file.name.replace(file_ext, ".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    buffer.seek(0)
                    st.download_button(
                        label=f"Download {file.name} as {conversion_type}",
                        data=buffer,
                        file_name=file_name,
                        mime=mime_type
                    )
                except Exception as e:
                    st.error(f"Conversion failed: {e}")

        st.markdown("---")
    st.success("🎊 All files processed successfully!👍")
else:
    st.info("📤 Upload one or more files to get started!")
