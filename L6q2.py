#this this for SE lab assignment 
#lab2 on git and git hub


#  find the maximum profit obtainable by cutting a rod
def rod_cutting(price, N):
    # dp[i] will store the maximum profit for a rod of length i
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        max_val = float('-inf')
        # Try all possible cuts j (1 to i)
        for j in range(1, i + 1):
            max_val = max(max_val, price[j - 1] + dp[i - j])
        dp[i] = max_val

    return dp[N]
# input
N = int(input("enter n :"))
price = list(map(int, input("Enter prices: ").split()))

print("Maximum obtainable value:", rod_cutting(price, N))
