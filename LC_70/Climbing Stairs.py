"""
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
"""


def climbStairs_rc(n: int) -> int:
    """ Recursion """
    if n <= 2:
        return n
    return climbStairs_rc(n-1) + climbStairs_rc(n-2)
    

def climbStairs_dp(n: int) -> int:
    """ Dynamic Programming """
    steps = {1:1, 2:2}
    for i in range(3,n+1):
        steps[i] = steps[i-1] + steps[i-2]
    return steps[n]


def climbStairs_bf(n: int) -> int:
    """ Brute Force """
    def climb_Stairs(i: int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        return climb_Stairs(i+1, n) + climb_Stairs(i+2, n)
    
    return climb_Stairs(0, n)


def climbStairs_memo(n: int) -> int:
    """ Memoization """
    memo = [0 for i in range(n+1)]
    
    def climb_Stairs(i: int, n: int, memo: list) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = climb_Stairs(i+1, n, memo) + climb_Stairs(i+2, n, memo)
        return memo[i]
    
    return climb_Stairs(0, n, memo)
    
   
if __name__ == "__main__":
    print(f"{'Recursion':25} {climbStairs_rc(3)}")
    print(f"{'Dynamic Programming':25} {climbStairs_dp(3)}")
    print(f"{'Brute Force':25} {climbStairs_bf(3)}")
    print(f"{'Memoization':25} {climbStairs_memo(3)}")
