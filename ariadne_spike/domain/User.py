class User:

    def __init__(self, name, age):
        self.name = name if name is not None else "stranger"
        self.age = age if age is not None else 18
