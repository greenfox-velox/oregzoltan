# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
    def __init__(self):
        self.store_items = []

    def size(self):
        total = 0
        for i in self.store_items:
            total += 1
        return total

    def push(self, item):
        self.store_items += [item]

    def pop(self):
        last = self.store_items[-1]
        self.store_items = self.store_items[:-1]
        return last

onestack = Stack()
onestack.push('apple')
onestack.push('wine')
onestack.push('wine')
print("Number of elements: ", onestack.size())
print(onestack.store_items)
print(onestack.pop())
print(onestack.store_items)
