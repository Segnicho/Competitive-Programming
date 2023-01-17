class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = 0
        nwArr = arr[:]
        for i in range(n-1,-1,-1):
            nwArr[i] = mx
            mx = max(arr[i], mx)
        nwArr[-1] = -1
        return nwArr
