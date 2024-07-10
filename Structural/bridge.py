class Implementation:
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (
            f"Abstraction: Base operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (
            f"ExtendedAbstraction: Extended operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


# Uso
implementation_a = ConcreteImplementationA()
abstraction = Abstraction(implementation_a)
print(abstraction.operation())

implementation_b = ConcreteImplementationB()
extended_abstraction = ExtendedAbstraction(implementation_b)
print(extended_abstraction.operation())
