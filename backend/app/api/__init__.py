from flask import Blueprint

# Criar blueprint da API
api_bp = Blueprint('api', __name__)

# Importar rotas (vamos criar depois)
from app.api import routes