class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        '''Creates a stack by using a linked list.'''
        self.head = Node("head")
        self.length = 0

    def push(self, item):
        '''Adds the new element to the stack.

        Args:
            item (object): This is the new value to be added.
        '''
        node = Node (item)
        node.next = self.head.next
        self.head.next = node
        self.length += 1

    def isEmpty(self):
        '''Validates if there are no elements remaining in the stack.

        Returns:
            bool: True means that the stack is empty and false if it has any elements in it.
        '''
        return self.length == 0

    def pop(self):
        '''Attempts to read and remove the most recently added element.

        Returns:
            object: If there is any element in the stack it returns the last added element, otherwise it returns None. 
        '''
        if not self.isEmpty():
            remove = self.head.next
            self.head.next = self.head.next.next
            self.length -= 1
            return remove.item
        else:
            return None

    def peek(self):
        '''Attempts to read the most recently added element without removing it.

        Returns:
            object: If there is any element in the stack it returns the last added element, otherwise it returns None.
        '''
        if not self.isEmpty():
            return self.head.next.item
        else:
            return None

    def size(self):
        '''Gets the number of elements in the stack

        Returns:
            int: Number of elements in the stack
        '''
        return self.length
