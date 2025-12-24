class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums= Counter(nums)    # print(nums)

        max_count=nums[0]
        max_ele = 0

        for i in nums:
            if nums[i] > max_count:
                max_ele = i
                max_count=nums[i]

        
        return max_ele
