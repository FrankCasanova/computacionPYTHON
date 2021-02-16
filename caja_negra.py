
import unittest

def suma(num1,num2):
    return num1 + num2

class Caja_Negra_Test(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num1 = 10
        num2 = 5

        resulta = suma(num1,num2)

        self.assertEqual(resulta, 15)

    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -7

        resulta = suma(num1,num2)

        self.assertEqual(resulta,-17)    
   


if __name__ == '__main__':
    unittest.main()