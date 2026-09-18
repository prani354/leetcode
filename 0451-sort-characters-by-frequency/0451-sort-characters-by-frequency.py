from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)

        for ch in s:

            if ch in s:
                freq[ch] += 1

            else:
                freq[ch] = 1

        sorted_freq_list = sorted(freq.items(),key = lambda x:x[1],reverse = True)
        #print(sorted_freq_list)
        res = ""

        for ch,val in sorted_freq_list:
            res += (ch*val)

        return res