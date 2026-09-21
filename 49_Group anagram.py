class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        total={}
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            
            total[tuple(count)].append(s)
        return list(total.values())