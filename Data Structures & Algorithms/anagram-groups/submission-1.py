class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def bubble_sort(string:str)-> str:
            string=list(string)
            for i in range(len(string)):
                sort_flag=False
                for j in range(len(string)-i-1):
                    if string[j]>string[j+1]:
                        string[j],string[j+1]=string[j+1],string[j]
                        sort_flag=True
                if sort_flag != True:
                    break
            return string

        final_array=[]
        res = defaultdict(list)
        for i in strs:
            sorteds="".join(bubble_sort(i.lower()))
            res[sorteds].append(i)
        return list(res.values())
            


        
        