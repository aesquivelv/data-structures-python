# import stack_deque as StackClass
# import stack_linked_list as StackClass
import stack as StackClass
import unittest

class TestStack(unittest.TestCase):
    
    def test_isEmpty_init(self):
        '''Create an empty stack. Test that its size is 0.'''
        stack = StackClass.Stack()
        self.assertEqual(0, stack.size())

    def test_push1_size(self):
        '''Push an element into the stack. Test that its size is now 1.'''
        stack = StackClass.Stack()
        stack.push(1)
        self.assertEqual(1, stack.size())

    def test_push2_size(self):
        '''Push another element into the stack. Test that its size is now 2.'''
        stack = StackClass.Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.size())
    
    def test_push1_peek_size(self):
        '''Peek an element from the stack. Test that it matches the 1st pushed value.
        Check that the size of the stack is 1.
        '''
        stack = StackClass.Stack()
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertEqual(1, stack.size()) 

    def test_push2_peek_size(self):
        '''Peek an element from the stack. Test that it matches the 2nd pushed value.
        Check that the size of the stack is 2.
        '''
        stack = StackClass.Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.peek())
        self.assertEqual(2, stack.size()) 

    def test_push2_pop1_size(self):
        '''Pop an element from the stack. Test that it matches the 2nd pushed value.
        Check that the size of the stack is 1.
        '''
        stack = StackClass.Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.size())
    
    def test_push1_pop1_size(self):
        '''Pop an element from the stack. Test that it matches the 1st pushed value.
        Check that the size of the stack is 0.
        '''
        stack = StackClass.Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())
        self.assertEqual(0, stack.size())
    
    def test_overflow(self):
        '''Attempt to pop an element from the stack. You should receive a None.
        '''
        stack = StackClass.Stack()
        self.assertEqual(None, stack.pop())

if __name__ == '__main__':
    unittest.main()