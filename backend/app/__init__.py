from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config

# Inicializar extensões
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_name='default'):
    """Factory para criar a aplicação Flask"""
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar extensões com a app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Registrar blueprints (rotas)
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Rota de health check
    @app.route('/health')
    def health():
        return {'status': 'ok', 'message': 'Business Suite API is running'}, 200
    
    return app