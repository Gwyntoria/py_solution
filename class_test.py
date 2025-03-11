from collections import deque


class TestClass:
    def __init__(self, message) -> None:
        self.message = message

    def calculate_sum(self, data_stream: deque[int]):
        for _ in range(len(data_stream)):
            data = data_stream.popleft()

class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B")
        super().method()  # 默认情况下，搜索起始位置为当前类（B）的 MRO

class C(A):
    def method(self):
        print("C")
        super(C, self).method()  # 指定起始位置为 C 类的 MRO

class D(B, C):
    def method(self):
                                # D 类的 MRO 是 (D, B, C, A, Obj)
        super().method()        # 起始位置 D 类， 第一个查找的是 B 类
        super(B, self).method() # 指定起始位置为 B 类, 第一个查找的是 C 类

