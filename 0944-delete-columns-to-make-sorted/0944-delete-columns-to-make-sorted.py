class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        hashmap = dict()

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                hashmap.setdefault(j, []).append(strs[i][j])
        #print(hashmap)

        count = 0
        for key,value in hashmap.items():
            if list(sorted(value)) != value:
                count += 1

        return count



        