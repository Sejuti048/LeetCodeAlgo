class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = 0
        while (low < high):
            mid = low + ((high - low) // 2)
            if isBadVersion(mid) == True:
                high = mid
            else:
                low = mid + 1

        return low