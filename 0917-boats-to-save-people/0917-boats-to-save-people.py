class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        h = len(people)-1

        boats = 0

        while l <= h:
            if people[l] + people[h] <= limit:
                l += 1
                h -= 1
            else:
                h -= 1
            boats += 1

        return boats