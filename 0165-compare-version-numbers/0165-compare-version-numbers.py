class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.') 
        m,n = len(s1),len(s2)
        #print(s1,s2)

        for i in range(max(m,n)):
            v1 = int(s1[i]) if i < m else 0
            v2 = int(s2[i]) if i < n else 0

            if v1 < v2:
                return -1
            if v1 > v2:
                return 1 

        return 0

        


        