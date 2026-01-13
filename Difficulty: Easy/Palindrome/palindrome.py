class Solution:
    def isPalindrome(self, n):
		# code here
		reverse=0
		palindrome=n
		while n>0:
		    last=n%10
		    reverse=reverse*10+last
		    n//=10
		return palindrome==reverse
		    