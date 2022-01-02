import os
from flask import Flask, request, abort
from Stats import *
from json import dumps as jsonstring
from waitress import serve

app = Flask(__name__)

stats = Stats()
if os.getenv("ENV") == "local":
    stats = Stats(temp_file="temp_file")

@app.route("/api/stats", methods=['GET'])
def get_stats():
    raw_result = stats.get_stats()
    result = jsonstring(raw_result.__dict__)

    return result

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3000)
