from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from config import Config
from flask_cors import CORS
from api.routes import api_routes_bp

# -----------------------------------
# Initialize the Flask application
# -----------------------------------
app = Flask(__name__)

# Apply the configurations to the app
app.config.from_object(Config)

CORS(app)


@app.route('/')
def home():
    """
    Basic route to test if Flask is running correctly.
    Returns:
        - A JSON response with a message confirming Flask is working.
    """
    return {"message": "Flask is working correctly!"}


# Initialize SQLAlchemy and JWT for the app
db = SQLAlchemy(app)
jwt = JWTManager(app)

app.register_blueprint(api_routes_bp, url_prefix='/api')

# Ensure all tables defined in models are created in the database
with app.app_context():
    db.create_all()
    print("Tables created successfully!")




if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
