from flask import Flask, jsonify, request

app = Flask(__name__)
tarefas = [{"id":1, "titulo": "Estudar inglês", "concluida":True},
           {"id":2, "titulo": "Estudar Matemática", "concluida":True},
           {"id":3, "titulo": "Lavar o banheiro", "concluida":False}]


#App
@app.get('/tarefas')
def lista_tarefa():
    return jsonify(tarefas)

@app.post('/tarefas')
def adicionar_tarefas():

    db = request.get_json()
    nova_id = tarefas[-1]["id"] + 1

    nova_tarefa = {
        "id" :nova_id,
        "titulo": db['titulo'],
        "concluida":False
    }

    tarefas.append(nova_tarefa)

    return jsonify(nova_tarefa),201

@app.put('/tarefas/<int:id>')
def concluida(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["concluida"] = True
            return jsonify(tarefa),200

    return jsonify({"erro": "Tarefa não encontrada"}), 404