class Solution:
    def product_except_self(self, nums):
        count_0 =  nums.count(0)
        if count_0>1:
            output=[0]*len(nums)
        elif count_0==1:
            index_0 = nums.index(0)
            output=[0]*len(nums)
            a=1
            for n in nums[:index_0]:
                a*=n
            for n in nums[index_0+1:]:
                a*=n
            output[index_0]=a
        else:
            a=1
            for n in nums:
                a*=n
            output=[]
            for n in nums:
                output.append(int(a/n))
        return output
        