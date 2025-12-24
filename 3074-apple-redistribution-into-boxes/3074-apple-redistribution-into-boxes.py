class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        apples = sum(apple)
        i = 0
        while apples > 0:
            apples -= capacity[i]
            i += 1

        return i
            

        