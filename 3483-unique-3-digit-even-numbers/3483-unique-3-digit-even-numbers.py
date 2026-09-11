class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        hashset = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:
                        hundreds = digits[i]
                        tens = digits[j]
                        ones = digits[k]
                    
                        if hundreds != 0 and ones % 2 == 0:
                            num = hundreds * 100 + tens * 10 + ones
                            hashset.add(num)

        return len(hashset)

                    