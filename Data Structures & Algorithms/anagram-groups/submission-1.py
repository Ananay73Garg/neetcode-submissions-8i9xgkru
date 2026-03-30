class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        a = []
        i = 0
        for j in strs:
            if sorted(j) not in x:
                x.append(sorted(j))
        
        while i < len(x):
            b = []
            for j in range(i,len(strs)):
                if sorted(x[i]) == sorted(strs[j]):
                    b.append(strs[j])
            a.append(b)
            i +=1
        return a