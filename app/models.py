class Ingrediente():
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco
  
  def __repr__(self):
    return '<Ingrediente {}>'.format(self.nome)
