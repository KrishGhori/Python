x = [9, 12, 7, 4, 11]
x.append(8)

# Sort list 
x.sort()
print(x)

# reversed list
reversed_x = x[::-1]
print(reversed_x)

# min value
print("min in array",min(x))


# Last-In, First-Out (LIFO) principle
st= []
st.append('A')
st.append('B')
st.append('C')
print("Stack: ", st)

# Peek
topElement = st[-1]
print("Peek: ", topElement)

# Pop
poppedElement = st.pop()
print("Pop: ", poppedElement)
print(f"stack : {st}")

# isEmpty
isEmpty = not bool(st)
print("isEmpty: ", isEmpty)

# Size
print(f"Size: {len(st)}")


# creat stack using class
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]
  
  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)
  
myStack = Stack()

myStack.push('x')
myStack.push('y')
myStack.push('z')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())


#Implementing a Queue Class
class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())



