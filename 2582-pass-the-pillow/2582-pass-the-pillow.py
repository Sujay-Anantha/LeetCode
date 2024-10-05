class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Determine the number of full cycles (forward and backward)
        cycle_length = 2 * (n - 1)  # Forward and backward cycle
        time_in_cycle = time % cycle_length
        
        # If the time is within the forward direction (1 to n)
        if time_in_cycle < n:
            return time_in_cycle + 1
        
        # If the time is in the backward direction (n to 1)
        return 2 * n - time_in_cycle - 1
            
        '''
        1-2-3-4-5-6-7-8
        '''