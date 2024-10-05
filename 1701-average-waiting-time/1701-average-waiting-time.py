class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_time = customers[0][0]
        wait_time = []
        
        for cust in customers:
            chef_time = max(chef_time, cust[0])
            chef_time += cust[1]
            
            wait_time.append(chef_time-cust[0])
            
        print(wait_time)
        return sum(wait_time)/len(wait_time)