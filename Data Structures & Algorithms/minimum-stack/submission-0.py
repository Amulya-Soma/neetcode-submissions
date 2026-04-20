class MinStack:

    def __init__(self):
        self.s = []
        self.smin = []

    def push(self, val: int) -> None:
        self.s.append(val)
        #Find the minimum element, is it current val or the top of min stack
        if self.smin:
            val = min(val,self.smin[-1])
        self.smin.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.smin.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.smin[-1]
