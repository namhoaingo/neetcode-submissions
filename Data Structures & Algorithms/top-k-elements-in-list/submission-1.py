import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store as tupple, {} means set, () means tupple
        # should be [(count, number)]
        result = [];
        counting_dictionary = defaultdict(int)     
        heapq.heapify(result)
        for number in nums:
            print(f"Number is {number}")            
            counting_dictionary[number] += 1
        
        for number, count in counting_dictionary.items():
            heapq.heappush(result, (count, number))
            if len(result) > k:
                print(f"len of result {len(result)}")                
                popout = heapq.heappop(result)       
                print(f"popped out count {popout[0]} and number {popout[1]}")         
            
                print(*(f"result count {count}, and number {number}" for count, number in result), sep="\n")     
        return [number for count, number in result]
        
       