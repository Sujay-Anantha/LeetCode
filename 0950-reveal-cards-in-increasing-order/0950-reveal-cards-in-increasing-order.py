class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
         # Step 1: Sort the deck in increasing order
        deck.sort()
        
        # Step 2: Use deque to simulate the reverse process
        queue = deque()
        
        # Start from the largest card to the smallest
        for card in reversed(deck):
            if queue:
                # Simulate the process: move the last card to the bottom of the deck
                queue.appendleft(queue.pop())
            # Place the current card on top of the deck
            queue.appendleft(card)
        
        # Convert deque back to list
        return list(queue)