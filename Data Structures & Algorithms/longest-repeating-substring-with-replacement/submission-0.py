class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # target time complexity O(n)
        # invariant: at end of loop, count always represent longest substring of distinct characters
        # where k chars of the substring are replaced
        # edge cases: s = XYXYXX, k = 1, output=4
        #             s = XXXYYYY, k = 1, output=4

        # brute force O(n^2)
        # for each possible window, check if the count of the same character
        # and add at most k equals the window size then
        # pick the max window size result
        # otherwise continue to next window

        # optimized algorithm O(n)
        # window expands each time
        # track char frequency within the window
        # pick max char with highest frequency and replacement up to k chars length
        # if window invalid (char with highest frequency and up to k chars
        # is not the same size as the window)
        # contract window from the left until condition is met
        res = 0

        l = 0
        freq = {}
        max_freq = 0
        for r, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            max_freq = max(max_freq, freq[c])
            # contract window when invalid
            while (r - l + 1) - max_freq > k:  
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

