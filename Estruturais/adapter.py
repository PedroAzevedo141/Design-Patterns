class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


# Uso
def client_code(target: Target) -> None:
    print(target.request())


adaptee = Adaptee()
adapter = Adapter(adaptee)
print("Client: I can work just fine with the Adapter object:")
client_code(adapter)
