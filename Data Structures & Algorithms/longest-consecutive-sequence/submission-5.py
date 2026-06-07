class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        nums_dict = set(nums)
        if len(nums_dict) == 0:
            return 0
        max_count = 1
        for num in nums:
            # consider num is the start of sequence
            next_num = num
            counter = 1
            while next_num + counter in nums_dict and counter <= len(nums_dict):
                counter += 1
                max_count = max(max_count, counter)
            
        return max_count

        