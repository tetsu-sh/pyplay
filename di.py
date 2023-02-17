from injector import Injector


class Dependency:
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder):
        pass

    def resolve(self, cls):
        return self.injector.get(cls)
