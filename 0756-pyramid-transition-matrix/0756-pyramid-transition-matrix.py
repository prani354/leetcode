class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        dallow = defaultdict(list)
        for a in allowed:
            dallow[a[:2]].append(a[2])
            
        crs = [bottom]
        while crs and len(crs[0]) > 1:
            nrs = set()
            for cr in crs:
                nr = [dallow[l+r] for l,r  in zip(cr, cr[1:])]
                nrs.update(product(*nr))
            crs = list(nrs)
        return len(crs) > 0