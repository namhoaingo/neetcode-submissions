import uuid
class Solution:

    def encode(self, strs: List[str]) -> str:        
        if len(strs) == 0:
            return "emptyArray"
        encoding_text = ("→").join(strs)                    
        return encoding_text
    def decode(self, s: str) -> List[str]:
        if s == "emptyArray":
            return []
        results = s.split(("→"))        
        return results