"""
Módulo que testa o módulo dateconv.py

Esse módulo implementa um unit test em python. 

Mais detalhes em:
    https://docs.python.org/3/library/unittest.html

Para usar o mecanismo de unit test em python basta:

    1. Importar o módulo unittest, que é nativo do python. 
    2. Crie uma classe que herda de unittest.TestCase.
    3. Use o método assertEqual para comparar 
    valores obtidos de valores esperados. 

Para rodar, execute no terminal:
    python <nome-arquivo-de-teste>.py
    
"""
import unittest
from dateconv import convert_to_unix
from dateconv import convert_from_unix


class TestDateConv(unittest.TestCase):
    """ Test Case """

    def test_convert_to_unix_with_time(self):
        date_unix1 = convert_to_unix('2022-01-07 21:00:00')
        self.assertEqual(date_unix1, 1641600000)

        date_unix1 = convert_to_unix('2022-04-07 21:00:00')
        self.assertEqual(date_unix1, 1649376000)     

        date_unix1 = convert_to_unix('2020-02-02 21:00:00')
        self.assertEqual(date_unix1, 1580688000)             

    def test_convert_from_unix_with_time(self):
        date_str = convert_from_unix(1641600000)
        self.assertEqual(date_str, '2022-01-07 21:00:00')

        date_str = convert_from_unix(1649376000)
        self.assertEqual(date_str, '2022-04-07 21:00:00')

        date_str = convert_from_unix(1589846400)
        self.assertEqual(date_str, '2020-05-18 21:00:00')        


if __name__ == '__main__':
    unittest.main()
