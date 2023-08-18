"""
This program creates a dynamic Array using a raw Array
from ctypes - A foreign function library for Python
"""

from dynamicArray import DynamicArray


def main():
    a = DynamicArray()
    # Print initial size = 0
    print(f"Initial length: {len(a)}")

    for _ in range(10):
        a.append(_)

    for _ in range(a.n):
        print(a[_], end=" ")
    print()

    # Print the after size
    print(f"After length: {len(a)}")


main()
