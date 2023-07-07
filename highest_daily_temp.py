# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
  
# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class HighestDailyTemp:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # initialize the array as all zeroes
        # same size as the input array
        output_ra = [0] * len(temperatures)
        
        # later stack will be made up of tuples [temp,index]
        # stack[-1] is end of the array (remember stacks
        # pop from the end) and [0] is the temperature
        stack = []

        # loop through the array with i as index counter
        # temp is the actual temperature number
        for i, temp in enumerate(temperatures):
            
            # while stack is not null
            # while the current temp is LARGER than temp
            # on top of the stack
            while stack and temp > stack[-1][0]:
                
                # pop the item, get the temp and index
                stack_temp, stack_index = stack.pop()
                
                # figure out the difference in days
                # i is current day in array, stack_index
                # is the most recently popped
                output_ra[stack_index] = (i - stack_index)
            
            # don't forget this part
            # you need to add temps as you move right
            # in the array
            stack.append([temp, i])
        
        # return your result
        return output_ra
