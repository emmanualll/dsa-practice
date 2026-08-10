class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        permutations = ""

        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutations += str(numbers[index])
            numbers.remove(numbers[index])
        
        return permutations
        