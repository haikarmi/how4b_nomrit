import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
from colors import bcolors
from sympy import sin


def trapezoidal_rule(f, a, b, n, Upper_bound=0):
    g = sp.diff(sp.diff(f))
    g = lambdify(x, g)
    f = lambdify(x, f)
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    E = (1 / 12) * (h ** 2) * (b - a) * g(Upper_bound)
    print("max error is: ", E)


    return integral


if __name__ == '__main__':
    print(
        "the git link:https:https://github.com/haikarmi/how4b_nomrit.git\n group:Almog Babila-209477678, Hai karmi-207265687, Yagel Batito-318271863, Meril Hasid-324569714\n ")
    print("..........................................................................................")

    x = sp.symbols('x')
    f = sin(x)
    a = 0
    b = math.pi
    n = 4
    result = trapezoidal_rule(f, a, b, n, 1)
    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)
