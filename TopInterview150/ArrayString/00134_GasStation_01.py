from typing import List


class Solution:
    def canCompleteCircuit_wa(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start_pos in range(n):
            tank = 0
            count = 0
            for i in range(n):
                current_pos = (start_pos + i) % n
                new_gas = gas[current_pos]
                tank += new_gas
                if cost[current_pos] > tank:
                    break
                tank -= cost[current_pos]
                count += 1
            if count >= n:
                return start_pos
        
        return -1


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        n_station = len(gas)
        gas_tank, start_index = 0, 0
        
        for i in range(n_station):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i + 1
                gas_tank = 0
            
        return start_index


if __name__ == '__main__':
    solution = Solution()

    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    expected = 3
    assert solution.canCompleteCircuit(gas, cost) == expected


