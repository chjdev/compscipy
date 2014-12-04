from functools import singledispatch

from .Monad import do_block as _do_block


class Maybe():
    pass


class Just(Maybe):
    def __init__(self, value):
        self._value = value

    def __call__(self, *args, **kwargs):
        return self._value


class Nothing(Maybe):
    pass


@singledispatch
def bind(what: Just, other: 'def f(a) -> Trivial: pass') -> Maybe:
    return other(what())


@bind.register(Nothing)
def bind_nothing(what: Nothing, _) -> Nothing:
    return what


def retrn(value) -> Maybe:
    return Just(value)


def maybe(*stmts):
    return _do_block(bind, *stmts)


if __name__ == '__main__':
    pass
