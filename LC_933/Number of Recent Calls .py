"""
You have a RecentCounter class which counts the number of recent requests within
a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in
milliseconds, and returns the number of requests that has happened in the past
3000 milliseconds (including the new request). Specifically, return the number
of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than
the previous call.
"""
import collections

from common_funcs import stringToList, listToString


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


def main():
    while True:
        try:
            line = input()
            operations = stringToList(line)
            line = input()
            values = stringToList(line)

            ret = []

            obj = None
            for i, op in enumerate(operations):
                if op == 'RecentCounter':
                    obj = RecentCounter()
                elif op == 'ping':
                    ret.append(obj.ping(values[i][0]))

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
