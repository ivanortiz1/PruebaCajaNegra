import unittest
from clases import Suma, Resta, Multiplicacion

class TestOperaciones(unittest.TestCase):

    def test_suma(self):
        print("Iniciando test de suma...")
        suma = Suma()
        resultado = suma.sumar(2, 3)
        self.assertEqual(resultado, 5)
        print("Test de suma finalizado correctamente.")
        

    def test_resta(self):
        print("Iniciando test de resta...")
        resta = Resta()
        resultado = resta.restar(5, 3)
        self.assertEqual(resultado, 2)
        print("Test de resta finalizado correctamente.")

    def test_multiplicacion(self):
        print("Iniciando test de multiplicacion...")
        multiplicacion = Multiplicacion()
        resultado = multiplicacion.multiplicar(2, 3)
        self.assertEqual(resultado, 6)
        print("Test de multiplicacion finalizado correctamente.")

if __name__ == '__main__':
    unittest.main()
