class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province_count = 0
        visited_cities = set()

        n = len(isConnected)

        def dfs(city: int) -> None:
            
            #base case

            #check neighbors
            for other_city in range(n):
              #if neighbor is connected to the city and neighbor is unvisited
              if isConnected[city][other_city] == 1 and other_city not in visited_cities:
                visited_cities.add(other_city)
                #run dfs on neighbor
                dfs(other_city)
            return
        for city in range(n):
                if city not in visited_cities:
                    visited_cities.add(city)
                    dfs(city)
                    province_count += 1

        return province_count