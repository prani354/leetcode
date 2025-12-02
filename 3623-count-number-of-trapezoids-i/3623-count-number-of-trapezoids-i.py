class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        from collections import defaultdict
        
        # 1. Group by y-coordinate
        y_groups = defaultdict(int)
        for x, y in points:
            y_groups[y] += 1
        
        # 2. Compute number of horizontal segments on each y-line: C(k, 2)
        seg_counts = []
        for k in y_groups.values():
            if k >= 2:
                seg_counts.append(k * (k - 1) // 2)
        
        # If less than 2 rows have >=2 points, no trapezoids
        if len(seg_counts) < 2:
            return 0
        
        # 3. Calculate sum of pairwise products efficiently
        # Sum over all i < j: seg[i] * seg[j]
        total_segments = sum(seg_counts) % MOD
        
        result = 0
        running_sum = 0
        
        for s in seg_counts:
            running_sum += s
            running_sum %= MOD
        
        # pairwise product: (sum^2 - sum(s^2)) / 2
        sum_squares = sum((s * s) % MOD for s in seg_counts) % MOD
        
        result = (running_sum * running_sum - sum_squares) % MOD
        result = result * pow(2, MOD-2, MOD)  # divide by 2 using modular inverse
        
        return result % MOD

        