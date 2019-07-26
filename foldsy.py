from collections import namedtuple

namedtuple("Kinds", "")






def kind(level=, set=None):
    return (0, 0, set if set is not None else set())


def sort(level=, ):
    return (1, kind(level=level), set())


def var(level=,  set=None):
    return (2, sort(level=level), set if set is not None else set())



def context(*vars):
    return set(vars)

def specialization():
    def impl(*vars):

        return ()



class Context:

    def __init__(self, *vars: Variable):


    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class Kind:

    def __init__(self, name, context: Context = None) -> None:
        self.name = name
        self.context = context

    def __repr__(self):
        return self.name + "::" + self.context

class Sort:

    def __init__(self, name, kind: Kind) -> None:
        self.name = name
        self.kind = kind


    def __call__(self, var_name: str) -> Variable:
        

class Variable:

    def __init__(self, name, sort: Sort) -> None:
        self.name = name
        self.sort = sort




class Spec:

    def __call__(self, fun):

        def wrapper(self, *args, **kwargs ):

            assert args in context
            assert kwargs in context

            # function implementation is left to implementer... must be a function !
            result = fun(*args, **kwargs)

            assert result in context



