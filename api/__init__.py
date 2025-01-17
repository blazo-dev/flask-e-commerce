from flask import Blueprint

# Initialize Blueprint for the API routes
api_routes_bp = Blueprint('api_routes', __name__)

# Import the route files to register the routes with the Blueprint
from .routes import users, orders, products
