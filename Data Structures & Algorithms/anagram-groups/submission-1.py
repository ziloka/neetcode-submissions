class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for string in strs:
            freq = [0] * 26;
            for c in string:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]

        return [*groups.values()]
