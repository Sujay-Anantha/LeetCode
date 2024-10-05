class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_time = 0  # Tracks when the chef will finish serving the current customer
        total_wait_time = 0  # Accumulates the total waiting time
        
        for cust in customers:
            arrival, prep_time = cust
            
            # Update chef's available time: if the chef is idle, start when the customer arrives
            chef_time = max(chef_time, arrival)
            
            # Calculate the total time the customer waits (prep time + any idle time)
            total_wait_time += (chef_time + prep_time - arrival)
            
            # Update when the chef will be available next
            chef_time += prep_time
        
        # Return the average waiting time
        return total_wait_time / len(customers)