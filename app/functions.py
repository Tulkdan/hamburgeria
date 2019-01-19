import json
import pprint as pp

def calcula_preco(lanche):
  preco = 0
  with open('mocks/mock-ingredientes.json', 'r') as f:
    ingredientes = json.load(f)
    for ingrediente in ingredientes:
      for ing in lanche['ingredientes']:
        if ingrediente['id'] == ing:
          preco += ingrediente['preco']
  
  return preco


def filtra_lanche(id):
  with open('mocks/mock-lanches.json', 'r') as f:
    lanches = json.load(f)
    for lanche in lanches:
      if lanche['id'] == id:
        return lanche

  return None

def get_all_together():
  data = []
  with open('mocks/mock-lanches.json', 'r') as l:
    lanches = json.load(l)
  with open('mocks/mock-ingredientes.json', 'r') as i:
    ingredientes = json.load(i)

  for lanche in lanches:
    auxI = []
    aux = lanche
    for ingrediente in ingredientes:
      for ing in lanche['ingredientes']:
        if ingrediente['id'] == ing:
          auxI.append(ingrediente)
    aux['ingredientes'] = auxI
    data.append(aux)

  return data
