""" The Naive pattern searching algorithm doesn’t work well in cases where 
    we see many matching characters followed by a mismatching character. 
    Following are some examples：
    
        haystack = "AAAAAAAAAAAAAAAAAB"
        needle = "AAAAB"

        haystack = "ABABABCABABABCABABABC"
        needle =  "ABABAC" (not a worst case, but a bad case for Naive)
    
    KMP algorithm uses degenerating property 
    (pattern having same sub-patterns appearing more than once in the pattern) 
    of the pattern and improves the worst case complexity to O(n).
"""
from typing import List


class KMP:
    def __init__(self, pattern: str):
        self.p = pattern  # pattern
        self.lps = self.__lps() 
        # preprocess the pattern to generate the partial match table
        
    def search_in(self, string: str) -> int:
        """ Implementation of the Knuth-Morris-Pratt Pattern Searching algorithm
            Complexity:
                Best-case: O(n),
                Worst-case: O(n),
                    where n = len(string)
        """
        
        m = len(string)  # length of string
        n = len(self.p)  # lenght of pattern
        
        i = 0  # pointer for current index
        while i <= m - n:
            for j in range(n):
                if string[i + j] != self.p[j]:
                    
                    # skip ahead 
                    # partial_match_length - table[partial_match_length - 1]
                    # characters
                    i += max(j - self.lps[j - 1], 1)
                    break
            else:
                return i
        return -1

    def __lps(self) -> List[int]:
        """ Build the partial match table:
            the length of the Longest Proper Prefix in the (sub)pattern that 
            matches a proper suffix in the same (sub)pattern.
        """
        
        lps = [0]*len(self.p)
        
        # length of longest proper prefix-suffix match for each partial match
        # for the first element, it's always 0 so we skip it
        for i in range(1, len(self.p)):
            select = self.p[:i+1]
            
            for j in range(1,len(select)):  # for each prefix-suffix pair
                prefix = select[:j]  
                suffix = select[-j:]
                
                # if prefix matches suffix and is longer than previous length
                if (prefix == suffix) and (len(prefix) > lps[i]):
                    lps[i] = len(prefix)
        return lps
    
    def display(self):
        print(self.p)
        print(self.lps)
        
def main():
    kmp = KMP("aaaaa")
    string = "aaaaaa"
    found = kmp.search_in(string)
    
    if found < 0:
        print(f"Pattern not found.")
    else:
        print(f"Pattern \"{kmp.p}\" first found in \"{string}\" at index {found}.")
        
        
if __name__ == "__main__":
    main()
