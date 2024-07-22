class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Convert supplies list to a set for faster lookup
        supply_set = set(supplies)
        
        # Adjacency list and in-degree count for topological sorting
        graph = defaultdict(list)
        in_degree = {recipe: 0 for recipe in recipes}
        
        # Build the graph and in-degree count
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient in supply_set:
                    continue
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        
        # Queue for processing recipes with zero in-degree (no dependencies or all dependencies met)
        queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
        
        # Result list to store the recipes that can be made
        result = []
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
