class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration


class IterableCollection:
    def __init__(self):
        self._items = []

    def __iter__(self):
        return Iterator(self._items)

    def add_item(self, item):
        self._items.append(item)


# Uso
collection = IterableCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

for item in collection:
    print(item)
