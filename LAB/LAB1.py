#Question 1. Write a program in Python to implement a singly linked list of integer values with the following operations :
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addtoHead (self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    #def
            
    def addtotail(self,val):
        new_node = Node(val)
        if self.head is None:
           self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    #def
            
    def addAfter(self,x,val):
        new_node = Node(val)
        curr = self.head
        while curr and curr.data != x:
            curr = curr.next
        if curr is None:
            return    #trả về linkedlist ban đầu trong trường hợp không tìm được số x
        new_node.next = curr.next           #(1,7,2)
        curr.next = new_node
    #def
    def addBefore(self, x, val):
        new_node = Node(val)
        curr = self.head
        prev = None
        while curr and curr.data != x:
            prev = curr
            curr = curr.next
        if not curr: #trả về linkedlist ban đầu trong trường hợp ko tìm được số x
            return
        new_node.next = prev.next
        prev.next = new_node    
    def deleteFromHead(self):
        if self.head is None:
            return
        self.head = self.head.next
    #def
        
    def deleteFromTail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        curr = self.head
        while curr.next is not self.tail:
            curr = curr.next
        curr.next = None
        self.tail = curr
    #def
        
    def deleteAfter(self, val):
        curr = self.head
        while curr is not None:
            if curr.data == val:
                if curr.next is None:
                    raise ValueError("No node to delete after node with value " + str(val))
                deleted_node = curr.next
                curr.next = curr.next.next
                return deleted_node.data
            curr = curr.next
        raise ValueError("Node not found")
    #def
        
    def delX(self, x):
        curr = self.head
        prev = None
        while curr and curr.data != x:
            prev = curr
            curr = curr.next
        if curr is None:  
            return
        if prev is None:  
            self.head = curr.next
        else:
            prev.next = curr.next
            if curr == self.tail:  
                self.tail = prev
        curr.next = None
    #def
        
    def search(self,x):
        curr = self.head
        while curr:
            if curr.data == x:
                return curr
            curr = curr.next
        return None
    #def
    
    def count(self):
        count = 0
        curr = self.head
        while curr:
            count +=1
            curr = curr.next
        return count
    #def
    
    def deleteAtIndex(self, i):
        if i<0 or i>= self.count():
            print("invalid index")
            return
        if i ==0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range (i - 1):
            curr = curr.next
        curr.next = curr.next.next
    #def
        
    def sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.insertNode(sorted_list, current)
            current = next_node

        self.head = sorted_list
    #def

    def insertNode(self, sorted_list, node):
        if sorted_list is None or sorted_list.data >= node.data:
            node.next = sorted_list
            return node

        current = sorted_list
        while current.next and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return sorted_list
    #def
    
    def del_Node(self,p):
        if self.head is None:
            return
        
        if self.head == p:
            self.head = self.head.next
            return
        
        curr = self.head
        while curr.next:
            if curr.next ==p:
                curr.next = curr.next.next
                return
            curr = curr.next
    #def
    
    def ToArray(self):
        array = []
        curr = self.head
        
        while curr:
            array.append(curr.data)
            curr = curr.next
        return array
    #def
    
    def mergeLists(self, list1, list2):
        merged_list = linkedlist()
        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.addtotail(current1.data)
                current1 = current1.next
            else:
                merged_list.addtotail(current2.data)
                current2 = current2.next

        while current1:
            merged_list.addtotail(current1.data)
            current1 = current1.next

        while current2:
            merged_list.addtotail(current2.data)
            current2 = current2.next

        return merged_list
    #def
    
    def attach(self,other_list):
        if self.head is None:
            self.head = other_list.head
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = other_list.head
        other_list.head = None
    #def
    
    def max(self):
        if self.head is None:
            return None
        
        max_val = self.head.data
        curr = self.head.next
        while curr is not None:
            if curr.data > max_val:
                max_val = curr.data
            curr = curr.next
        
        return max_val
    #def
    
    def min(self):
        if self.head is None:
            return None
        
        min_val = self.head.data
        curr = self.head.next
        while curr is not None:
           if curr.data < min_val:
                min_val = curr.data
           curr = curr.next
        return min_val
    #def
    
    def sum(self):
        total = 0
        curr = self.head
        while curr is not None:
            total += curr.data
            curr = curr.next
        return total
    #def
    
    def avg(self):
        total = 0
        count = 0
        curr= self.head
        while curr is not None:
            total += curr.data
            count += 1 
            curr = curr.next
        if count > 0:
            return total / count
        else:
            return None
    #def
    
    def sorted(self):
        if self.head is None or self.head.next is None:
            return True
        
        curr = self.head
        while curr.next is not None:
            if curr.data > curr.next.data:
                return False
            curr = curr.next
        return True
    #def
    
    def insert(self, val):
        new_node = Node(val)

        # Case 1: Danh sách trống hoặc giá trị nút mới nhỏ hơn phần đầu
        if self.head is None or val < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None and current.next.data < val:
                curr = curr.next

            # Case 2: Chèn nút mới vào giữa hoặc cuối danh sách
            new_node.next = curr.next
            curr.next = new_node
    #def
    
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    #def
    
    def isSame(self, other_list):
        current1 = self.head
        current2 = other_list.head

        while current1 is not None and current2 is not None:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next

        # If one list is longer than the other
        if current1 is not None or current2 is not None:
            return False

        return True

    #def
    
    def traverse(self):
        if self.head is None:
            print(' linkedlist is empty ')
            return
        
        curr = self.head
        while curr is not None:
            print ( curr.data, end= "  ")
            curr = curr.next
        print()
    
  

   
number = [4,3,2,1,0]
mylist= linkedlist()
for i in range(len(number)):
    mylist.addtoHead(number[i])
mylist.addtotail(5)
mylist.addtotail(6)
mylist.addAfter(2,9)
mylist.addBefore(5,7)
#mylist.deleteFromHead()
#mylist.deleteFromTail()
#mylist.delX(3)
print("Original list 1:")
mylist.traverse()
#
deleted_value = mylist.deleteAfter(3)
print("Deleted value:", deleted_value)
mylist.traverse()
# Search for a node
node= mylist.search(2)
if node:
    print("Node found:", node.data)
else:
    print("Node not found.")
    
# Count the number of nodes
node_count = mylist.count()
print("num of nodes:",node_count)

# Delete a node at a specific index
mylist.deleteAtIndex(4)
# Traverse the list and display node info
curr = mylist.head
while curr:
    print(curr.data, end= "  ")
    curr = curr.next
    
#sorted:
mylist.sort()
print("\nSorted list:")
mylist.traverse()

#delete node p:
mylist.del_Node(4)
print("Linked list after deletion:")
mylist.traverse()

#Create array:
arr = mylist.ToArray()
print("Array representation:",arr)

# Example Merged list:
list1 = linkedlist()
list1.addtotail(1)
list1.addtotail(3)
list1.addtotail(5)

list2 = linkedlist()
list2.addtotail(2)
list2.addtotail(4)
list2.addtotail(6)
print('- New list1:')
print("+ First list:")
list1.traverse()

print("+ Second list:")
list2.traverse()

merged_list = list1.mergeLists(list1, list2)
print("+ Merged list:")
merged_list.traverse()

# Example attach:
list3 = linkedlist()
list3.addtotail(1)  
list3.addtotail(2)
list3.addtotail(3)

list4 = linkedlist()
list4.addtotail(4)
list4.addtotail(5)
print('- New list2:')
print("+ Third list:")
list3.traverse()

print("+ Fourth list:")
list4.traverse()

list3.attach(list4)
print("+ Attach merged list:")
list3.traverse()


#Find MAX in list:
max_value = mylist.max()
print("Max value:", max_value)

#Find MIN in list:
min_value = mylist.min()
print("Min value:", min_value)

#Sum in list:
sum_of_list = mylist.sum()
print("SUM of list:", sum_of_list)

#Average in list:
average = mylist.avg()
if average is not None:
    print("AVERAGE of list:", average)
else:
    print("ERROR AVERAGE")

#Sorted in list:
is_sorted = mylist.sorted()
if is_sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted>")

#Insert:
mylist.insert(6)
mylist.insert(4)
mylist.insert(8)
mylist.insert(1)
mylist.insert(2)
mylist.traverse()

# reverse()
print("Reversed list:")
mylist.reverse()
mylist.traverse()

#Is_same():
linked_list1 = linkedlist()
linked_list1.addtoHead(1)
linked_list1.addtoHead(2)
linked_list1.addtoHead(3)

linked_list2 = linkedlist()
linked_list2.addtoHead(1)
linked_list2.addtoHead(2)
linked_list2.addtoHead(3)

is_same = linked_list1.isSame(linked_list2)
print("Are the lists the same?", is_same)  # Output: Are the lists the same? True


#Question 2. Write a program in Python to implement a singly linked list of string values with 1 - 10 operations in the above list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def addAfter(self, p, x):
        current = self.head
        while current is not None:
            if current.value == p:
                new_node = Node(x)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    # Other methods from the previous code...


# Example usage
linked_list = SinglyLinkedList()

linked_list.addToHead("Alice")
linked_list.addToHead("Bob")
linked_list.addToTail("Charlie")
linked_list.addAfter("Bob", "Dave")

print("Linked List Q2:") 
linked_list.traverse()  # Output: Bob Alice Dave Charlie



#Question 3. Write a program in Python to implement a doubly linked list of integer values with the above operations.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def addAfter(self, p, x):
        current = self.head
        while current is not None:
            if current.value == p:
                new_node = Node(x)
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                break
            current = current.next

    def traverseForward(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    def traverseBackward(self):
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.value, end=" ")
            current = current.prev
        print()

    # Other methods from the previous code...


# Example usage
linked_list = DoublyLinkedList()

linked_list.addToHead(1)
linked_list.addToHead(2)
linked_list.addToTail(3)
linked_list.addAfter(2, 4)
print("DoublyLinkedList Q3:")

print("Linked List (forward):")
linked_list.traverseForward()  # Output: 2 1 4 3

print("Linked List (backward):")
linked_list.traverseBackward()  # Output: 3 4 1 2


#Question 4. Write a program in Python to implement a circular linked list of integer values with the above operations.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def addAfter(self, p, x):
        current = self.head
        while current.next != self.head:
            if current.value == p:
                new_node = Node(x)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        if current.value == p:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node

    def traverse(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    # Other methods from the previous code...


# Example usage
linked_list = CircularLinkedList()

linked_list.addToHead(1)
linked_list.addToHead(2)
linked_list.addToTail(3)
linked_list.addAfter(2, 4)

print("Circular Linked List Q4 :")
linked_list.traverse()  # Output: 2 1 4 3  (circular)




