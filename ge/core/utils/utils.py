import sys
import importlib

def get_problem_class(classname):
    m = importlib.import_module('ge.problems.' + classname.lower())
    return getattr(m, classname)
    