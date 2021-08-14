from bin.product_of_array_except_self import Solution

def test_product_except_self_1():
    sol = Solution()
    result = sol.product_except_self([1,2,3,4])
    assert result==[24,12,8,6]

def test_product_except_self_2():
    sol = Solution()
    result = sol.product_except_self([-1,1,0,-3,3])
    assert result==[0,0,9,0,0]
