class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashh=set()

        for i in nums:
            if i in hashh:
                return True
            hashh.add(i)

        return False

        
        
        """for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] == nums[j]:
                        return True
        return False"""
