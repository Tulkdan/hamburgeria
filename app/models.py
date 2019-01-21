class Ingrediente():
  def __init__(self, _id, nome, preco):
    self._id = _id
    self.nome = nome
    self.preco = preco
  
  def __repr__(self):
    return '<Ingrediente {}>'.format(self.nome)
  
  def toJSON(self):
    return {
      "id": self._id,
      "nome": self.nome,
      "preco": self.preco
    }


class Lanche():
  def __init__(self, nome, ingredientes):
    self._id = -1
    self.nome = nome
    self.ingredientes = ingredientes

  def __repr__(self):
    return '<Lanche {}>'.format(self.nome)

  def setId(self, codigo):
    self._id = codigo

  def add_ingrediente(self, ingrediente):
    self.ingredientes.append(ingrediente)

  def toJSON(self):
    ingredientes = []
    for x in self.ingredientes:
      ingredientes.append(x.toJSON())
    return {
            "id": self._id,
            "nome": self.nome,
            "ingredientes": ingredientes
          }
