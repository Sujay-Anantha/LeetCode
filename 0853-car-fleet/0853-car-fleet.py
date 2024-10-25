class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up positions and speeds, and calculate the time to reach the target
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        fleets = 0
        curr_time = 0
        
        # Iterate over the times from the closest car to the furthest
        for time in times:
            # If a car takes more time than the current time, it forms a new fleet
            if time > curr_time:
                fleets += 1
                curr_time = time
        
        return fleets
