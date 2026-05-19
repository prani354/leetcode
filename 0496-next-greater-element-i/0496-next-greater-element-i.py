class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        hash_map = {}

        for num in reversed(nums2):

            while stack:
                if stack[-1] > num:
                    hash_map[num] = stack[-1]
                    stack.append(num)
                    break
                else:
                    stack.pop()

            if not stack:
                hash_map[num] = -1
                stack.append(num)

        for num in nums1:
            res.append(hash_map[num])

        return res