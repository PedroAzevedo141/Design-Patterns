from typing import List


class Component:
    def operation(self) -> str:
        pass

    def add(self, component: "Component") -> None:
        pass

    def remove(self, component: "Component") -> None:
        pass

    def is_composite(self) -> bool:
        return False


class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    def __init__(self) -> None:
        self.children: List[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


# Uso
simple = Leaf()
print(f"Client: I've got a simple component:\n{simple.operation()}")

tree = Composite()
branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

branch2 = Composite()
branch2.add(Leaf())

tree.add(branch1)
tree.add(branch2)
print(f"Client: Now I've got a composite tree:\n{tree.operation()}")
