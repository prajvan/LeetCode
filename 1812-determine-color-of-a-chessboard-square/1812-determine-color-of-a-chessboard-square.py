class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        steps = abs(int(coordinates[1])-(ord(coordinates[0])-96))
        if steps%2 == 0:
            return False
        else:
            return True
        