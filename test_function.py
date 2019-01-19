import unittest
from app.functions import *

class Testes(unittest.TestCase):
  def test_calcula_preco(self):
    lanche = filtra_lanche(1)
    self.assertEqual(calcula_preco(lanche), 4.50)

  def test_filtro_lanche(self):
    self.assertEqual(filtra_lanche(1)['nome'], 'X-Burguer')

  def test_get_all(self):
    self.assertEqual(len(get_all_together()), 4)
  
unittest.main()