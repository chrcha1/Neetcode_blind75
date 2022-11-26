class Solution:
    # notes:
    # sorted(string) returns a list
    # to join the list together do: "".join(sorted(string))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for word in strs:
            sortedW = "".join(sorted(word))
            if sortedW in res_dict:
                res_dict[sortedW].append(word)
            else:
                res_dict[sortedW] = [word]
        return res_dict.values()
