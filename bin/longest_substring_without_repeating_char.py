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
                sub_str = {s[i]}
                sub_str_len=1
                while(j<len_s):
                    c = s[j]
                    if c in sub_str:
                        break
                    else:
                        sub_str.add(s[j])
                        sub_str_len+=1
                        j+=1
                if sub_str_len>max_len:
                    max_len=sub_str_len
                i+=1
            return max_len
