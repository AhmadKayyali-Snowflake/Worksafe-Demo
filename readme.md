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

1. Run the following:
   ```python
   python visulization.py
   ```
   This will start the Flask app with the visualization at http://127.0.0.1:8050/
2. Run the following:
   ```bash
   streamlit run app.py
   ```
   This will start the streamlit app which displays the visualization via iframe.

