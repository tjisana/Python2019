class Stack:
    def __init__(self):
        self._data = list()
    
    def push(self, obj):
        self._data.append(obj)

    def pop(self):
        if self._data:
            return self._data.pop()
        return None

    def peek(self):
        return self._data[-1] if self._data else None

    def size(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self._data)

def linter(inputs):
    if not input:
        return True

    closers = {'(': ')', '{': '}', '[' : ']'}
    s = Stack()

    for c in inputs:
        if c in closers.keys():
            s.push(c)
        else:
            if s.is_empty():
                return False
            else:
                if closers[s.pop()] != c:
                    return False
    return True


print(linter('([{}])'))
print(linter('(([{}]])'))
