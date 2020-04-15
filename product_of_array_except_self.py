'''

Product of Array Except Self
Ref: https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1, return an array output 
such that output[i] is equal to the product of all the elements of nums 
except nums[i].

Example:
--------
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: 
-----------
It's guaranteed that the product of the elements of any prefix 
or suffix of the array (including the whole array) fits in a 32 bit integer.

Note:
----- 
Please solve it without division and in O(n).

Follow up:
----------
Could you solve it with constant space complexity? (The output array does not 
count as extra space for the purpose of space complexity analysis.)
'''

__author__ = ['Minh-Tan Dinh']

class Solution_1:
    ''' Time Complexity: O(N), Space Complexity: O(N) '''
    def productExceptSelf(self, nums):
        l2r = []
        r2l = []
        
        # Left to right
        tmp = 1
        for i in range(len(nums)):
            tmp *= nums[i]
            l2r.append(tmp)
        
        # Right to left
        tmp = 1
        for i in reversed(range(len(nums))):
            tmp *= nums[i]
            r2l = [tmp] + r2l
        
        # Get result 
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(r2l[i+1])
            elif i == len(nums) - 1:
                res.append(l2r[i-1])
            else:
                res.append(l2r[i-1] * r2l[i+1])
        
        return res


class Solution_2:
    ''' Time Complexity: O(N), Space Complexity: O(1) '''
    def productExceptSelf(self, nums):
        res = []
        
        # Build the l2r arr first
        tmp = 1
        for i in range(len(nums)):
            tmp *= nums[i]
            res.append(tmp)
        
        # Iter res from right to left
        tmp = 1
        for i in reversed(range(len(nums))):
            if i == 0:
                res[i] = tmp
            else:
                res[i] = res[i-1] * tmp 
            tmp *= nums[i]
            
        return res


if __name__ == "__main__":
    input = [1,2,3,4]
    expected_output = [24,12,8,6]

    solver_1 = Solution_1()
    solver_2 = Solution_2()

    output_1 = solver_1.productExceptSelf(input)
    output_2 = solver_2.productExceptSelf(input)

    # Check 
    assert expected_output == output_1
    assert expected_output == output_2


