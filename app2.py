import streamlit as st
import streamlit.components.v1 as components

cytoscape_html = """
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/cytoscape/dist/cytoscape.min.js"></script>
  <style>
    #cy {
      width: 100%;
      height: 600px;
      background-color: #0f1116;
    }
  </style>
</head>
<body>
  <div id="cy"></div>
  <script>
    var cy = cytoscape({
      container: document.getElementById('cy'),
      layout: { name: 'breadthfirst' },
      style: [
        {
          selector: 'node',
          style: {
            'shape': 'roundrectangle',
            'background-color': '#1A1A1A',
            'color': '#FFFFFF',
            'label': 'data(label)',
            'text-wrap': 'wrap',
            'text-valign': 'center',
            'text-halign': 'center',
            'font-size': '12px',
            'padding': '10px',
            'border-width': '2px',
            'border-color': '#4B8BF4',
            'width': '220px',
            'height': '100px'
          }
        },
        {
          selector: '.dynamic',
          style: {
            'border-color': '#7FBA00'
          }
        },
        {
          selector: 'edge',
          style: {
            'curve-style': 'bezier',
            'target-arrow-shape': 'triangle',
            'line-color': '#888',
            'target-arrow-color': '#888',
            'width': 2
          }
        }
      ],
      elements: {
        nodes: [
          { data: { id: 'orders', label: 'ORDERS\\nTable\\nCreated: Jan 12, 2024' }},
          { data: { id: 'customers', label: 'CUSTOMER_DATA\\nDynamic Table\\nCreated: Feb 20, 2024' }, classes: 'dynamic' },
          { data: { id: 'transactions', label: 'TRANSACTION_LOGS\\nDynamic Table\\nCreated: Mar 15, 2024' }, classes: 'dynamic' },
          { data: { id: 'products', label: 'PRODUCTS\\nTable\\nCreated: Dec 8, 2023' }},
          { data: { id: 'inventory', label: 'INVENTORY_STATUS\\nDynamic Table\\nCreated: Feb 5, 2024' }, classes: 'dynamic' },
          { data: { id: 'shipping', label: 'SHIPPING_DETAILS\\nTable\\nCreated: Jan 25, 2024' }},
          { data: { id: 'reviews', label: 'CUSTOMER_REVIEWS\\nDynamic Table\\nCreated: Mar 1, 2024' }, classes: 'dynamic' },
          { data: { id: 'analytics', label: 'SALES_ANALYTICS\\nView\\nCreated: Mar 3, 2024' }, classes: 'dynamic' }
        ],
        edges: [
          { data: { source: 'orders', target: 'customers' }},
          { data: { source: 'orders', target: 'transactions' }},
          { data: { source: 'orders', target: 'shipping' }},
          { data: { source: 'products', target: 'inventory' }},
          { data: { source: 'products', target: 'orders' }},
          { data: { source: 'customers', target: 'reviews' }},
          { data: { source: 'transactions', target: 'analytics' }},
          { data: { source: 'inventory', target: 'analytics' }},
          { data: { source: 'reviews', target: 'analytics' }},
          { data: { source: 'shipping', target: 'analytics' }}
        ]
      }
    });
  </script>
</body>
</html>
"""

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.empty()
with col2:
    st.title("🔗 Data Lineage Graph")
    components.html(cytoscape_html, height=850, width=1200, scrolling=False)
with col3:
    st.empty()
