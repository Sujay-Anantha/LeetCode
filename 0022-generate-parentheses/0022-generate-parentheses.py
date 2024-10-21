class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # If the current string is of the required length, add it to the results
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an open parenthesis if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a close parenthesis if it would not exceed the number of open parentheses
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Start the backtracking process
        backtrack("", 0, 0)
        return result