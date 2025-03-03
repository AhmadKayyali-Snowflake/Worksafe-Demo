import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor': '#0f1116', 'height': '100vh', 'padding': '20px'},
    children=[
        cyto.Cytoscape(
            id='lineage-graph',
            layout={'name': 'breadthfirst'},
            style={
                'width': '100%',
                'height': '100%',
                'background-color': '#0f1116'
            },
            elements=[
                # Nodes
                {'data': {'id': 'orders', 'label': 'ORDERS\nTable\nCreated: Jan 12, 2024'}, 'classes': 'table'},
                {'data': {'id': 'customers', 'label': 'CUSTOMER_DATA\nDynamic Table\nCreated: Feb 20, 2024'}, 'classes': 'dynamic'},
                {'data': {'id': 'transactions', 'label': 'TRANSACTION_LOGS\nDynamic Table\nCreated: Mar 15, 2024'}, 'classes': 'dynamic'},
                {'data': {'id': 'products', 'label': 'PRODUCTS\nTable\nCreated: Dec 8, 2023'}, 'classes': 'table'},
                {'data': {'id': 'inventory', 'label': 'INVENTORY_STATUS\nDynamic Table\nCreated: Feb 5, 2024'}, 'classes': 'dynamic'},
                {'data': {'id': 'shipping', 'label': 'SHIPPING_DETAILS\nTable\nCreated: Jan 25, 2024'}, 'classes': 'table'},
                {'data': {'id': 'reviews', 'label': 'CUSTOMER_REVIEWS\nDynamic Table\nCreated: Mar 1, 2024'}, 'classes': 'dynamic'},
                {'data': {'id': 'analytics', 'label': 'SALES_ANALYTICS\nView\nCreated: Mar 3, 2024'}, 'classes': 'dynamic'},

                # Edges (dependencies)
                {'data': {'source': 'orders', 'target': 'customers'}},
                {'data': {'source': 'orders', 'target': 'transactions'}},
                {'data': {'source': 'orders', 'target': 'shipping'}},
                {'data': {'source': 'products', 'target': 'inventory'}},
                {'data': {'source': 'products', 'target': 'orders'}},
                {'data': {'source': 'customers', 'target': 'reviews'}},
                {'data': {'source': 'transactions', 'target': 'analytics'}},
                {'data': {'source': 'inventory', 'target': 'analytics'}},
                {'data': {'source': 'reviews', 'target': 'analytics'}},
                {'data': {'source': 'shipping', 'target': 'analytics'}}
            ],
            
            stylesheet=[
                # Style for nodes
                {
                    'selector': 'node',
                    'style': {
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
                    'selector': '.dynamic',
                    'style': {
                        'border-color': '#7FBA00'
                    }
                },

                # Style for edges
                {
                    'selector': 'edge',
                    'style': {
                        'curve-style': 'bezier',
                        'target-arrow-shape': 'triangle',
                        'line-color': '#888',
                        'target-arrow-color': '#888',
                        'width': 2
                    }
                }
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)