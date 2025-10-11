class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)

        power_cnt = []
        for p in sorted(counter.keys()):
            power_cnt.append((p,counter[p]))

        cache = {}
        def max_damage(idx):
            if idx in cache:
                return cache[idx]
            if idx >= len(power_cnt):
                return 0

            not_damage = max_damage(idx+1)

            curr_power,curr_cnt = power_cnt[idx]
            next_idx = bisect.bisect_left(power_cnt,(curr_power+3,-1))
            damage = curr_power * curr_cnt + max_damage(next_idx)

            cache[idx] = max(not_damage,damage)
            return cache[idx]

        return max_damage(0)