#LeetCode: Problem 01 Two Sum 
#Author: Ryan Arendt 
#Hash Map Solution Adapted from: https://www.youtube.com/watch?v=U8B984M1VcU
#Verified: 11/15/2020

#Description: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.You may assume that each input would have exactly 
# one solution, and you may not use the same element twice.You can return the answer 
# in any order.

# Example:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]


#This is the O(n) solution using a hash map. Its a good example of how
#how to think of a problem in a subtley different way. So its worthy of note here.

class Solution: 
    def twoSum(self, nums, target): 
        #The index map stores each number and its index
        index_map = {}
        #Contains the index of the two numbers that add to the target sum
        sum_index = []

        for idx in range(0, len(nums)): 
            cur_num = nums[idx]

            #This is the critical peice of the algorithem. Instead of searching for
            #what two numbers add up to the target, we see if the difference between the
            #current number and the target is in the map (its complement). This is suble
            #but super important, since doing it this away allows to only check the hash map
            # O(1) and eliminates the need for another for loop.
            diff = target-cur_num

            #If the difference is in the index map: we have a solution. 
            #Remember: seeing if a key is in a hash is ~constant time.
            if diff in index_map: 
                sum_index.append(index_map[diff])
                sum_index.append(idx)

                return sum_index
            #We have not seen the number yet, add it to the map.
            else: 
                index_map[cur_num] = idx
                
        return sum_index

#s = Solution()
#print(s.twoSum([2,5,7, 4], 9))


#This is the brute force solution I originally solved this problem with. However, 
#LeetCode now says that this is too slow. (Which makes sence: its O(n^2). So. We have to
#think of a better way. 
# class Solution: 
#     def twoSum(self, nums, target): 
      
#       for i in range(0, len(nums)): 
#           # Since there are no repeats, we can continously 
#           # slice off chunks of the list we have already seen.
#           nums_slice = nums[i+1:len(nums)]

#           for j in range(0, len(nums_slice)): 
#               if nums[i] + nums_slice[j] == target: 
#                   return [i, j+i+1]

# s = Solution()
# print(s.twoSum([3,2,4], 6))