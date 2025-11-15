class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zeros = [-1]
        res = 0

        for i,c in enumerate(s):
            if s[i] == '0':
                zeros.append(i)

            p = len(zeros) - 1
            count = 0
            j = i

            while 0 <= p and count * count <= i:
                k = zeros[p]
                p -= 1
                ones = i - k - count
                res += max(0,min(j-k,ones - count * count + 1))
                j = k
                count += 1
        return res 

        