"""
Library
"""

def factorial(_n_: int) -> int:
    """
    Factorial function
    """
    assert _n_ >= 0
    return 1 if _n_ <= 1 else _n_ * factorial(_n_-1)
