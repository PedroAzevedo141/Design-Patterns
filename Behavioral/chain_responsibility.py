class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)


class ConcreteHandler1(Handler):
    def handle(self, request):
        if 0 < request <= 10:
            print(f"ConcreteHandler1 handled request {request}")
        else:
            super().handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request):
        if 10 < request <= 20:
            print(f"ConcreteHandler2 handled request {request}")
        else:
            super().handle(request)


class ConcreteHandler3(Handler):
    def handle(self, request):
        if 20 < request <= 30:
            print(f"ConcreteHandler3 handled request {request}")
        else:
            super().handle(request)


# Uso
h1 = ConcreteHandler1()
h2 = ConcreteHandler2()
h3 = ConcreteHandler3()

h1._successor = h2
h2._successor = h3

requests = [5, 14, 22, 18, 3, 27]
for request in requests:
    h1.handle(request)
