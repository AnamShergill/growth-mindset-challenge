# growth-mindset-challenge
Created Datasweeper Sterling Integrator using Python and Streamlit where user can transform files between CSV and Excel formats with built-in data cleaning and visualization.

# **Datasweeper Sterling Integrator** 🚀

**Datasweeper Sterling Integrator** is a Streamlit-powered application designed to help users quickly transform and clean their data files. With this tool, you can easily upload CSV and Excel files, perform basic data cleaning, visualize your data, and convert files between CSV and Excel formats—all within an intuitive, professional interface.

---

## **✨ Features**

- **📁 File Upload:**  
  Easily upload multiple CSV, XLSX, and XLS files.
  
- **🛠 Data Cleaning Options:**  
  - Remove duplicate rows  
  - Fill missing values in numeric columns using the column mean
  
- **🔍 Column Selection:**  
  Choose which columns to keep for further processing.

- **📊 Data Summary:**  
  Get a quick summary of your data, including shape, column data types, and descriptive statistics.

- **🎨 Data Visualization:**  
  Visualize your numeric data using Bar, Line, or Area charts. Customize which columns to plot.

- **🔄 File Conversion:**  
  Convert your cleaned data files between CSV and Excel formats. Download the converted files with a click.

- **💻 Professional UI:**  
  The app includes a modern, responsive design with sidebar navigation, clear instructions, and feedback messages to guide you through each step.

---

## **🚀 Getting Started**

### **Prerequisites**

Make sure you have Python installed (version 3.7 or later is recommended). Then, install the necessary dependencies:

```bash
pip install streamlit pandas openpyxl


## **🚀 Running the App**

Clone the repository:

bash
Copy
Edit
git clone https://github.com/AnamShergill/growth-mindset-challenge.git
cd growth-mindset-challenge
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Run the application:

bash
Copy
Edit
streamlit run index.py
Open your browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

## **📂 Project Structure**
index.py
The main Streamlit application containing the data cleaning, visualization, and conversion functionalities.

.streamlit/config.toml
(Optional) A configuration file for customizing the Streamlit theme and other settings.

README.md
This file.

## **🎨 Customization**
You can customize the appearance and functionality of the app by editing the code. For example:

Theme:
Modify the .streamlit/config.toml file to change the color scheme.
Data Cleaning:
Add more data cleaning options as needed.
Visualization:
Expand the visualization options with additional chart types.

## ***🤝 Contributing***
Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## **📝 License**
This project is licensed under the MIT License.

## **📬 Contact**
For questions or feedback, please reach out to anamzeeshanshergill@gmail.com .

