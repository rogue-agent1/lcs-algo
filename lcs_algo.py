#!/usr/bin/env python3
"""Longest common subsequence."""
import sys
def lcs(a,b):
    m,n=len(a),len(b)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]: dp[i][j]=dp[i-1][j-1]+1
            else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # Backtrace
    result=[];i,j=m,n
    while i>0 and j>0:
        if a[i-1]==b[j-1]: result.append(a[i-1]);i-=1;j-=1
        elif dp[i-1][j]>dp[i][j-1]: i-=1
        else: j-=1
    return ''.join(reversed(result))
def main():
    if "--demo" in sys.argv:
        pairs=[("ABCBDAB","BDCABA"),("AGGTAB","GXTXAYB"),("abcdef","ace")]
        for a,b in pairs:
            r=lcs(a,b)
            print(f"LCS('{a}','{b}') = '{r}' (length={len(r)})")
    elif len(sys.argv)>2: print(lcs(sys.argv[1],sys.argv[2]))
if __name__=="__main__": main()
