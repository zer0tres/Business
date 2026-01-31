# Development Guide - Business Suite

Guia para desenvolvedores contribuindo com o projeto.

---

## 🏗️ Estrutura do Projeto
```
Business/
├── backend/
│   ├── app/
│   │   ├── __init__.py          # Factory da aplicação
│   │   ├── api/                 # Endpoints da API
│   │   │   ├── auth.py          # Login/Register
│   │   │   ├── customers.py     # CRUD Clientes
│   │   │   └── routes.py        # Rotas gerais
│   │   ├── models/              # Modelos do banco
│   │   │   ├── user.py
│   │   │   ├── company.py
│   │   │   └── customer.py
│   │   └── schemas/             # Validação
│   │       ├── auth.py
│   │       └── customer.py
│   ├── config.py                # Configurações
│   ├── run.py                   # Entrypoint
│   └── init_db.py               # Setup do banco
├── docs/                        # Documentação
├── frontend/                    # (Em desenvolvimento)
└── docker-compose.yml           # Containers
```

---

## 🔄 Workflow de Desenvolvimento

### 1. Criar uma nova feature
```bash
# Criar branch
git checkout -b feature/nome-da-feature

# Desenvolver...

# Commit
git add .
git commit -m "feat: descrição da feature"

# Push
git push origin feature/nome-da-feature
```

### 2. Padrão de Commits

Usamos **Conventional Commits:**

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `refactor:` Refatoração
- `test:` Testes
- `chore:` Manutenção

**Exemplos:**
```
feat: adiciona endpoint de agendamentos
fix: corrige validação de email
docs: atualiza README com exemplos
```

---

## 🗄️ Trabalhando com o Banco de Dados

### Criar novo modelo

1. Criar arquivo em `app/models/`
2. Definir classe herdando de `db.Model`
3. Adicionar em `app/models/__init__.py`
4. Criar tabela:
```bash
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

### Acessar banco via Docker
```bash
# Conectar ao PostgreSQL
docker exec -it business_suite_db psql -U postgres -d business_suite

# Comandos úteis:
\dt              # Listar tabelas
\d users         # Descrever tabela
SELECT * FROM users;
\q               # Sair
```

---

## 🧪 Testando Endpoints

### Com cURL
```bash
# Salvar token
TOKEN="seu_token_aqui"

# GET
curl -X GET http://localhost:5000/api/customers \
  -H "Authorization: Bearer $TOKEN"

# POST
curl -X POST http://localhost:5000/api/customers \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Teste", "phone": "123456789"}'
```

### Com Postman/Insomnia

1. Criar collection "Business Suite"
2. Adicionar variável `{{base_url}}` = `http://localhost:5000/api`
3. Fazer login e salvar token
4. Adicionar token em Headers: `Authorization: Bearer {{token}}`

---

## 📝 Adicionando Novo Endpoint

### Exemplo: Criar endpoint de produtos

**1. Criar modelo (`app/models/product.py`):**
```python
from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
```

**2. Criar rotas (`app/api/products.py`):**
```python
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.api import api_bp
from app.models.product import Product

@api_bp.route('/products', methods=['GET'])
@jwt_required()
def list_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products]), 200
```

**3. Registrar em `app/api/__init__.py`:**
```python
from app.api import routes, auth, customers, products
```

**4. Criar tabela:**
```bash
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

---

## 🐛 Debug

### Ver logs do servidor
```bash
python run.py
# Logs aparecem no terminal
```

### Debug no VSCode
Criar `.vscode/launch.json`:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Flask",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/backend/run.py",
      "console": "integratedTerminal"
    }
  ]
}