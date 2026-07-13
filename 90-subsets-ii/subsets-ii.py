class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        def backtrack(idx, cur, res, nums):
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates
                cur.append(nums[i])
                res.append(cur[:])
                backtrack(i + 1, cur, res, nums)
                cur.pop()
        backtrack(0, [], res, nums)
        return res