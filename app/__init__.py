from flask import Flask
from dotenv import load_dotenv
load_dotenv()

def create_app():
    flask_app = Flask(__name__)

    from app.routes.main_routes import bp as main_bp
    from app.routes.stock_routes import bp as stock_bp
    flask_app.register_blueprint(main_bp)
    flask_app.register_blueprint(stock_bp)

    return flask_app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(debug=True)

