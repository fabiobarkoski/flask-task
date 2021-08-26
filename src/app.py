from flask import Flask
from flask import jsonify
# import the blueprint
from src.blueprint_view import distance_bp

# creating the app
app = Flask(__name__)

# registering blueprint
app.register_blueprint(distance_bp)

@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found. Please, send a request with a value'})

if __name__ == "__main__":
    app.run(debug=True)
