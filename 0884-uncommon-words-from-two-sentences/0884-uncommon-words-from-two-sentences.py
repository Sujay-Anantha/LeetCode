class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s = s1 + s2
        word = Counter(s)
        uncommon = [x for x in word if word[x]==1]
        
        return uncommon
        