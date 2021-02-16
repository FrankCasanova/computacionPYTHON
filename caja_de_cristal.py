import unittest
from unittest import result

def mayor_de_edad(edad):
    return edad >= 18

class Caja_De_Cristal(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado,True)

    def test_es_menor_de_edad(self):
        edad = 17

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado,False)    

if __name__ == '__main__':
    unittest.main()