class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_map = {} # stores { character: last_seen_index }
        start = 0

        for end, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            char_map[char] = end
            longest = max(longest, end - start + 1)

        return longest
