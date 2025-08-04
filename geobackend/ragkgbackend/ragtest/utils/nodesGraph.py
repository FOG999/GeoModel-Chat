from flask import Flask, jsonify
from flask_cors import CORS
from neo4j import GraphDatabase, basic_auth

app = Flask(__name__)
driver = GraphDatabase.driver("neo4j://10.242.10.244:7687", auth=basic_auth("neo4j", "gisgisgis"))
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8081"}})

@app.route('/api/getNodesGraph', methods=['GET'])
def get_nodes_graph_data():
    query = """
    MATCH (n:`__Entity__`) -[r]-> (m)
    RETURN n, r, m LIMIT 200
    """
    data = {
        "nodes": [],
        "edges": []
    }
    try:
        with driver.session() as session:
            results = session.run(query)
            node_ids = set()
            edge_ids = set()

            if results.peek() is None:
                print("No data found for the specified query.")
                return jsonify(data)

            for record in results:
                n = record["n"]
                m = record["m"]
                r = record["r"]

                def get_label(node):
                    return node.get("name") or node.get("title", "Unknown")
                
                for node in [n, m]:
                    node_id = node.id
                    node_label = get_label(node)
                    if node_id not in node_ids:
                        data["nodes"].append({
                            "id": node_id,
                            "label": node_label,
                        })
                        node_ids.add(node_id)

                start_id = n.id
                end_id = m.id
                edge_type = r.type
                edge_id = (start_id, end_id, edge_type)
                
                if edge_id not in edge_ids:
                    data["edges"].append({
                        "source": start_id,
                        "target": end_id,
                        "label": edge_type
                    })
                    edge_ids.add(edge_id)

            print("Nodes Graph Data:", data)
            return jsonify(data)
    except Exception as e:
        print("An error occurred in get_nodes_graph_data:", e)
        return jsonify({"error": "An error occurred retrieving the nodes graph data."})

@app.route('/api/getTxtGraph', methods=['GET'])
def get_txt_graph_data():
    query = """
    MATCH (n:`__Document__`) RETURN n LIMIT 100
    """
    data = {
        "nodes": [],
        "edges": []
    }
    try:
        with driver.session() as session:
            results = session.run(query)
            node_ids = set()
            
            if results.peek() is None:
                print("No data found for the specified query.")
                return jsonify(data)

            for record in results:
                n = record["n"]
                node_id = n.id
                node_title = n.get("title", "Unknown")

                if node_id not in node_ids:
                    data["nodes"].append({
                        "id": node_id,
                        "label": node_title,
                    })
                    node_ids.add(node_id)

            print("Text Graph Data:", data)
            return jsonify(data)
    except Exception as e:
        print("An error occurred in get_txt_graph_data:", e)
        return jsonify({"error": "An error occurred retrieving the text graph data."})

if __name__ == '__main__':
    app.run(debug=True)