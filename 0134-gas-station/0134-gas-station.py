class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, curr_sum, tot = 0, 0,0
        for i, num in enumerate(gas):
            curr_sum += num - cost[i];
            tot += num - cost[i];
            if(curr_sum < 0):
                curr_sum = 0;
                res = i + 1;
        if tot < 0 or res == len(gas):
            return -1
        return res