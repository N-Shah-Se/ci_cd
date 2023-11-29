from flask import Flask, jsonify, make_response
from jsonschema import ValidationError
from routes import routes
from flask_cors import cross_origin

app = Flask(__name__)

@app.errorhandler(400)
@cross_origin(origins='*', headers={"Content-Type":"application/json"})
def bad_request(error):
	if isinstance(error.description, ValidationError):
		return make_response(jsonify({"message":"INVALID REQUEST"}), 400)
	return make_response(jsonify({"message":"INVALID_REQUEST"}),400)

app.register_blueprint(routes)

if __name__=="__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
