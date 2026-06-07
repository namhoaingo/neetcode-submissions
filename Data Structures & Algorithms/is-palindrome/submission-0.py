class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # using two pointer
        pointer_left_index = 0
        pointer_right_index = len(s) - 1
        while pointer_left_index <= pointer_right_index:
            if not s[pointer_left_index].isalnum():
                pointer_left_index += 1
                continue
            elif not s[pointer_right_index].isalnum():
                pointer_right_index -= 1
                continue
            elif s[pointer_left_index].lower() == s[pointer_right_index].lower():
                pointer_left_index += 1
                pointer_right_index -= 1
            else:
                return False
        
        return True