class Strategy:
    def do_algorithm(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return sorted(data, reverse=True)


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


# Uso
context = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
context.do_some_business_logic()

print("\nClient: Strategy is set to reverse sorting.")
context.set_strategy(ConcreteStrategyB())
context.do_some_business_logic()
