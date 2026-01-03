# API de Tarefas (TODO List)

API REST simples para gerenciar tarefas, construída com Flask.

## Funcionalidades

- Listar todas as tarefas
- Criar nova tarefa
- Marcar tarefa como concluída

## Como rodar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o servidor:

```bash
flask run
```

3. Acesse: `http://localhost:5000/tarefas`

## Endpoints

- `GET /tarefas` - Lista todas as tarefas
- `POST /tarefas` - Cria nova tarefa
- `PUT /tarefas/<id>` - Marca tarefa como concluída
    