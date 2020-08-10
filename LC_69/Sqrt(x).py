"""
    Compute and return the square root of x,
    where x is guaranteed to be a non-negative integer.

    Since the return type is an integer,
    the decimal digits are truncated
    and only the integer part of the result is returned.
"""


def mySqrt1(x: int) -> int:
    """ straightforward math """
    return int(x**(1/2))


def mySqrt2(x: int) -> int:
    """ Newton's iterative method """
    k = x
    while k * k > x:
        k = (k + x/k)//2
    return int(k)


def mySqrt3(x: int) -> int:
    """ Binary Search method """
    if x == 0:
        return 0
    
    left, right = 1, x
    while left < right:
        mid = left + (right - left) // 2
        if mid > x / mid:
            right = mid - 1
        else:
            if mid + 1 > x / (mid + 1):
                return mid
            left = mid + 1
    return left


if __name__ == "__main__":
    for i in range(0, 20):
        print(f"{i:2}: {mySqrt1(i)}, {mySqrt2(i)}, {mySqrt3(i)}")
