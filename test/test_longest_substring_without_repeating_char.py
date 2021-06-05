from bin.longest_substring_without_repeating_char import Solution

def test_lengthOfLongestSubstring1():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("abcabcbb")
    assert result==3

def test_lengthOfLongestSubstring2():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("bbbbb")
    assert result==1

def test_lengthOfLongestSubstring3():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("pwwkew")
    assert result==3

def test_lengthOfLongestSubstring4():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("")
    assert result==0

def test_lengthOfLongestSubstring5():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("aab")
    assert result==2
