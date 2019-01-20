from flask import render_template, jsonify, request
from app import app, functions
import json
import pprint as pp

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
  return render_template('index.html', title='Lanches', lanches=functions.get_all_together())

@app.route('/lanche/<codigo>', methods=['GET', 'POST'])
def lanche(codigo):
  lanche = functions.filtra_lanche(int(codigo))
  if request.method == 'GET':
    preco = functions.calcula_preco(lanche)
    lanche = functions.get_ingredientes_lanche(lanche)
    return render_template('lanche.html', title='Lanche escolhido', 
            lanche=lanche, ingredientes=functions.get_all_ingredientes(),
            preco=preco)
  else:
    data = request.get_json()
    if len(data) > 0:
      for extra in data:
        lanche['ingredientes'].append(int(extra))
    preco = functions.calcula_preco(lanche)
    lanche = functions.get_ingredientes_lanche(lanche)
    return jsonify({ "lanche": lanche, "preco": preco })


@app.route('/<codigo>', methods=['GET'])
def ingrediente(codigo):
  lanche = functions.filtra_lanche(int(codigo))
  preco = functions.calcula_preco(lanche)
  return jsonify({ "lanche": lanche, "preco": preco })