import unittest
from app.functions import calcula_preco, filtra_lanche, get_all_ingredientes, get_all_together, get_ingredientes_lanche, get_ingrediente, Promos
from app.models import Ingrediente, Lanche

class Testes(unittest.TestCase):
  def test_calcula_preco(self):
    lanche = filtra_lanche(1)
    self.assertEqual(calcula_preco(lanche), 4.50)

  def test_filtro_lanche(self):
    aux = Lanche('', [])
    aux._id = 1
    self.assertEqual(filtra_lanche(1)._id, aux._id)

  def test_get_all(self):
    self.assertEqual(len(get_all_together()), 4)

  def teste_get_all_ingredients(self):
    self.assertEqual(len(get_all_ingredientes()), 5)

  def test_get_ingredientes(self):
    lanche = filtra_lanche(1)
    self.assertEqual(len(get_ingredientes_lanche(lanche).ingredientes), 2)

  def test_get_ingrediente(self):
    self.assertEqual(get_ingrediente('Alface')._id, 0)

class TestePromos(unittest.TestCase):
  def test_light(self):
    lanche = Lanche('Teste', [])
    lanche.ingredientes.append(get_ingrediente('Alface'))
    lanche.ingredientes.append(get_ingrediente('Queijo'))
    self.assertEqual(Promos().light(lanche), True)

if __name__ == '__main__':
  unittest.main(verbosity=2)