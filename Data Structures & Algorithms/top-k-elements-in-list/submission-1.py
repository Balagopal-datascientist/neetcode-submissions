class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        position_dict=dict()
        for value in nums:
            position_dict[value]=position_dict.get(value,0)+1
        # print(position_dict)
        arr=[]
        for num,cnt in position_dict.items():
            arr.append([cnt, num])
        # print(repo)
        arr.sort()
        res= []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        