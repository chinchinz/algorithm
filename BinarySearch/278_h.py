# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n
        l = 1
        while l < r:
            mid = (l+r)//2
            # print(mid)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l