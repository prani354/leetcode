class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def count_seq(bars):
            curr = 0
            all_num = set(bars)
            ans = 1

            for i in bars:
                if i - 1 not in all_num:
                    curr = i
                    curr_count = 1

                    while curr + 1 in all_num:
                        curr += 1
                        curr_count += 1
                    ans = max(ans,curr_count)

            return ans

        longest_h = count_seq(hBars)
        longest_v = count_seq(vBars)

        return (min(longest_h,longest_v) + 1) ** 2