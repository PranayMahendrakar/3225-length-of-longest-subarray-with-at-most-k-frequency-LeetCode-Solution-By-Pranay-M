class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        left = 0
        result = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result