import math

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        if targetCapacity == 0:
            return True
        
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        # Check if the target capacity is divisible by the gcd of jug capacities
        return targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0

# Example usage:
solution = Solution()
print(solution.canMeasureWater(3, 5, 4))  # Output: True
