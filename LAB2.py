class EmptyStackException(Exception):
    pass
#class

class EmptyQueueException(Exception):
    pass
#class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    #def

#class

#Question 1. Write a program in Python to implement a stack of integer values 
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def
    
    def clear(self):
        self.head = None
        
    #def

    def push(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    #def

    def pop(self):
        
        if self.isEmpty() :
            raise EmptyStackException("Stack is empty")
        elif self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            popped = curr.next
            self.tail = curr
            self.tail.next = None
        return popped.data
    #def

    def top(self):
        if self.isEmpty() is True:
            raise EmptyStackException("Stack is empty")
        else:
            return self.tail.data
    #def

    def traverse(self):
        result = []
        curr  = self.head
        if self.isEmpty() is True:
            raise EmptyStackException("Stack is empty")
        else:
            while curr is not None:
                result.append(curr.data)
                curr = curr.next 
            print(result)
    #def



def decimal_to_binary1(decimal_num):
    stack = Stack()
    if decimal_num == 0:
        stack.push(0)

    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num //= 2

    binary_num = ""
    while not stack.isEmpty():
        binary_num += str(stack.pop())

    return binary_num


stack = Stack()
print("is Empty:", stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Original list 1:")
stack.traverse()
print("is Empty:", stack.isEmpty())
print("Top:", stack.top())

binary = decimal_to_binary1(15)
print("Binary representation of 15:", binary)


#Question 2. Write a program in Python to implement a queue of integer values with the following operations :
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def

    def clear(self):
        self.head = None
        self.tail = None

    def enQueue(self,data):
        new_Node = Node(data)
        if self.isEmpty() is True:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head = new_Node
    # add element at the head of the Linked List
    #def

    def deQueue(self):
        if self.isEmpty() is True:
            raise EmptyQueueException("Queue is empty")
        elif self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            popped = self.tail
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
            self.tail = curr
        return popped.data
    # delete element at the end of the Linked List
    #def

    def first(self):
        if self.isEmpty() is True:
            raise EmptyQueueException("Queue is empty")
        else:
            return self.tail.data
    #def

    def traverse(self):
        result = []
        curr = self.head
        if self.isEmpty() is True:
            raise EmptyQueueException("Queue is empty")
        else:
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            print(result)
    # convert Linked List to the List
    #def

def decimal_to_binary2(decimal_num):
    queue = Queue()
    if decimal_num == 0:
        queue.enQueue(0)
    while decimal_num > 0:
        remainder = decimal_num % 2
        queue.enQueue(remainder)
        decimal_num //= 2

    binary_num = ""
    while not queue.isEmpty():
        binary_num = str(queue.deQueue()) + binary_num

    return binary_num
#def
queue = Queue()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
print("Original list 2:")
queue.traverse()
binary = decimal_to_binary2(15)
print("Binary representation of 15:", binary)

    
    






