import sys
from io import StringIO

input1 = """5"""
input2 = """"""

sys.stdin = StringIO(input1)


# sys.stdin = StringIO(input2)


def draw_figure(n):
    if n == 0:
        return
    print('*' * n, end='\n')
    draw_figure(n - 1)
    print('#' * n)


n = int(input())
draw_figure(n)
