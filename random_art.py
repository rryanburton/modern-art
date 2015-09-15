import random
from math import *
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

# sin = math.sin
# cos = math.cos
# tan = math.tan
# pi = math.pi
def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr1 = lambda x, y: sin(x) + cos(y) + sin(x) + cos(sin(tan(x)))
    expr2 = lambda x, y: cos(tan(y))
    expr3 = lambda x, y: sin(y) + cos(x) + sin(x) + cos(sin(tan(y)))
    return random.choice([expr1, expr2, expr3])
#
# res = []
#
# for _ in range(random.randint)


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
