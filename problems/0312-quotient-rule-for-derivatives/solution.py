import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """

    def ddx(coeffs: list, x_in: float):
        output = 0
        for i in range (len(coeffs) - 1):
            degree = len(coeffs) - i - 1
            output += coeffs[i] * degree * x_in ** (degree - 1)
        return output

    def func(coeffs: list, x_in: float):
        output = 0
        for i in range (len(coeffs) - 1):
            degree = len(coeffs) - i - 1
            output += coeffs[i] * x_in ** (degree)
        return output + coeffs[-1]

    g_prime = ddx(g_coeffs, x)
    h_prime = ddx(h_coeffs, x)
    g_x = func(g_coeffs, x)
    h_x = func(h_coeffs, x)

    # print(g_prime, h_prime, g_x, h_x)

    return (g_prime * h_x - h_prime * g_x) / ((h_x) ** 2)
    