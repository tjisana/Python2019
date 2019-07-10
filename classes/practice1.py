class Employee:
    raise_amt = 1

    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
        self._full_name = "{} {}".format(fn, ln)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        return cls(*emp_str.split('-'))

    def __repr__(self):
        return "Employee('{}', '{}')".format(self.fn, self.ln)

    def __str__(self):
        return "First name: {}, Last name: {}".format(self.fn, self.ln)


class Developer(Employee):
    pass


if __name__ == '__main__':
    e = Employee("e-FN", "e-LN")
    print("Employee.raise_amt : {} e.raise_amt : {}".format(Employee.raise_amt, e.raise_amt))  # prints 1 1
    e.raise_amount = 2
    print("Employee.raise_amt : {} e.raise_amt : {}".format(Employee.raise_amt, e.raise_amt))  # prints 1 1
    e.raise_amt = 3
    print("Employee.raise_amt : {} e.raise_amt : {}".format(Employee.raise_amt, e.raise_amt))  # prints 1 3
    print(e.__dict__)  # prints {'fn': 'e1', 'raise_amount': 2, 'raise_amt': 3}

    # using classmethod as alternate constructor
    emp_str = 'John-Doe'
    e1 = Employee.from_string(emp_str)
    print(e1.__dict__)

    #  print(help(Developer)) printing help function output gives good information about a class.
    #  especially the method resolution order.
    print(e.full_name)
    print(help(Employee))
