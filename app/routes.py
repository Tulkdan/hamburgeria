from flask import render_template, jsonify, request, redirect, url_for, session
from app import app, functions, models
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
    lanche = functions.get_ingredientes_lanche(lanche)
    preco = functions.calcula_preco(lanche)
    return render_template('lanche.html', title='Lanche escolhido', 
            lanche=lanche, ingredientes=functions.get_all_ingredientes(),
            preco=preco)
  else:
    data = request.get_json()
    if len(data) > 0:
      for extra in data:
        lanche.ingredientes.append(int(extra))
    lanche = functions.get_ingredientes_lanche(lanche)
    preco = functions.calcula_preco(lanche)
    session['lanche'] = lanche.toJSON()
    session['preco'] = preco
    return redirect(url_for('finalizar'))

'''
@app.route('/<codigo>', methods=['GET'])
def ingrediente(codigo):
  lanche = functions.filtra_lanche(int(codigo))
  preco = functions.calcula_preco(lanche)
  return jsonify({ "lanche": lanche, "preco": preco })
'''

@app.route('/finalizar', methods=['GET'])
def finalizar():
  aux = session.get('lanche', None)
  preco = session.get('preco', None)
  lanche = models.Lanche(aux['nome'], [])
  for ingrediente in aux['ingredientes']:
    lanche.add_ingrediente(models.Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco']))
  promos = functions.Promos()
  desconto = 0
  desconto += promos.light(lanche, preco)
  desconto += promos.too_much(lanche, 'Hambúrguer de carne')
  desconto += promos.too_much(lanche, 'Queijo')
  desconto = round(desconto, 2)
  if desconto > 0:
    preco = preco - desconto
  return render_template('finalizado.html', title=lanche.nome,
          lanche=lanche, preco=preco, desconto=desconto)

@app.route('/montar', methods=['GET', 'POST'])
def montar():
  if request.method == 'GET':
    ingredientes = functions.get_all_ingredientes()
    return render_template('montar.html', title='Montar lanche', ingredientes=ingredientes)
  else:
    data = request.get_json()
    ingredientes = list(map(lambda x: int(x), data))
    lanche = models.Lanche('', ingredientes)
    lanche = functions.get_ingredientes_lanche(lanche)
    preco = functions.calcula_preco(lanche)
    session['lanche'] = lanche.toJSON()
    session['preco'] = preco
    return redirect(url_for('finalizar'))

@app.route('/logout', methods=['GET'])
def logout():
  for key in session.keys():
    session.pop(key)
    return redirect(url_for('index'))
