# Problem: Two Sum
# Approach:
# Use two nested loops to check all possible pairs
# For each nums[i], check if any nums[j] equals (target - nums[i])
# Return indices when a valid pair is found

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
