class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Stack solution
        stack = []
        pairs = [(pos,spd) for pos,spd in zip(position,speed)]
        pairs = sorted(pairs)[::-1]

        #print(pairs)
        #Time calculation

        for pos,spd in pairs:
            time = (target - pos) / spd
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)