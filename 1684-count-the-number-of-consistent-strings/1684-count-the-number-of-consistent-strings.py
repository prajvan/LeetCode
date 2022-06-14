class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count  = 0
        allowed_map = set(allowed)
        for word in words:
            for letter in word:
                if letter not in allowed_map:
                    count+=1
                    break 
        return len(words)-count
        