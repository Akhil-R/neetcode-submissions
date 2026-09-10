class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        diff_counts = [0] * 26
        base = ord('a')
        for char_s, char_t in zip(s, t):
            diff_counts[ord(char_s) - base] += 1
            diff_counts[ord(char_t) - base] -= 1
        return not any(diff_counts)
        