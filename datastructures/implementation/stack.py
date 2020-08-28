class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def show(self):
        return self.items

    def is_empty(self):
        return self.items == []

s = Stack()
print ("Is stack empty:",s.is_empty())
print (s.show())

s.push('A')
s.push('B')
s.push('C')
print (s.show())
print (s.peek())
print (s.show())
s.pop()
print ("Is stack empty:",s.is_empty())
print (s.show())
