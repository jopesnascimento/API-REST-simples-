from flask import Flask, jsonify, request
import json

#funções auxiliares
def carregar_tarefas():
    try:
        with open('tarefas.json','r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas():
    with open('tarefas.json','w') as arquivo:
        json.dump(tarefas,arquivo,indent=2)



app = Flask(__name__)
tarefas = carregar_tarefas()


#App
@app.get('/tarefas')
def lista_tarefa():
    return jsonify(tarefas)



@app.post('/tarefas')
def adicionar_tarefas():

    db = request.get_json()

    if not db or 'titulo' not in db:
        return jsonify({"erro":"Campo 'titulo' é obrigatório"}),400
    if not db['titulo'].strip():
        return jsonify({"erro":"Titulo não pode estar vazio"}),400
    if len(tarefas) ==0:
        nova_id = 1
    else:
        nova_id = tarefas[-1]["id"] + 1

    nova_tarefa = {
        "id" :nova_id,
        "titulo": db['titulo'],
        "concluida":False
    }

    tarefas.append(nova_tarefa)


    salvar_tarefas()

    return jsonify(nova_tarefa),201



@app.put('/tarefas/<int:id>')
def concluida(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["concluida"] = True
            salvar_tarefas()
            return jsonify(tarefa),200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

#Fase 2

@app.delete('/tarefas/<int:id>')
def deletar(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            salvar_tarefas()
            return '',204
    return jsonify({"erro":"Tarefa não encontrada"}),404