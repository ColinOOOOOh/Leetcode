class Solution:
    def find(self, s: str, c: str) -> list:
        ret = []
        for i, e in enumerate(s):
            if e == c:
                ret.append(i)
        return ret
    
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        substr_tmp = []
        substr = []
        for e in s:
            substr_tmp.append(e)
            substr_set = set(substr_tmp)
            if len(substr_set) <= 2:
                # substr_tmp.append(e)
                print(substr_set)
            else:
                if len(substr_tmp) - 1 > len(substr):
                    substr = substr_tmp[:-1]
                while len(substr_set) > 2:
                    substr_tmp.pop(0)
                    substr_set = set(substr_tmp)
        if len(substr_tmp) > len(substr):
            substr = substr_tmp
        return len(substr)
            
