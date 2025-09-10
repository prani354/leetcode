class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        seen = set()

        for u , v in friendships:
            u -= 1
            v -= 1
            flag = False

            for x in languages[u]:
                if x in languages[v]:
                    flag = True
                    break

            if not flag:
                seen.add(u)
                seen.add(v)

        res = len(languages) + 1

        for i in range(1,n+1):
            ans = 0

            for v in seen:
                if i not in languages[v]:
                    ans += 1
                
            res = min(res,ans)

        return res
        