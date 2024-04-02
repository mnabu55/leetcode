from typing import List


class Solution:
    def hIndex_1(self, citations: List[int]) -> int:
        n = len(citations)
        max_h_index = 0

        for h_index in range(1, n + 1):
            count = 0
            for i in range(n):
                if citations[i] >= h_index:
                    count += 1
                if count >= h_index:
                    max_h_index = h_index
                    break
            if count < h_index:
                return max_h_index

        return max_h_index

    def hIndex_2(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        h_index = 0
        for i in range(n):
            if h_index + 1 <= citations[i]:
                h_index += 1

        return h_index

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)

        if n == 1 and citations[0] > 0:
            return 1
        if citations[-1] >= n:
            return n

        for i in range(n):
            if citations[i] < i + 1:
                return i

        return 0



if __name__ == '__main__':
    solution = Solution()

    citations = [3,0,6,1,5]
    expected = 3
    assert solution.hIndex(citations) == expected

    citations = [1,3,1]
    expected = 1
    assert solution.hIndex(citations) == expected
