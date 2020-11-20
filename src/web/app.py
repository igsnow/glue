from bson import json_util
from flask import Flask
from flask_pymongo import PyMongo
import json

from src.web.config.db import MONGODB_CONF

app = Flask(__name__)
app.config['DEBUG'] = True

mongo = PyMongo(app,
                uri=f"mongodb://{MONGODB_CONF['userName']}:{MONGODB_CONF['pwd']}@{MONGODB_CONF['host']}:{MONGODB_CONF['port']}/{MONGODB_CONF['dbName']}")  # 开启数据库实例


@app.route('/get_list')
def query_list():
    data = mongo.db.details.find({})
    print(data)
    result = []
    for i in data:
        result.append(i)

    if data:
        res = {
            'results': result,
            'msg': 'success',
            'total': len(result)
        }
        return json.loads(json_util.dumps(res))
    else:
        return 'No user found!'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8088)
