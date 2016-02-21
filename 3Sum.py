"""
Leetcode: https://leetcode.com/problems/3sum/
"""
from sets import Set

class Solution(object):
	
	def threeSum(self, nums):
		nums = sorted(nums)
		res = Set()
		last_index = len(nums) - 1
		for i, n in enumerate(nums):
			x = self.sum2(nums, i+1, last_index, -n)
			for t in x:
				res.add((nums[i], t[0], t[1]))
		return list(res)


	def sum2(self, n, s, e, k):
		res = []
		while s < e:
			if n[s] + n[e] < k:
				s += 1
			elif n[s] + n[e] > k:
				e -= 1
			else:
				res.append([n[s], n[e]])
				s += 1
				e -= 1
		return res

def main():
	s = Solution()
	# r = s.sum2([3,5,10,15,17], 0, 4, 25)
	r = s.threeSum([-2,0,1,1,2])
	print r

if __name__ == '__main__':
	main()