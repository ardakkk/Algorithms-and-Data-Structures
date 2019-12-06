# Time: O(1)
# Space: O(1)
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map:
            self.nums.append(val)
            self.map[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        else:
            idx_of_val_to_remove = self.map[val]
            last = self.nums[-1]
            self.map[last] = idx_of_val_to_remove

            # Swap values at last index and index of value to remove
            self.swap(self.nums, idx_of_val_to_remove, len(self.nums) - 1)
            self.nums.pop()
            del self.map[val]

            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return self.nums[random.randint(0, len(self.nums) - 1)]

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()