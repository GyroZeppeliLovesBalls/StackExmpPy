class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def stack(self):
        return self.items

    def peek(self):
        i = self.pop()
        self.push(i)
        return i


def balanced(strn):
    stck = Stack()
    for i in strn:
        if i == '(':
            stck.push('(')
        elif i == ')':
            if not stck.is_empty():
                if stck.peek() == '(':
                    stck.pop()
            else:
                return False

    return stck.is_empty()


print(balanced(input()))
