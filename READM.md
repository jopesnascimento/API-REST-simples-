# 📝 API de Tarefas (TODO List)

API REST completa para gerenciar tarefas, construída com Flask e persistência em JSON.

## 🚀 Funcionalidades

- ✅ Criar nova tarefa
- ✅ Listar todas as tarefas
- ✅ Marcar tarefa como concluída
- ✅ Deletar tarefa
- ✅ Persistência em arquivo JSON
- ✅ Validações de dados

## 🛠️ Tecnologias

- Python 3.x
- Flask
- JSON para persistência

## 📦 Instalação

1. Clone o repositório
2. Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o servidor:

```bash
flask run
```

A API estará disponível em `http://localhost:5000`

## 📚 Endpoints

### Listar todas as tarefas

```http
GET /tarefas
```

**Resposta:**

```json
[
  {
    "id": 1,
    "titulo": "Estudar Python",
    "concluida": false
  }
]
```

### Criar nova tarefa

```http
POST /tarefas
Content-Type: application/json

{
  "titulo": "Nova tarefa"
}
```

**Resposta:** `201 Created`

### Marcar tarefa como concluída

```http
PUT /tarefas/{id}
```

**Resposta:** `200 OK`

### Deletar tarefa

```http
DELETE /tarefas/{id}
```

**Resposta:** `204 No Content`

## 🧪 Testando

Use Thunder Client, Postman ou Insomnia para testar os endpoints.

## 📝 Estrutura do Projeto

```
.
├── app.py              # Aplicação principal
├── tarefas.json        # Banco de dados (gerado automaticamente)
├── requirements.txt    # Dependências
└── README.md          # Documentação
```

## 🎯 Próximos passos

- [ ] Adicionar autenticação
- [ ] Migrar para banco de dados SQL
- [ ] Adicionar paginação
- [ ] Criar frontend

## 👨‍💻 Autor

Seu nome - [jopesnascimento](https://github.com/jopesnascimento)
