class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        diff_counts = [0] * 26
        base = ord('a')
        for i in range(len(s)):
            diff_counts[ord(s[i]) - base] += 1
            diff_counts[ord(t[i]) - base] -= 1
        return not any(diff_counts)
        