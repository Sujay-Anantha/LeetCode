class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        white= ['a2','a4','a6','a8','b1','b3','b5','b7','c2','c4','c6','c8','e2','e4','e6','e8','g2','g4','g6','g8',
            'd1','d3','d5','d7','f1','f3','f5','f7','h1','h3','h5','h7']
            
        black = [ 'b2','b4','b6','b8','a1','a3','a5','a7','d2','d4','d6','d8','f2','f4','f6','f8','h2','h4','h6','h8',
            'c1','c3','c5','c7','e1','e3','e5','e7','g1','g3','g5','g7']
        
        
        if coordinate1 in white and coordinate2 in black:
            return False
    
        if coordinate1 in black and coordinate2 in white:
            return False
        
        return True