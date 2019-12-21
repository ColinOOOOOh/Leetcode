class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_tmp = []
        substr = []
        for e in s:
            if e in substr_tmp:
                if len(substr_tmp) > len(substr):
                    substr = substr_tmp
                idx = substr_tmp.index(e)
                substr_tmp = substr_tmp[idx+1:]
                substr_tmp.append(e)
            else:
                substr_tmp.append(e)
        if len(substr_tmp) > len(substr):
            substr = substr_tmp
        ret = "" 
        return len(ret.join(substr))
