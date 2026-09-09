import unittest
from multiplicacao import multiplicar

class TesteMultiplicacao(unittest.TestCase):
    def test_tipo_errado_1(self):
        self.assertRaises(TypeError, multiplicar, 'a', 3)

    def test_tipo_errado_2(self):
        self.assertRaises(TypeError, multiplicar, 4, '3')

    def test_valor_errado_1(self):
        self.assertRaises(ValueError, multiplicar, 0, 5)

    def test_valor_errado_2(self):
        self.assertRaises(ValueError, multiplicar, 3, -9)

    def test_multiplicacao_inteiro(self):
        self.assertEqual(multiplicar(5, 2), 10)

    def test_multiplicacao_float(self):
        self.assertEqual(multiplicar(1.5, 1.5), 2.25)

    def test_multiplicacao_int_e_float(self):
        self.assertEqual(multiplicar(2, 1.5), 3)


if __name__ == '__main__':
    unittest.main()