class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        if s_counter == t_counter:
            return True
        else:
            return False
        