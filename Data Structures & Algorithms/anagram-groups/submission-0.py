class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        placed = set()

        result = []
        for i in range(len(strs)):
            if i in placed:
                continue

            group = [strs[i]]
            for j in range(i+1, len(strs)):
                if j not in placed and self.isAnagram(group[0], strs[j]):
                    group.append(strs[j])
                    placed.add(j)
            result.append(group)
        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for c in s:
            freq = count.get(c, 0) + 1
            count[c] = freq
        
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] < 0:
                return False
        return True