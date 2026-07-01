class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch not in freq:
                freq[ch]=0
            freq[ch]+=1

        for ch in t:
            if ch not in freq:
                freq[ch]=0
            freq[ch]-=1

        for value in freq.values():
            if value!=0:
                return False
        
        return True