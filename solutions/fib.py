# timestamp: ~31 minutes
def fib(n: int) -> int:
  memo = {}

  def fib_helper(n: int, memo: dict) -> int:
    if n in memo:
      return memo[n]
    elif n <= 2:
      return 1
    else:
      memo[n] = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
      return memo[n]

  return fib_helper(n, memo)

print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025