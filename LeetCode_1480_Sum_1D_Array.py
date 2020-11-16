
#LeetCode Problem 1480: Returing Sum of 1D Array 
#Author: Ryan Arendt 
#Verified: 11/15/2020
 
#Description: 
# Goal: Return the Sum of a 1D array.
# Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example: 
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution: 
    def runningSum(self,nums): 
        """ Computes the running sum of a list of integers. Returns a list
            that contains the running sum at each index. 
        """
        run_sum = []
        cur_sum = 0

        for n in nums: 
            cur_sum += n
            run_sum.append(cur_sum)

        return run_sum

