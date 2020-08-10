from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {name: i for i, name in enumerate(list1)}
        min_sum, res = len(list1) + len(list2), []
        for i, name in enumerate(list2):
            if name in index1:
                index_sum = index1[name] + i
                if index_sum < min_sum:
                    res = [name]
                    min_sum = index_sum
                elif index_sum == min_sum:
                    res.append(name)
        return res


def main():
    while True:
        try:
            line = input()
            list1 = stringToList(line)
            line = input()
            list2 = stringToList(line)
            
            sol = Solution()
            ret = sol.findRestaurant(list1, list2)
            
            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
