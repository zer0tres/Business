#  Setup do Projeto - Business Suite

Guia completo para configurar e rodar o projeto localmente.

---

##  Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop/)
- **Git** - [Download](https://git-scm.com/)

---

## 🔧 Instalação

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/business-suite.git
cd business-suite
```

### 2️⃣ Configurar Backend
```bash
# Entrar na pasta backend
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# Criar arquivo .env
cp .env.example .env
```

### 3️⃣ Subir Banco de Dados (Docker)
```bash
# Voltar para raiz do projeto
cd ..

# Subir containers PostgreSQL e Redis
docker-compose up -d

# Verificar se estão rodando
docker ps
```

### 4️⃣ Inicializar Banco de Dados
```bash
cd backend

# Criar tabelas e usuário admin
python init_db.py
```

**Credenciais do Admin:**
- Email: `admin@business.com`
- Senha: `admin123`

### 5️⃣ Rodar Servidor
```bash
# Com ambiente virtual ativado
python run.py
```

Servidor rodando em: `http://localhost:5000`

---

##  Verificar Instalação

Teste os endpoints:
```bash
# Health check
curl http://localhost:5000/health

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@business.com", "password": "admin123"}'
```

Se retornar um token JWT, está tudo funcionando! ✅

---

##  Workflow Diário
```bash
# 1. Entrar na pasta do backend
cd backend

# 2. Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Garantir que Docker está rodando
docker ps

# 4. Se Docker não estiver rodando:
cd ..
docker-compose up -d
cd backend

# 5. Rodar servidor
python run.py
```

---

##  Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'flask'"
**Solução:** Ative o ambiente virtual primeiro!
```bash
source venv/bin/activate
```

### Erro: "Connection refused" ao conectar no banco
**Solução:** Verifique se os containers Docker estão rodando
```bash
docker ps
docker-compose up -d
```

### Erro: "Port 5000 already in use"
**Solução:** Mate o processo na porta 5000
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID  /F
```

---

##  Próximos Passos

- [API Documentation](API.md) - Endpoints disponíveis
- [Development Guide](DEVELOPMENT.md) - Guia de desenvolvimento
- [Architecture](ARCHITECTURE.md) - Arquitetura do sistema