# Worksafe Lineage View Demo

## Overview

This Streamlit app is meant to demonstrate the feasability of creating a lineage view to breakdown upstream and downstream table dependencies. This demonstration will utilize dash	For building the web app and layout and dash_cytoscape for creating the interactive data lineage graph.


## Setup Instructions

### Step 1 - Activate Virtual Environment & Install Dependencies

1. This project uses python version 3.11.6
2. Ensure you are in your project directory:
   ```bash
   cd path/to/project
   ```
3. Create and activate a virtual environment by running:
   ```bash
   python3.11 -m venv venv
   ```
   - On Windows, run:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux, run:
     ```bash
     source venv/bin/activate
     ```
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2 - Run Project

Option 1 - Rendering the visualization html in Streamlit:
1. Run the Streamlit app by running the following in a new terminal:
   ```bash
   streamlit run app2.py
   ```
   This will start the streamlit app which displays the visualization.

Option 2 - Running Flask app and embedding it into Streamlit using iframe:
1. Run the following:
   ```python
   python visulization.py
   ```
   This will start the Flask app with the visualization at http://127.0.0.1:8050/
2. After running the command above, start the Streamlit app by running the following in a new terminal:
   ```bash
   streamlit run app.py
   ```
   This will start the streamlit app which displays the visualization via iframe.

### Recommendation
If you are considering using dash for the visualization tool. I would recommend developing the html first, seperate to Streamlit. Then, once you are satisfied with the visualization render the visualization directly in Streamlit.