class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_dictionary = {}
        for num in nums:
            if num in result_dictionary:
                result_dictionary[num] = result_dictionary[num] + 1
            else:
                result_dictionary[num] = 1
        return sorted(result_dictionary.keys(), key=lambda x: result_dictionary[x], reverse=True)[:k]
