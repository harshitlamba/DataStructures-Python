class Node:
    
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
        
class Stack:
    
    length = 0
           
    def __init__(self):
        self.top = None
        self.bottom = None
        print('Empty Stack created.')
    
    def is_empty(self):
        if self.top is None:
            return(True)
        else:
            return(False)
            
    def return_top(self):
        if not self.is_empty():
            return('The top of stack is: {}'.format(self.top.data))
        raise Exception('The stack is empty.')
    
    def push(self, data):
        if isinstance(data, list):
            for i in data:
                if self.top is None:
                    node = Node(i, None)
                    self.top = node
                    self.bottom = node
                    Stack.length += 1
                else:
                    node = Node(i, None)
                    self.top.next_node = node
                    self.top = node
                    Stack.length += 1
        else:
            raise Exception('Expected a list, got {}'.format(type(data)))
        
    def pop(self, count = 1):
        if self.is_empty():
            raise Exception('The stack is empty.')
        elif Stack.length == 1:
            self.top = None
            self.bottom = None
            Stack.length = 0
            print('{} element(s) popped. New top is {}.'.format(count, self.top))
        else: 
            step_count = 1
            itr = self.bottom
            while Stack.length - step_count > count:
                itr = itr.next_node
                step_count += 1
            self.top = itr
            self.top.next = None
            Stack.length -= count
            print('{} element(s) popped. New top is {}.'.format(count, self.top.data))
    
    def print_stack(self):
        if self.is_empty():
            raise Exception('The stack is empty.')
        itr = self.bottom
        stack_element = ''
        while itr:
            stack_element += str(itr.data) + '|'
            itr = itr.next_node
        print('The stack is: {}'.format(stack_element))
            
stack = Stack()            
# stack.is_empty()        
# stack.return_top()            
# stack.pop()        
stack.push([3,5])
stack.print_stack()
# stack.is_empty()        
stack.return_top()
stack.push([6,7])
stack.print_stack()            
stack.pop(2)
stack.pop()
stack.pop()    
stack.push([10,20])
stack.print_stack()