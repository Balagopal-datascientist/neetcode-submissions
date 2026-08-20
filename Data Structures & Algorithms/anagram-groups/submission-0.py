class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_array=[]
        res = defaultdict(list)
        for i in strs:
            sorteds="".join(sorted(i))
            res[sorteds].append(i)
        return list(res.values())
            


        
        