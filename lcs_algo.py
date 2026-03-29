#!/usr/bin/env python3
"""Longest Common Subsequence / Substring. Zero dependencies."""

def lcs_subsequence(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # Reconstruct
    result = []; i, j = m, n
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]: result.append(a[i-1]); i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]: i -= 1
        else: j -= 1
    return "".join(reversed(result)) if isinstance(a, str) else list(reversed(result))

def lcs_length(a, b):
    m, n = len(a), len(b)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]: curr[j] = prev[j-1] + 1
            else: curr[j] = max(prev[j], curr[j-1])
        prev = curr
    return prev[n]

def longest_common_substring(a, b):
    m, n = len(a), len(b)
    best = 0; end_i = 0
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                curr[j] = prev[j-1] + 1
                if curr[j] > best: best = curr[j]; end_i = i
        prev = curr
    return a[end_i - best:end_i]

if __name__ == "__main__":
    print(lcs_subsequence("ABCBDAB", "BDCAB"))
