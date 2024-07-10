from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


# Uso
creator_a = ConcreteCreatorA()
print(creator_a.some_operation())

creator_b = ConcreteCreatorB()
print(creator_b.some_operation())
