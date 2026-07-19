from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        remainder = 0

        index = 0
        for num in nums:
            
            remainder = target - num

            snd_indx = 0
            for nm in nums:

                if nm + remainder == target:
                    print( num , nm)
                    return [num , nm]
                snd_indx += 1
            
            index += 1
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [2, 7]
    print(solution.twoSum([3, 2, 4], 6))       # Output: [2, 4]
    print(solution.twoSum([3, 3], 6))          # Output: [3, 3]