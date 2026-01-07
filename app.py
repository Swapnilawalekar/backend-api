from flask import Flask, request, jsonify
from insert_data import insert_data
from fetch_data import fetch_all
from update_data import update_data
from delete_data import delete_data

app = Flask(__name__)

@app.route("/insert", methods=["POST"])
def insert_api():
    body = request.json

    insert_data(
        body["table"],
        body["data"]
    )

    return jsonify({"message": "Data inserted successfully"})

@app.route("/fetch/<table>", methods=["GET"])
def fetch_api(table):
    data = fetch_all(table)
    return jsonify(data)

@app.route("/update", methods=["PUT"])
def update_api():
    body = request.json

    update_data(
        body["table"],
        body["data"],
        body["condition"]
    )

    return jsonify({"message": "Data updated successfully"})

@app.route("/delete", methods=["DELETE"])
def delete_api():
    body = request.json

    delete_data(
        body["table"],
        body["condition"]
    )

    return jsonify({"message": "Data deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
