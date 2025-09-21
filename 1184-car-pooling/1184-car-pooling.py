class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #trips.sort(key = lambda x:(x[1],x[2]))
        #print(trips)
        locations = [0] * 1001
        for passenger,s,e in trips:
            locations[s] += passenger
            locations[e] -= passenger
        #print(locations)
        for passenger in locations:
            capacity -= passenger
            #print(capacity)
            if capacity < 0: return False

        return True

        