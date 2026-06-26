from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)

        for ch in s:

            if ch in s:
                freq[ch] += 1

            else:
                freq[ch] = 1

        sorted_dict = sorted(freq.items(),key = lambda x:x[1] , reverse = True)
        #print(sorted_dict)
        l = ""
        for ent in sorted_dict:
            ch , num = ent
            l += (num*ch)

        return l

        