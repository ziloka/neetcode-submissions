class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1
        
        # fixed sliding window
        start = 0
        end = len(s1)
        while end < len(s2) + 1:
            target = s2[start:end]
            freq = {}
            for c in target:
                freq[c] = freq.get(c, 0) + 1
            
            if freq == s1_freq:
                return True

            start += 1
            end += 1

        return False