class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tupple with number and the original index, sort by number
        sorted_nums = []
        sorted_nums = sorted((num, index) for index, num  in enumerate(nums));
        index_i = 0
        index_j = len(nums) - 1
        number_at_i = 0
        number_at_j = 0
        for counter in range(0, len(nums)):            
            print(f"index_i {index_i} index_j {index_j}")
            print(f"number at index_i {sorted_nums[index_i]}" )
            print(f"number at index_j {sorted_nums[index_j]}" )

            if sorted_nums[index_i][0] + sorted_nums[index_j][0] == target:
                return sorted([sorted_nums[index_i][1], sorted_nums[index_j][1]])                
            elif sorted_nums[index_i][0] + sorted_nums[index_j][0] > target:
                index_j -= 1
            else:
                index_i += 1 
        return [int]