from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Check a word letters in word
        counter = 0 
        group = []
        for word in strs:

            sub_group = []
            for i in strs:
                if sorted(i) == sorted(word):
                    sub_group.append(word)
                    sub_group.append(i)
                else:
                    sub_group.append(word)
            
            group.append(list(set(sub_group)))
            counter += 1

        final_grp = []
        for grp in group:
            if grp in final_grp:
                continue
            else:
                if len(final_grp) > 0 and len(grp) < len(final_grp[-1]):
                    total_length_list = len(final_grp) -1 
                    final_grp.insert(total_length_list-1, grp)
                else:
                    final_grp.append(grp)
        return sorted(final_grp)



if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
        