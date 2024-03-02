'''
Title: 238. Product of Array Except Self
Source: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def productExceptSelf_bruteforce(self, nums: List[int]) -> List[int]:
        '''
        # Title: Brute-force solution

        # Time complexity: O(N ** 2)
        # Space complexity: O(N)
        # Status: TLE
        '''
        n = len(nums)

        products = []
        for i in range(n):
            product = 1
            for j in range(n):
                if j == i:
                    continue
                product *= nums[j]
            products.append(product)

        return products

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        # Title: Brute-force solution
        
        # Intuition: 
        左からの走査と、右からの走査によって、計算する
        
        # Time complexity: O(N)
        
        # Space complexity: O(N)
        '''
        n = len(nums)

        left_product = 1
        right_product = 1
        products = [1] * n
        for i, val in enumerate(nums):
            products[i] *= left_product     # 左から、直前の要素までのproductを掛ける 
            left_product *= val             # 次に掛ける値を更新する
        
        for i in range(n-1, -1, -1):
            products[i] *= right_product    # 右から、直前の要素までの product を掛ける
            right_product *= nums[i]        # 次に掛ける値を更新する

        return products


solution = Solution()
assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]