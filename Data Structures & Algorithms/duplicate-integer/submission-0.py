class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_arr=[]
        for i in nums:
            if i in test_arr:
                return True
            test_arr.append(i)
        return False


        