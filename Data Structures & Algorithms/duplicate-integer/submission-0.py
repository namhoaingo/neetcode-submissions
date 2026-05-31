class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_value = set(nums)
        return len(distinct_value) != len(nums)