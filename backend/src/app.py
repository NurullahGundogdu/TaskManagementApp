from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask('Task Management App')
api = Api(app)

app.url_map.strict_slashes = False
cors = CORS(app)


initialize_routes(api)


@app.route("/", methods=['GET'])
def welcome():
    return {"status": "true"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
