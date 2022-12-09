class Equation:

    def get_results_Q_equation(self, a, b, c):
        if a == 0: 
            return 'a = 0, уравнение не квадратное'
        D = b**2 - 4 * a * c
        if D < 0:
            return 'Нет корней'
        elif D == 0:
            return -b / (2 * a)
        elif D > 0:
            return sorted([(-b + D**(1/2)) / (2 * a), (-b - D**(1/2)) / (2 * a)])

