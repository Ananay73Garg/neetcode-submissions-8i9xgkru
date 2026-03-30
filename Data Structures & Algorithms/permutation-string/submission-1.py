class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = list(sorted(s1))

        if len(s1) > len(s2):
            return False

        for i in range(len(s2)-len(s1)+1):
            set2 = list(sorted(s2[i:i+len(s1)]))
            if set2 == set1:
                return True

        return False