import unittest
from quadr_equation import Equation 



class TestEquation(unittest.TestCase):

    def setUp(self):
        self.Equation = Equation()

    #Все случаи с аргументами != 0

    def test_D_biggger_0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(1, 2, -3), [-3.0, 1.0])
    
    def test_D_eq_0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(1, -6, 9), 3)

    def test_D_less_0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(3, 1, 2), 'Нет корней')

    #Аргументы 0

    def test_a0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(0, 1, 2), 'a = 0, уравнение не квадратное')
    
    def test_b0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(2, 0, -2), [-1.0, 1.0])

    def test_b0_c0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(a = 1, b = 0, c = 0), 0.0)

    def test_c0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(a = 2, b = 4, c = 0), [-2.0, 0.0])

    def test_c0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(0, 0, 0), 'a = 0, уравнение не квадратное')

    #_________________________________________________________________________________

  
if __name__ == "__main__":
    unittest.main()