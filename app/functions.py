from app.models import Ingrediente, Lanche
import json
import pprint as pp

def calcula_preco(lanche):
  preco = 0
  for ing in lanche.ingredientes:
    preco += ing.preco

  return preco

def get_ingredientes_lanche(lanche):
  aux = []
  with open('mocks/mock-ingredientes.json', 'r') as f:
    ingredientes = json.load(f)
    for ingrediente in ingredientes:
      for ing in lanche.ingredientes:
        if ingrediente['id'] == ing:
          aux.append(Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco']))
  lanche.ingredientes = aux
  return lanche

def filtra_lanche(id):
  with open('mocks/mock-lanches.json', 'r') as f:
    lanches = json.load(f)
    for lanche in lanches:
      if lanche['id'] == id:
        aux = Lanche(lanche['nome'], lanche['ingredientes'])
        aux._id = lanche['id']
        return aux

  return None

def get_all_together():
  data = []
  with open('mocks/mock-lanches.json', 'r') as l:
    lanches = json.load(l)
  with open('mocks/mock-ingredientes.json', 'r') as i:
    ingredientes = json.load(i)

  for lanche in lanches:
    auxI = []
    aux = Lanche(lanche['nome'], lanche['ingredientes'])
    aux._id = lanche['id']
    for ingrediente in ingredientes:
      for ing in lanche['ingredientes']:
        if ingrediente['id'] == ing:
          auxI.append(Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco']))
    aux.ingredientes = auxI
    data.append(aux)

  return data

def get_all_ingredientes():
  datas = []
  with open('mocks/mock-ingredientes.json', 'r') as f:
    data = json.load(f)
    for ingrediente in data:
      aux = Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco'])
      datas.append(aux)
  return datas

def get_ingrediente(nome):
  with open('mocks/mock-ingredientes.json', 'r') as f:
    ingredientes = json.load(f)
    for ingrediente in ingredientes:
      if ingrediente['nome'] == nome:
        return Ingrediente(ingrediente['id'], ingrediente['nome'], ingrediente['preco'])
  return None


class Promos():
  def light(self, lanche, preco):
    lanche = lanche.toJSON()
    alface = get_ingrediente('Alface').toJSON()
    bacon = get_ingrediente('Bacon').toJSON()
    if alface in lanche['ingredientes'] and bacon not in lanche['ingredientes']:
      return preco * 0.1
    else:
      return 0

  def too_much(self, lanche, nome):
    count = 0
    ing = get_ingrediente(nome)
    for ingrediente in lanche.ingredientes:
      if ingrediente.nome == nome:
        count += 1
    if count // 3 > 0:
      div = count // 3
      return ing.preco * div
    else:
      return 0