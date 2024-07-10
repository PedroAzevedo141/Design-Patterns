class Command:
    def execute(self):
        pass


class SimpleCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(
            f"SimpleCommand: See, I can do simple things like printing ({self._payload})"
        )


class ComplexCommand(Command):
    def __init__(self, receiver, a, b):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print("ComplexCommand: Complex stuff should be done by a receiver object.")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    def do_something(self, a):
        print(f"Receiver: Working on ({a})")

    def do_something_else(self, b):
        print(f"Receiver: Also working on ({b})")


class Invoker:
    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


# Uso
invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))

invoker.do_something_important()
