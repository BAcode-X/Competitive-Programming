class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()
        return sum(salary[1:-1]) / (n - 2)
