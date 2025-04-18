# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

# Example 1:

# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]

# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# sma
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        # Initialize with numbers 1 to 1000
        initial_elements = list(range(1, 1001))
        heapq.heapify(initial_elements)
        # Correctly assign the list (now a heap)
        self.min_heap = initial_elements
        # Use a set for efficient presence tracking
        self.present_elements = set(initial_elements)

    def popSmallest(self) -> int:
        if not self.min_heap:
            # Or raise an error, depending on desired behavior when empty
            return -1 # Indicate empty or handle error appropriately

        # Use heappop to remove and return the smallest
        smallest = heapq.heappop(self.min_heap)
        # Update the tracking set
        self.present_elements.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        # Only add back if it's not currently considered present
        # Optional: Add constraint like num <= 1000 if sticking to finite idea
        if num not in self.present_elements:
            heapq.heappush(self.min_heap, num)
            self.present_elements.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)