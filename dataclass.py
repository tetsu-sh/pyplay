from dataclasses import dataclass
from typing import Protocol
from enum import Enum

@dataclass(frozen=True)
class ChimDataClass(Protocol):
    pass

class FoodType(Enum):
    FISH=1
    CHIKIN=2

@dataclass(frozen=True)
class Kuu(ChimDataClass):
    name:str
    id:str

    def jump(self,distance:int)->bool:
        if distance<3:
            return True
        else:
            return False

    def eat(self,food:FoodType):
        match food:
            case FoodType.FISH:
                print("I like it")
            case FoodType.CHIKIN:
                print("yammy")
            case _:
                print("error")


def main():
    kuu=Kuu(name="str",id="ddd")
    kuu.id="aaa"
    print(kuu)


if __name__=="__main__":
    main()