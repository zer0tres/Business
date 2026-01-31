from flask import jsonify
from app.api import api_bp

@api_bp.route('/hello', methods=['GET'])
def hello():
    """Endpoint de teste - Hello World"""
    return jsonify({
        'message': 'Hello from Business Suite API!',
        'version': '1.0.0',
        'status': 'operational'
    }), 200

@api_bp.route('/status', methods=['GET'])
def status():
    """Endpoint de status da API"""
    return jsonify({
        'api': 'Business Suite',
        'status': 'running',
        'environment': 'development'
    }), 200