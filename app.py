from flask import Flask, jsonify, request, json
from flask_cors import CORS
from models import Name

app = Flask(__name__)
CORS(app)

memory_names[]

@app.route('/api/v1/inscribite/nombre', methods=["GET", "POST"])
def nombre():
    added = flask.request.method == 'POST'

    if added:
        body = flask.request.json
        new_name = Name(
            body["name"],
        memory_names.append(new_name.to_json()),
        return {"Nombre": new_name.to_json(), "mensaje": "Nombre agregado", "status": "ok"}



if __name__ == '__main__':
    app.run()
