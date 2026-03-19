class Solution:
    def getMinMax(self, arr):
        mini = arr[0]
        maxi = arr[0]
        
        for num in arr:
            if num < mini:
                mini = num
            if num > maxi:
                maxi = num
                
        return [mini, maxi]