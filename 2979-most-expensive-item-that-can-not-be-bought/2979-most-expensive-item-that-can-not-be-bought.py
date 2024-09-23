class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        #primes: 2,3,5,7,11,13
        return (primeOne * primeTwo) - primeOne - primeTwo
            
        