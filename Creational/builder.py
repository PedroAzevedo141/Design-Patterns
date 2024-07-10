class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)


class Builder:
    def __init__(self):
        self.product = Product()

    def produce_part_a(self):
        self.product.add("PartA")

    def produce_part_b(self):
        self.product.add("PartB")

    def produce_part_c(self):
        self.product.add("PartC")


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


# Uso
builder = Builder()
director = Director()
director.set_builder(builder)

print("Standard basic product:")
director.build_minimal_viable_product()
print(builder.product.list_parts())

print("\nStandard full featured product:")
director.build_full_featured_product()
print(builder.product.list_parts())

print("\nCustom product:")
builder.produce_part_a()
builder.produce_part_c()
print(builder.product.list_parts())
