class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        help_dict={}
        for i,num in enumerate(nums) :
            diff= target-num
            if diff in help_dict:
                return [help_dict[diff],i]
            help_dict[num]=i
        
        