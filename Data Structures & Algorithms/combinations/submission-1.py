class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    
    #1 i=0, val=1, stack=[1] 
        #2 i=1, val=2 stack=[1,2]
        
        #n i=1, val=2, stack=[1]
            #3 i=1 val=2, stack=[1,3]
                #4 i=2, val=4 stack=[1,3] (added)

            #n i=1, val=2, stack=[1]
                #3 i=2, val=3
            

    #n
        #2

        #n
            #3
            
            #n

        res = []
        stack = []

        def backtrack( val):
            nonlocal res, stack
            if val > n:
                if len(stack) == k:
                    res.append(stack[:])
                return
            stack.append(val)
            backtrack(val + 1)
            stack.pop()
            backtrack(val + 1)

        backtrack(1)
        return res
