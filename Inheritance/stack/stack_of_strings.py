class Stack:

    def __init__(self):
        self.data = ["pomegranate", "durian", "peach"]

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not self.data:
            print("Stack is empty.")
        else:
            print(self.data[-1])
            self.data.pop(-1)

    def top(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.data[-1] 

    def is_empty(self):
        if not self.data:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data[::-1])


# 1. Create a new stack
stack = Stack()

# 2. Test push method
stack.push("apple")
stack.push("banana")
stack.push("cherry")
print("Stack after pushes:", stack)  # Expect: [cherry, banana, apple]

# 3. Test top method
print("Top element:", stack.top())  # Expect: "cherry"

# 4. Test is_empty method
print("Is the stack empty?", stack.is_empty())  # Expect: False

# 5. Test pop method
print("Popped element:", stack.pop())  # Expect: "cherry"
print("Stack after pop:", stack)       # Expect: [banana, apple]

# 6. Test pop method on remaining elements
stack.pop()  # Should remove "banana"
stack.pop()  # Should remove "apple"
print("Stack after popping all elements:", stack)  # Expect: []

# 7. Test is_empty on empty stack
print("Is the stack empty?", stack.is_empty())  # Expect: True

# 8. Test top and pop on empty stack to see behavior
print("Top element on empty stack:", stack.top())  # Expect: Stack is empty. / None
print("Popped element on empty stack:", stack.pop())  # Expect: Stack is empty. / None

