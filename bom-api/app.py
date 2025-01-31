from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Path where BoM files are stored
BOM_DIR = "/bom"

def read_json_file(filename):
    try:
        with open(os.path.join(BOM_DIR, filename), "r") as f:
            return json.load(f)
    except Exception as e:
        return {"error": str(e)}

@app.route('/bom', methods=['GET'])
def get_bom():
    return jsonify({
        "cluster-info": read_json_file("cluster-info.json"),
        "nodes": read_json_file("nodes.json"),
        "namespaces": read_json_file("namespaces.json"),
        "deployments": read_json_file("deployments.json"),
        "services": read_json_file("services.json"),
        "configmaps": read_json_file("configmaps.json"),
        "secrets": read_json_file("secrets.json"),
        "helm-charts": read_json_file("helm-charts.json"),
    })

@app.route('/bom/<component>', methods=['GET'])
def get_component(component):
    return jsonify(read_json_file(f"{component}.json"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
