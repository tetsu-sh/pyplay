from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol


@dataclass(frozen=True)
class ChimDataClass(Protocol):
    pass


class FoodType(Enum):
    FISH = auto()
    CHIKIN = auto()


@dataclass(frozen=True)
class Kuu:
    name: str
    id: str

    def jump(self, distance: int) -> bool:
        if distance < 3:
            return True
        else:
            return False

    def eat(self, food: FoodType) -> None:
        match food:
            case FoodType.FISH:
                print("I like it")
            case FoodType.CHIKIN:
                print("yammy")
            case _:
                print("error")


@dataclass(frozen=True)
class Chim:
    name: str
    id: str

    def eat(self, food: FoodType) -> None:
        match food:
            case FoodType.FISH:
                print("chim yammy")
            case FoodType.CHIKIN:
                print("no")

    def jump(self, distance: int) -> bool:
        return False


class Cat(Protocol):
    def jump(self, distance: int) -> bool:
        ...

    def eat(self, food: FoodType) -> None:
        ...
from typing import TypeVar

T=TypeVar("T",bound=int)

def calc(a:T,b:T)->T:
    return a+b

def morning(cat: Cat) -> None:
    cat.eat(FoodType.FISH)

    cat.jump(3)


def main() -> None:
    kuu = Kuu(name="str", id="ddd")
    print(kuu)
    kuu.eat(food=FoodType.CHIKIN)
    chim = Chim(name="chim", id="1")
    morning(chim)


if __name__ == "__main__":
    main()
