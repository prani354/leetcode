class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1],reverse=True)
        count = 0
        #print(boxTypes)
        for box,unit in boxTypes:
            if box <= truckSize:
                count += (box * unit)
                #print(count)
                truckSize -= box

            else:
                count += (truckSize * unit)
                break

        return count
