#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		answer=0
		while n>0:
		    last=n%10
		    answer=answer*10+last
		    n//=10
		return answer