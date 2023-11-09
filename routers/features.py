import re
from pydantic import BaseModel

def format_function(fun):
    fun = re.sub(r'\^', '**', fun)
    fun = re.sub(r'\blog\b', 'math.log10', fun)
    fun = re.sub(r'\bln\b', 'math.log', fun)
    fun = re.sub(r'\bexp\b', 'math.exp', fun)
    return fun


# Objetos
class BaseInput(BaseModel):
    fun: str 
    tol: float
    niter: int
    error: int

class IntervalInput(BaseInput):
    a: float 
    b: float

class Newton(BaseInput):
    x0: float

class FixedPoint(Newton):
    dfun: str