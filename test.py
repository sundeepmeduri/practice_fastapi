
class Car:

    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name


c1 = Car(1, 'Honda')
print(c1.id, c1.name)