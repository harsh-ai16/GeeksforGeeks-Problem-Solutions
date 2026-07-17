class Solution:
    def largest(self, arr):
        counter=arr[0]
        for i in arr:
            if i>counter:
                counter=i
        return counter
        
