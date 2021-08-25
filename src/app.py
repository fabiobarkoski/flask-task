from flask import Flask
# import the blueprint
from blueprint_view import distance_bp

# creating the app
app = Flask(__name__)

# registering blueprint
app.register_blueprint(distance_bp)

if __name__ == "__main__":
    app.run(debug=True)
