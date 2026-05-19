class MinStack:

    def __init__(self):
        self.stack_arr = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.stack_arr.append(val)
        min_arr_length = len(self.min_arr)
        if min_arr_length == 0:
            self.min_arr.append(val)
        elif val <= self.min_arr[-1]:
            self.min_arr.append(val)        

    def pop(self) -> None:
        top_element = self.stack_arr[-1]
        self.stack_arr = self.stack_arr[:-1]
        if self.min_arr[-1] == top_element:
            self.min_arr = self.min_arr[:-1]
        
        return top_element

    def top(self) -> int:
            return self.stack_arr[-1]

        

    def getMin(self) -> int:
            print(self.min_arr)
            return self.min_arr[-1]

        
