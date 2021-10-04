"""
Python Program
"""
import sys

from coolmathtools import factorial


def main() -> int:
    """
    Main function
    """
    _x_: int = factorial(100)
    print(f"100 factorial is {_x_}")
    return 0


if __name__ == "__main__":
    res: int = main()
    sys.exit(res)
