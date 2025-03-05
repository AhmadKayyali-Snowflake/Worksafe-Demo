import streamlit as st
import streamlit.components.v1 as components
from session import create_session
import pandas as pd
import json

st.set_page_config(layout="wide")

session = create_session()

def create_cytoscape_elements(upstream_df, downstream_df, selected_table):
    nodes = []
    edges = []

    nodes.append({"data": {"id": selected_table, "label": selected_table}, "classes": "selected-table"})

    for _, row in upstream_df.iterrows():
        source = row["SOURCE_OBJECT_NAME"]
        nodes.append({"data": {"id": source, "label": source}})
        edges.append({"data": {"source": source, "target": selected_table}})

    for _, row in downstream_df.iterrows():
        target = row["TARGET_OBJECT_NAME"]
        nodes.append({"data": {"id": target, "label": target}})
        edges.append({"data": {"source": selected_table, "target": target}})

    return nodes + edges


col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.empty()
with col2:
    st.title("🔗 Data Lineage Graph")

    databases_result = session.sql("SHOW DATABASES").collect()
    databases = pd.DataFrame([row.as_dict() for row in databases_result])
    st.selectbox(label="Select a Database", options=databases["name"], key="database", index=None)

    if st.session_state.get("database"):
        tables_result = session.sql(f"SHOW TABLES IN DATABASE {st.session_state.database}").collect()
        tables = pd.DataFrame([row.as_dict() for row in tables_result])
        if tables.shape[0] > 0:
            tables["full_table_name"] = (
                tables["database_name"]
                + "."
                + tables["schema_name"]
                + ".\""
                + tables["name"]
                + "\""
            )

            st.selectbox(label="Select a Table", options=tables["full_table_name"], key="table")
        else:
            st.info("This database has no tables.")
    else:
        st.info("Please select a database.")

    if st.session_state.get("table"):

        upstream_sql = f"""
            SELECT * FROM TABLE(
                SNOWFLAKE.CORE.GET_LINEAGE('{st.session_state.table}', 'TABLE', 'UPSTREAM')
            )
        """
        downstream_sql = f"""
            SELECT * FROM TABLE(
                SNOWFLAKE.CORE.GET_LINEAGE('{st.session_state.table}', 'TABLE', 'DOWNSTREAM')
            )
        """

        columns_to_drop = [
          "SOURCE_OBJECT_VERSION",
          "SOURCE_COLUMN_NAME",
          "TARGET_OBJECT_VERSION",
          "TARGET_COLUMN_NAME"
        ]

        # Clean upstream lineage
        upstream = session.sql(upstream_sql).to_pandas()
        upstream = upstream.drop(columns=columns_to_drop, errors="ignore")

        # Clean downstream lineage
        downstream = session.sql(downstream_sql).to_pandas()
        downstream = downstream.drop(columns=columns_to_drop, errors="ignore")

        elements = create_cytoscape_elements(upstream, downstream, st.session_state.table)
        elements_json = json.dumps(elements)

        splitter = st.columns(2)

        with splitter[0]:
            cytoscape_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
              <script src="https://unpkg.com/cytoscape/dist/cytoscape.min.js"></script>
              <style>
                #cy {{
                  width: 100%;
                  height: 600px;
                  background-color: #0f1116;
                }}
              </style>
            </head>
            <body>
              <div id="cy"></div>
              <script>
                var cy = cytoscape({{
                  container: document.getElementById('cy'),
                  layout: {{ name: 'breadthfirst' }},
                  minZoom: 0.5,
                  maxZoom: 2,
                  style: [
                    {{
                      selector: 'node',
                      style: {{
                        'shape': 'roundrectangle',
                        'background-color': '#1A1A1A',
                        'color': '#FFFFFF',
                        'label': 'data(label)',
                        'text-valign': 'center',
                        'text-halign': 'center',
                        'font-size': '12px',
                        'padding': '10px',
                        'border-width': '2px',
                        'border-color': '#4B8BF4',
                        'width': '220px',
                        'height': '100px'
                      }}
                    }},
                    {{
                      selector: '.selected-table',
                      style: {{
                        'background-color': '#2E86C1',
                        'border-color': '#1B4F72',
                        'border-width': '4px',
                        'font-weight': 'bold',
                        'color': '#FFFFFF'
                      }}
                    }},
                    {{
                      selector: 'edge',
                      style: {{
                        'curve-style': 'bezier',
                        'target-arrow-shape': 'triangle',
                        'line-color': '#888',
                        'target-arrow-color': '#888',
                        'width': 2
                      }}
                    }}
                  ],
                  elements: {elements_json}
                }});
              </script>
            </body>
            </html>
            """
            components.html(cytoscape_html, height=850, width=600, scrolling=False)

        with splitter[1]:
            st.subheader("⬆️ Upstream Lineage")
            with st.container():
                st.dataframe(upstream, use_container_width=True, height=150, hide_index=True)

            st.subheader("⬇️ Downstream Lineage")
            with st.container():
                st.dataframe(downstream, use_container_width=True, height=150, hide_index=True)

with col3:
    st.empty()