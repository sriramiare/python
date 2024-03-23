def min_items(n,m,items):
    dp=[float('inf')]*(m+1)
    dp[0]=0
    for i in range(1,m+1):
        for j in range(n):
            if items[j]<=i:
                dp[i]=min(dp[i],dp[i-items[j]]+1)
    return dp[m] if dp[m]!=float('inf')else -1
n,m=map(int,input().split())
items=list(map(int,input().split()))
print(min_items(n,m,items))
