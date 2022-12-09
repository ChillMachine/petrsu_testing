import unittest
from quadr_equation import Equation 



class TestEquation(unittest.TestCase):

    def setUp(self):
        self.Equation = Equation()

    def test_D_biggger_0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(1, 2, -3), [-3.0, 1.0])
    
    def test_D_eq_0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(1, -6, 9), 3)

    def test_D_less_0(self):
        self.assertEqual(self.Equation.get_results_Q_equation(3, 1, 2), 'Нет корней')

if __name__ == "__main__":
    unittest.main()
