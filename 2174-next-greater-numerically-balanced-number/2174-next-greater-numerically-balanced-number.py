class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i =  n + 1

        while True:
            counter = Counter(str(i))
            flag = True

            for k,v in counter.items():
                if int(k) == v:
                    pass

                else:
                    flag = False
                    break

            if flag:
                return i

            i += 1
        