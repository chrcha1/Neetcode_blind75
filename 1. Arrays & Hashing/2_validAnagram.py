class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_list = list(t)
        for st in s:
            if st in t_list:
                t_list.remove(st)
            else:
                return False
        return True