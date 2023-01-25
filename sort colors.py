"""
Description:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #bc of constraints in the problem statement, need to use 3 pointers
        l = cur = 0 #l or left will be left boundary, cur is current
        r = len(nums) - 1 # r will be the right boundary
        """
        you iterate over the list, if cur == 0 you swap the value w/l boundary, and update l and cur pointers
        if cur == 1, you update the cur pointer
        if cur == 2, you swap the cur and r boundary and update the right boundary pointers
        """
        while cur <= r:
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            else:
                cur += 1
