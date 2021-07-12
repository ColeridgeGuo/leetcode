"""
Given an array of strings words and a width maxWidth, format the text such that 
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as 
you can in each line. Pad extra spaces ' ' when necessary so that each line has 
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the 
number of spaces on a line does not divide evenly between words, the empty slots 
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is 
inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            line = []  # each line of words, given maxWidth
            line_len = 0  # length of the line w/ 1 space after each word
            # In a greedy approach, fit as many words into one line as possible,
            # in which case at most 1 space is inserted after each word

            # find the right words that fit within maxWidth
            while i < len(words) and line_len + len(words[i]) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i]) + 1
                i += 1

            # calculate justifying spaces
            if len(line) > 1 and i < len(words):
                # number of spaces needed
                spaces = maxWidth - sum(len(x) for x in line)
                # number of places to insert spaces
                n = len(line) - 1
                # if not evenly divided, zp places on the left will be assigned
                # pp+1 spaces, and the rest will be assigned pp spaces
                pp, zp = divmod(spaces, n)
                new_line = []  # line w/ spaces
                # put each word and its following spaces into new_line
                for j, word in zip(range(n), line):
                    new_line.append(word)
                    new_line.extend([' ']*(pp, (pp+1))[j < zp])
                new_line.append(line[-1])  # add the last word of this line
                res.append(''.join(new_line))
            else:
                # if only one word or the last line of text, left-justified with
                # no extra space inserted between words
                res.append(' '.join(line).ljust(maxWidth))
        return res


def main():
    while True:
        try:
            line = input()
            words = stringToList(line)
            line = input()
            maxWidth = int(line)

            sol = Solution()
            ret = sol.fullJustify(words, maxWidth)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
