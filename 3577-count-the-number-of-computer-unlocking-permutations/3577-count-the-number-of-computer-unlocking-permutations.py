class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        di=defaultdict(int)
        for i in complexity:
            di[i]+=1
        k=len(complexity)
        n= (10**9)+7
        mi=min(complexity)
        if di[mi]>1  or complexity[0]!=mi:
            return 0
        else:
            return math.factorial(k-1)%n