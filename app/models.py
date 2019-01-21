from flask import jsonify

class Ingrediente():
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco
  
  def __repr__(self):
    return '<Ingrediente {}>'.format(self.nome)


class Lanche():
  def __init__(self, nome, ingredientes):
    self._id = -1
    self.nome = nome
    self.ingredientes = ingredientes

  def __repr__(self):
    return '<Lanche {}>'.format(self.nome)

  def setId(self, codigo):
    self._id = codigo

  def toJSON(self):
    return jsonify({
            "id": self._id,
            "nome": self.nome,
            "ingredientes": self.ingredientes
          })
