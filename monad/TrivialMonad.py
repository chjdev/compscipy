from .Monad import do_block as _do_block


class Trivial():
    def __init__(self, value):
        self._value = value

    def __call__(self, *args, **kwargs):
        return self._value


def bind(what: Trivial, other: 'def f(a) -> Trivial: pass') -> Trivial:
    return other(what())


def retrn(value) -> Trivial:
    return Trivial(value)


def trivial(*stmts):
    return _do_block(bind, *stmts)


if __name__ == '__main__':
    pass
