import unittest

from factorial import factorial_no_recursivo, factorial_recursivo
from fibonacci import fibonacci_no_recursivo, fibonacci_recursivo

class Test_factorial_no_recursivo(unittest.TestCase):
    def test_5(self):
        resultado = factorial_no_recursivo(5)
        self.assertEqual(resultado,120)
    
    def test_10(self):
        resultado = factorial_no_recursivo(10)
        self.assertEqual(resultado, 3628800)
    
    def test_3(self):
        resultado = factorial_no_recursivo(3)
        self.assertEqual(resultado, 6)

    def test_7(self):
        resultado = factorial_no_recursivo(7)
        self.assertEqual(resultado, 5040)


class Test_factorial(unittest.TestCase):
    def test_5(self):
        resultado = factorial_recursivo(5)
        self.assertEqual(resultado, 120)

    def test_8(self):
        resultado = factorial_recursivo(8)
        self.assertEqual(resultado, 40320)

    def test_6(self):
        resultado = factorial_recursivo(6)
        self.assertEqual(resultado, 720)

    def test_4(self):
        resultado = factorial_recursivo(4)
        self.assertEqual(resultado, 24)


class Test_fibonacci_no_recursivo(unittest.TestCase):
    def test_12(self):
        resultado = fibonacci_no_recursivo(12)
        self.assertEqual(resultado, 144)

    def test_10(self):
        resultado = fibonacci_no_recursivo(10)
        self.assertEqual(resultado, 55)

    def test_5(self):
        resultado = fibonacci_no_recursivo(5)
        self.assertEqual(resultado, 5)

    def test_7(self):
        resultado = fibonacci_no_recursivo(7)
        self.assertEqual(resultado, 13)

class Test_fibonacci_recursivo(unittest.TestCase):
    def test_9(self):
        resultado = fibonacci_recursivo(9)
        self.assertEqual(resultado, 34)
 
    def test_5(self):
        resultado = fibonacci_recursivo(5)
        self.assertEqual(resultado, 5)

    def test_11(self):
        resultado = fibonacci_recursivo(11)
        self.assertEqual(resultado, 89)

    def test_12(self):
        resultado = fibonacci_recursivo(12)
        self.assertEqual(resultado, 144)

    def test_7(self):
        resultado = fibonacci_recursivo(7)
        self.assertEqual(resultado, 13)

if __name__ == '__main__':
    unittest.main()
