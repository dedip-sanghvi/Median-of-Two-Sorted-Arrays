class Solution:
    def __is_string_unique(self, s):
        set_len = len({c for c in s})
        return len(s)==set_len
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        len_s = len(s)
        max_len =0
        if len_s==1:
            return 1
        elif self.__is_string_unique(s):
            return len_s
        else:
            while(i<len_s):
                j=i+1
                while(j<=len_s):
                    sub_str=s[i:j]
                    len_sub_str=len(sub_str)
                    if self.__is_string_unique(sub_str):
                        if len_sub_str>max_len:
                            max_len=len_sub_str
                    else:
                        break
                    j+=1
                i+=1
            return max_len
