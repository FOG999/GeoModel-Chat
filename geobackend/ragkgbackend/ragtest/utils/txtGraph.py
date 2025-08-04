from flask import Flask, jsonify
from flask_cors import CORS
from neo4j import GraphDatabase, basic_auth

app = Flask(__name__)
driver = GraphDatabase.driver("neo4j://10.242.10.244:7687", auth=basic_auth("neo4j", "gisgisgis"))
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8081"}})

@app.route('/api/getTxtGraph', methods=['GET'])
def get_graph_data():
    query = """
    MATCH (n:`__Document__`) RETURN n LIMIT 100
    """
    data = {
        "nodes": [],
        "edges": []  # 无关系
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
                node_title = n.get("title", "Unknown")  # 获取节点的 title 属性

                if node_id not in node_ids:
                    data["nodes"].append({
                        "id": node_id,
                        "label": node_title,  # 使用 title 作为标签
                    })
                    node_ids.add(node_id)

            print("Graph Data:", data)
            return jsonify(data)
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({"error": "An error occurred retrieving the graph data."})

if __name__ == '__main__':
    app.run(debug=True)