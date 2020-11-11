class MyQueue(object):
    def __init__(self):
        self.queue = []
        self.buff = []
    
    def peek(self):
        if len(self.queue) == 0:
            while self.buff:
                self.queue.append(self.buff.pop(-1))
            
        return self.queue[-1]
            
    def pop(self):
        if len(self.queue) == 0:
            while self.buff:
                self.queue.append(self.buff.pop(-1))
            
        self.queue.pop(-1)
        
        
    def put(self, value):
        self.buff.append(value)
            
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
