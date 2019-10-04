# Time: (nd) | Space O(n)
def minNumberOfCoinsForChange(n, denums):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denums:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])

    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1

print(minNumberOfCoinsForChange(7, [2,4]))