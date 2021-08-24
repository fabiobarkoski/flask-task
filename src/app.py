from flask import Flask
#import the blueprint
from blueprint_view import distance_bp

app = Flask(__name__)

#blueprints
app.register_blueprint(distance_bp)

if __name__ == "__main__":
    app.run()