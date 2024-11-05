from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = "/swagger"  # Swagger UI URL
API_URL = "/static/customer_service.swagger.json"  # Path to your Swagger JSON file

# Swagger UI setup
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "gRPC Python Microservice"},  # Swagger UI config overrides
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(port=8080)
