# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# the Sliding Window Approach
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        min_len = float('inf')  # Initialize with infinity
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]  # Expand the window

            while current_sum >= target:  # Shrink the window if possible
                min_len = min(min_len, right - left + 1)  # Update min_len
                current_sum -= nums[left]  # Remove the leftmost element
                left += 1  # Move the left pointer

        return min_len if min_len!= float('inf') else 0  # Handle the case where no subarray is found
            
        
        
        
        
        