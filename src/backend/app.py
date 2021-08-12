import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)


def get_from_mongo():

    mongo_host = os.environ.get("MONGO_HOST", "mongo")
    mongo_port = int(os.environ.get("MONGO_PORT", 27017))
    mongo_user = os.environ.get("MONGO_USER", "root")
    mongo_pass = os.environ.get("MONGO_PASSWORD", "root")

    mongo_db = os.environ.get("MONGO_DB", "test")
    mongo_coll = os.environ.get("MONGO_COLLECTION", "test")

    client = MongoClient( mongo_host, mongo_port, username=mongo_user, password=mongo_pass)
    
    db = client[mongo_db]
    collection = db[mongo_coll] 
    cur = collection.find()
    try:
        text_value = cur[0]["value"]
    except:
        text_value = "Erro ao acesso registro no mongo"
    
    return text_value


@app.route('/mongo')
def get_from_mongo_route():
    return {"data": get_from_mongo(), "status":200}

if __name__ == "__main__":
    app.run(host=os.environ.get("APP_HOST", "0.0.0.0"), port= os.environ.get("APP_PORT", "9000"), debug=1)