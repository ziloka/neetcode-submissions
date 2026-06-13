import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eatingRate = bannas eaten / hour
        
        # naive many loops but ig O(n^2)
        # calculate piles of bananas to be eaten
        # piles = [1,4,3,2], h = 4
        # eat 4 piles, with 4 banana / hour, finished in 4 hours (highest eatingRate that makes sense)
        # but we want min eating rate
        # init max number in piles, init k
        # for i in range(max, 1, -1):
        # attempt to eat piles of bananas per i bananas an hour
        # if failed, break
        # otherwise, k = min(k, i)
        # return k


        # attempt to write optimized
        # calculate eating Rate = bananas eaten / h
        # init k = (max number of bananas in a pile - min number of bananas in pile) // 2
        # call binary search(low, high)
        # if end < start, return
        # middle = low + (high - low) // 2
        # how do you determine this is the slowest eating rate possible?
        # time to eat = sum(math.ceil(n / middle) for n in piles)
        # if not eating fast enough
        #    eat a bit faster
        # otherwise, eat slower
        # piles [1,4,3,2], h = 9
        
        # def binarySearch(low, high):
        #     if high < low:
        #         # does this make sense?
        #         return h
            
        #     middle = low + (high - low) // 2
        #     hoursTaken = sum(math.ceil(n / middle) for n in piles)

        #     # how do we know if we reach target h
        #     result = False
        #     if hoursTaken < h:
        #         return binarySearch(middle + 1, high)
        #     return binarySearch(low, middle - 1)

        #     # the next binary search was unsuccessful, we probably hit min bananas
        #     # eaten in an hour 
        #     if not result:
        #         return middle 

        # started using help with AI
        # O(N*log(M)), where N is num piles, and M is max bananas in pile
        k = max(piles)
        low = 1
        high = max(piles)
        while low <= high:
            middle = low + (high - low) // 2
            hoursTaken = sum(math.ceil(n / middle) for n in piles)

            if hoursTaken > h:
                low = middle + 1
            else:
                # a valid k, since k <= h
                k = min(k, middle)
                high = middle - 1
        return k
