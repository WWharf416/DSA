class Stack:
    def __init__(self):
        self.top=-1
        self.S=[None]*(1000)
    def Push(self,v):
        self.top+=1
        self.S[self.top]=v
        return
    def Pop(self):
        if self.isempty():
            print('stack is empty')
        else:
            self.top-=1
        return
    def peek(self):
        if self.isempty():
            return -1
        else:
            return self.S[self.top]
    def Size(self):
        return self.top+1
    def isempty(self):
        return self.top==-1
    
stk = Stack()
t = int(input())

for i in range(t):
    a = input()
    if a[:4]=='push':
        comm, inp = a.split()
        inp = int(inp)
        #print(comm + '\n' + inp)
        stk.Push(inp)
    else:
        if a=='pop':
            stk.Pop()
        elif a=='peek':
            print(stk.peek())
        elif a=='size':
            print(stk.Size())
        elif a=='isempty':
            print(int(stk.isempty()))
    