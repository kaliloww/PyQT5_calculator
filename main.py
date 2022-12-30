def get_list() -> list:
    return list(range(0, 1_000_000, 2))


""" 
    what is Binary Search? 
    then do Solution for search target in list 
"""


class Solution:
    def __init__(self, list, target):
        self.list = list
        self.target = target

    def find_target(self, list, target):
        self.list = list
        self.target = target
        a = list

        value = target
        mid = len(a) // 2
        low = 0
        high = len(a) - 1

        while a[mid] != value and low <= high:
            if value > a[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            return "No value"
        else:
            return f"ID = {mid}"


h = Solution(get_list(), 981860)
print(h.find_target(get_list(), 981860))