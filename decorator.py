from functools import wraps
from typing import Callable, Generic, NamedTuple, ParamSpec, TypeVar, cast

R = TypeVar("R", bound=str)
P = ParamSpec("P")


def with_good_morning(f: Callable[P, R]) -> Callable[P, R]:
    @wraps(f)
    def wrapper(*args: P.arg, **kwargs: P.kwargs) -> R:
        print("Hellow World!")
        return f(*args, **kwargs)

    return wrapper


@with_good_morning
def greet(*greets: str) -> None:
    """greeting"""
    for g in greets:
        print(g)
    print("Good Night")


@with_good_morning
def greet_(afternoon: str, evening: str) -> None:
    print(afternoon)
    print(evening)
    print("Good Night")


class N(NamedTuple):
    """test named tuple"""

    name: str


K = TypeVar("K")
L = TypeVar("L")


class C(Generic[L, K]):
    pass


I = TypeVar("I", bound=int)

greet("hello", "good evening")
greet_(afternoon="goodafternoo", evening="good evening")
tuple = N(name="chimu")


def plus(a: I, b: I) -> I:
    return cast(I, a + b)
