class Solution:
	def reverseSubArray(self,arr,l,r):
		if l>=r:
		    return arr
		arr[l-1],arr[r-1]=arr[r-1],arr[l-1]
		return self.reverseSubArray(arr,l+1,r-1)
		