import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def accueil():
    return jsonify(
        message="API fil rouge",
        binome=os.environ.get("BINOME", "inconnu"),
        conteneur=socket.gethostname(),
    )

@app.get("/sante")
def sante():
    return jsonify(statut="ok")

@app.get("/version")
def version():
    return jsonify(version="1.1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
