import unittest

from carro import Motor

class teste_carro(unittest.TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()        
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

unittest.main()