class Mother:
    def __init__(self):
        self._m = 1
        print("in mother")

class Father:
    def __init__(self):
        self._f = 1
        print("in father")

class Child(Mother, Father):
    def __init_(self):
        self._c = 1
        print("in child")

if __name__ == "__main__":
    c = Child()
    print(c._m)