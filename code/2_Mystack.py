'''
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

'''
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackList = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stackList.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stackList.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stackList[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stackList == []
"""
愚蠢的我，这是在用栈模拟栈。。。
"""