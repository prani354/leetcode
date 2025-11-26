class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for text in strs:
            sorted_str = ''.join(sorted(text))

            if sorted_str not in hashmap:
                hashmap[sorted_str]  = [] 

            hashmap[sorted_str].append(text)

        return list(hashmap.values())

        