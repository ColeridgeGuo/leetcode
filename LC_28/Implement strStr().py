def strStr(haystack: str, needle: str) -> int:
    """ Simple pattern searching using substring 
        Complexity: 
            Best-case: O(n),
            Worst-case: O(m*(n-m+1)), 
                where n = len(haystack), m = len(needle)
    """
    
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:len(needle)+i] == needle:
            return i
    return -1
