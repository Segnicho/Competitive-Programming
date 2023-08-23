class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = []
        res = []
        def subsets(i= 0, temp=[]):
            if i >= n:
                ky = temp[:]
                res.append(ky)
                return
            temp.append(nums[i])
            st.append(nums[i])
            
            subsets(i+1, temp)
            temp.pop()
            st.pop()
            if nums[i] not in st:
                subsets(i+1, temp)

        subsets()
        return res
    