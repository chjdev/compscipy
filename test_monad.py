class a: pass


def f(x: a) -> a:
    return ~x


def g(x: a) -> a:
    return x ** 2


x = 1
print('f(g(x))', f(g(x)))
print('g(f(x))', g(f(x)))


def combine(x: 'def f(x: a) -> a: pass', y: 'def f(x: a) -> a: pass'):
    return lambda _: x(y(_))

print('(f ø g)(a)', combine(f, g)(x))
print('(g ø f)(a)', combine(g, f)(x))


def h(x: a) -> a:
    return 2 * x


print('(f ø (g ø h))(x)', combine(f, combine(g, h))(x))
print('((f ø g) ø h)(x)', combine(combine(f, g), h)(x))


# http://code.activestate.com/recipes/384122/
class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __rshift__(self, other):
        return self.function(other)

    def __call__(self, value1, value2):
        return self.function(value1, value2)


ø = Infix(combine)

print('(f ø (g ø h))(x)', (f |ø| (g |ø| h))(x))
print('((f ø g) ø h)(x)', ((f |ø| g) |ø| h)(x))
print('(f ø g ø h)(x)', (f |ø| g |ø| h)(x))
print('(f ø h ø g)(x)', (f |ø| h |ø| g)(x))
print('(h ø f ø g)(x)', (h |ø| f |ø| g)(x))
assert (f |ø| g |ø| h)(x) != (h |ø| g |ø| f)(x)
assert (f |ø| g |ø| h)(x) == f(g(h(x)))

from monad.TrivialMonad import Trivial, bind as trivial_bind, retrn as trivial_return


def tf(x: int) -> Trivial:
    return Trivial(f(x))


def tg(x: int) -> Trivial:
    return Trivial(g(x))


def th(x: int) -> Trivial:
    return Trivial(h(x))


programA = (lambda a: trivial_bind(th(a),
                           lambda b: trivial_bind(tg(b),
                                           lambda c: trivial_bind(tf(c),
                                                           lambda d: trivial_return(d)))))(x)
print('programA', programA())

from monad.TrivialMonad import trivial, retrn as tretrn

programB = trivial(
    th,
    tretrn,
    tg,
    tretrn,
    tretrn,
    tf)(x)

print('programB', programB())
assert programA() == programB() == f(g(h(x)))

from monad.MaybeMonad import Maybe, Just, Nothing, maybe

def mfun1(x: int) -> Maybe:
    print('mfun1', x)
    if (x % 2) == 0:
        return Just(x)
    else:
        return Nothing()

def mfun2(x: int) -> Maybe:
    print('mfun2', x)
    if (x % 3) == 0:
        return Just(x)
    else:
        return Nothing()

def mfun3(x: int) -> Maybe:
    print('mfun3', x)
    if (x % 4) == 0:
        return Just(x)
    else:
        return Nothing()


programC = maybe(
    mfun1,
    mfun2,
    mfun3)
print(programC(12)())
try:
    print(programC(11)())
except:
    print('as expected')

