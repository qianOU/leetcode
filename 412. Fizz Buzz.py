class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1, n+1)]
        for i in range(1, n+1):
            if i%15 == 0:
                ans[i-1] = "FizzBuzz"
                continue
            elif i%5 == 0:
                ans[i-1] = 'Buzz'
                continue
            elif i%3 == 0:
                ans[i-1] = 'Fizz'
        return ans