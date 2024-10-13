from Person import Person

class Person(Person):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def dispaly(self):
        print(self.name)
        print(self.weight)


if __name__ == '__main__':
    obj = Person("jaga", 80)
    obj.dispaly()
