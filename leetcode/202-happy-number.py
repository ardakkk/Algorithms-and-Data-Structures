class Solution:
    def numSquareSum(self, n):
        squareSum = 0
        while(n):
            squareSum += (n % 10) * (n % 10)
            n = int(n / 10)
        return squareSum

    def isHappy(self, n: int) -> bool:
        # initialize slow
        # and fast by n
        slow, fast = n
        while(True):

            # move slow number
            # by one iteration
            slow = self.numSquareSum(slow)

            # move fast number
            # by two iteration
            fast = self.numSquareSum(self.numSquareSum(fast))
            if(slow != fast):
                continue
            else:
                break

        # if both number meet at 1,
        # then return true
        return (slow == 1)