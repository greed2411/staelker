import os

from singleton import TweetManager
from flask import Flask, request, jsonify                                                  

import logging
logging.getLogger().setLevel(logging.INFO)


app = Flask(__name__)

FLASK_HOST = os.getenv("FLASK_HOST")
FLASK_PORT = os.getenv("FLASK_PORT")

@app.route("/")
def main():
    return "Hello World"


@app.route("/celeb", methods=["POST"])
def add_celeb():
    content = request.get_json()
    print(content)
    print(content["handle"])
    tm = TweetManager.get_instance()
    tm.append_celebs(content["handle"])
    tm.kill_and_start()
    print("updated twitter ids", tm.watching_celeb_twitter_ids)
    logging.info("updated twitter id")
    return jsonify({"message": "success", "added": content["handle"]})


if __name__ == "__main__":

    celeb_handles = ["FaensOnly"]
    tm = TweetManager(celeb_handles)
    print("starting flask application")
    app.run(host=FLASK_HOST, port=FLASK_PORT)

    # curl -d '{"handle":"kunalb11"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5001/celeb
    # curl -d '{"handle":"realDonaldTrump"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5001/celeb