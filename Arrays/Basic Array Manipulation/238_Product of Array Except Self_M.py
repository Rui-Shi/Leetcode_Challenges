# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

from math import prod  # Imports the prod function from the math module (Python 3.8+)
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        zero_count = nums.count(0)
        res = []
        
        if zero_count > 1:
            return [0]*n
        
        elif zero_count == 1:
            total_product = 1
            for num in nums:
                if num != 0:
                    total_product *= num
            
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(total_product)
            
            
        else:
            total_product = prod(nums)
            
            for num in nums:
                res.append(total_product//num)
        
        return res
    

# a better one:
class Solution:
    def productExceptSelf(self,nums):
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

        Args:
            nums: A list of integers.

        Returns:
            A list of integers.
        """
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(1, n):
            prefix *= nums[i - 1]
            answer[i] *= prefix
        
        # Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            answer[i] *= suffix
        
        return answer
        