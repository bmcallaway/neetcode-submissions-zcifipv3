class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = sum([c for c, g in zip(customers, grumpy) if g == 0])
        added = sum([c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1])
        maxCustomers = base + added
        l = 0
        for r in range(minutes, len(customers)):
            if grumpy[r] == 1:
                added += customers[r]
            if grumpy[l] == 1:
                added -= customers[l]
            l += 1
            maxCustomers = max(maxCustomers, base + added)
        return maxCustomers



