"""
A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
    1. One or more digits, followed by a dot '.'.
    2. One or more digits, followed by a dot '.', followed by one or more digits
    3. A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", 
"4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", 
"--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""
from common_funcs import stringToString


class Solution:
    def isNumber_re(self, s: str) -> bool:
        import re
        match = re.fullmatch(r'[+-]?(\d+\.\d*|\d*\.\d+|\d+)([eE][+-]?\d+)?', s)
        return bool(match)

    def isNumber_dfa(self, s: str) -> bool:
        # each dictionary in the list represents a state
        # each key-value pair represents a transition function
        # all keys represent the alphabet for the DFA
        dfa = [
            {'+': 1, '-': 1, 'digit': 2, '.': 3},
            {'digit': 2, '.': 3},
            {'digit': 2, '.': 4, 'e': 5, 'E': 5},
            {'digit': 4},
            {'digit': 4, 'e': 5, 'E': 5},
            {'+': 6, '-': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7}
        ]
        curr_state = 0  # DFA initial state
        # run the DFA
        for char in s:
            # cast all digit inputs to 'digit' in the alphabet
            if char.isdigit():
                char = 'digit'
            # return false in an invalid character encountered
            if char not in dfa[curr_state]:
                return False
            # make a transition according to the transition function of the DFA
            curr_state = dfa[curr_state][char]
        if curr_state in {2, 4, 7}:  # return true if DFA ends in accept states
            return True
        return False

    def isNumber(self, s: str) -> bool:
        # whether we have seen the dot, the e(E), or any digit
        seen_dot = seen_e = seen_digit = False

        for i, char in enumerate(s):

            # the optional sign must either come before everything else or
            # right after the E
            if char in '+-':
                if i and s[i-1].lower() != 'e':
                    return False

            # the dot (optional) can only appear once and must be before the E
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True

            # the E can only appear once (optional) and must be following a
            # decimal number or an integer; reset seen_digit for the second part
            elif char in 'eE':
                if seen_e or not seen_digit:
                    return False
                seen_e, seen_digit = True, False

            # set seen_digit to True if we see one
            elif char.isdigit():
                seen_digit = True

            # all other characters are invalid
            else:
                return False
        return seen_digit  # there at least has to be 1 digit in the string


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.isNumber(s)
            ret_re = sol.isNumber_re(s)
            ret_dfa = sol.isNumber_dfa(s)

            out = str(ret)
            out_re = str(ret_re)
            out_dfa = str(ret_dfa)
            print(f"Solved by parsing each char: {out}")
            print(f"Solved using regex:          {out_re}")
            print(f"Solved by simulating DFA:    {out_dfa}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
