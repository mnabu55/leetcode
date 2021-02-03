'''

'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = i2 = 0
        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                i1 += 1
            else:
                pass


    def test_zip(self):
        list_a = [1,2,3]
        list_b = [1,2,3,4]

        for a, b in zip(list_a, list_b):
            print("a: {}, b: {}".format(a, b))


solution = Solution()
solution.test_zip()
