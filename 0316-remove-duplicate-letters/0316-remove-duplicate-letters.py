class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hashmap = {}
        stack = []
        visited = set()

        for ch in s:
            
            hashmap[ch] = hashmap.get(ch,0) + 1

        for ch in s:
            
            hashmap[ch] -= 1

            if ch in visited:
                continue

            while stack and ch < stack[-1] and hashmap[stack[-1]] > 0:
                 visited.remove(stack.pop())

            visited.add(ch)
            stack.append(ch)

        return "".join(stack)