class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range for k
        left, right = 1, max(piles)
        
        # Binary search for the minimum k
        while left < right:
            mid = (left + right) // 2
            # Calculate total hours required to eat all bananas at speed mid
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid  # Equivalent to math.ceil(pile / mid)
            
            # Check if Koko can finish within h hours with this speed
            if hours <= h:
                right = mid  # Try a smaller speed
            else:
                left = mid + 1  # Increase the speed

        return left  # left will be the minimum speed at which Koko can eat all the bananas 
            
            
            
            
            
        