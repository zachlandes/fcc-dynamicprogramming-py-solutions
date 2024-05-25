# timestamp: ~1:01
def gridTraveler(m: int, n: int) -> int:
    memo = {}
    def gridTraveler_helper(m: int, n: int, memo: dict) -> int:
        key = str(m) + ',' + str(n)
        if key in memo:
            return memo[key]
        elif (m == 1 and n == 1):
            return 1
        elif (m== 0 or n == 0):
            return 0
        else:
            memo[key] = gridTraveler_helper(m-1, n, memo) + gridTraveler_helper(m, n-1, memo)
            return memo[key]
    return gridTraveler_helper(m,n,memo)

print(gridTraveler(1,1)) # 1
print(gridTraveler(2,3)) # 3
print(gridTraveler(3,2)) # 3
print(gridTraveler(3,3)) # 6
print(gridTraveler(18,18)) # 2333606220