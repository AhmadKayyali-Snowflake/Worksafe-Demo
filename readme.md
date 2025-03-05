# Worksafe Lineage View Demo

## Overview

This Streamlit app is meant to demonstrate the feasability of creating a lineage view to breakdown upstream and downstream table dependencies. This demonstration will utilize dash	For building the web app and layout and dash_cytoscape for creating the interactive data lineage graph.


## Setup Instructions

### Step 1 - Install and Configure Snow CLI
1. This project will read your snowflake credentials from your config.toml file that configure when setting up your Snow CLI.
2. Please follow this documentation to get install SnowCLI: [SnowCLI Installation Guide](https://docs.snowflake.com/en/developer-guide/snowflake-cli/installation/installation)
3. Please follow this documentation to add a snowflake connection: [SnowCLI Configuration Guide](https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-connections#add-a-connection)

### Step 2 - Activate Virtual Environment & Install Dependencies

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

### Step 3 - Run Project

1. Alter line 9 in session.py file at the root of the folder and add the name of your connection.
   ```python
   session = Session.builder.config("connection_name", "<YOUR_CONNECTION_NAME>").create()
   ```

2. Run the Streamlit app by running the following in a new terminal:
   ```bash
   streamlit run app.py
   ```