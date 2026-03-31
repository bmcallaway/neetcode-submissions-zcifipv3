class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #38/1 

        #res[0]:1,res[1]:4 res[2]:1, res[3]:2, res[4]:1

        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while(stack and t > stack[-1][0]):
                pair = stack.pop()
                result[pair[1]] = i - pair[1]
            stack.append([t, i])

        return result