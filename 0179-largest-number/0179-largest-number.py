class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = list(map(str, nums))
        res.sort(key=lambda x:x*10,reverse=True)
        print(res)

        if res[0] == '0':
            return '0'

        return "".join(res)