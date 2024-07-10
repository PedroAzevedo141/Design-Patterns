import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype1(Prototype):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return f"ConcretePrototype1: {self.field}"


class ConcretePrototype2(Prototype):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return f"ConcretePrototype2: {self.field}"


# Uso
prototype1 = ConcretePrototype1("Value1")
clone1 = prototype1.clone()
print(clone1)

prototype2 = ConcretePrototype2("Value2")
clone2 = prototype2.clone()
print(clone2)
