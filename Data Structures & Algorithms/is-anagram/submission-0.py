class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        test_s={}
        test_t={}

        for i in range(len(s)):
            test_s[s[i]]=test_s.get(s[i],0)+1
            test_t[t[i]]=test_t.get(t[i],0)+1
        return test_s==test_t

        