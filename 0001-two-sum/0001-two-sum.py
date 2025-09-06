class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in hashset:
                return [hashset[ans] , i]
            else:
                hashset[nums[i]] = i

        

        
        