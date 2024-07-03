import math

class FinancialCalculations:

    @staticmethod
    def fv_simple(pv, r, n):
        return (1 + r * n) * pv

    @staticmethod
    def pv_simple(fv, r, n):
        return fv / (1 + r * n)

    @staticmethod
    def r_simple(pv, fv, n):
        return (fv / pv - 1) / n

    @staticmethod
    def fv_compound(pv, r, n):
        return pv * (1 + r) ** n

    @staticmethod
    def pv_compound(fv, r, n):
        return fv / (1 + r) ** n

    @staticmethod
    def r_compound(pv, fv, n):
        return (fv / pv) ** (1 / n) - 1

    @staticmethod
    def fv_interval(pv, r, n, m):
        return pv * (1 + r / m) ** (m * n)

    @staticmethod
    def pv_interval(fv, r, n, m):
        return fv / (1 + r / m) ** (m * n)

    @staticmethod
    def r_interval(pv, fv, n, m):
        return ((fv / pv) ** (1 / (m * n)) - 1) * m

    @staticmethod
    def fv_continuous(pv, r, n):
        return pv * math.exp(r * n)

    @staticmethod
    def pv_continuous(fv, r, n):
        return fv / math.exp(r * n)

    @staticmethod
    def r_continuous(pv, fv, n):
        return math.log(fv / pv) / n

    @staticmethod
    def fv_with_deposit(r, n, m, a):
        return (a / (r / m)) * ((1 + r / m) ** (m * n) - 1)

    @staticmethod
    def pv_with_deposit(r, n, m, a):
        return (a / (r / m)) * (1 - 1 / (1 + r / m) ** (m * n))
