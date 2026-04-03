# def is_a_pal(x: str) -> bool:
#     i: int = 0
#     while i <= len(x)/2:
#         if x[i] != x[len(x) - 1 - i]:
#             return False
#         i += 1
#     return True

def is_a_pal(x: str) -> bool:
    return x == x[::-1]


# def palyndrom_min(s: str) -> int:
#     memo = {}

#     def solve(rest: str) -> int:
#         if rest in memo:
#             return memo[rest]

#         if is_a_pal(rest):
#             return 0

#         best = float("inf")

#         for i in range(1, len(rest)):
#             left = rest[:i]
#             if is_a_pal(left):
#                 best = min(best, 1 + solve(rest[i:]))

#         memo[rest] = best
#         return best

#     return solve(s)

# def palyndrom_min(s: str) -> int:
#     n = len(s)
#     dp = [i for i in range(n)]

#     for i in range(n):
#         left = r = i
#         while (left >= 0) and (r < n) and (s[left] == s[r]):
#             dp[r] = min(dp[r], 0 if left == 0 else dp[left - 1] + 1)
#             left -= 1
#             r += 1
#         left, r = i, i + 1
#         while left >= 0 and r < n and s[left] == s[r]:
#             dp[r] = min(dp[r], 0 if left == 0 else dp[left - 1] + 1)
#             left -= 1
#             r += 1
#     return dp[-1]

# def palyndrom_min_slices(s: str) -> int:
#     n = len(s)
#     dp = [float("inf")] * (n + 1)
#     print(dp)
#     dp[0] = -1  # astuce : évite de compter une coupure en trop
#     print(dp)

#     for i in range(1, n + 1):
#         for j in range(i):
#             sub = s[j:i]           # slice vers l'avant
#             if sub == sub[::-1]:   # slice vers l'arrière
#                 dp[i] = min(dp[i], dp[j] + 1)

#     return dp[n]

def palyndrom_min_slices(s: str) -> int:
    n = len(s)
    dp = [float("inf")] * (n + 1)
    dp[0] = -1

    for i in range(1, n + 1):
        for j in range(i):
            sub = s[j:i]
            if sub == sub[::-1]:
                print('i:', i, '; dp[i]:', dp[i], '; dp[j] + 1:', dp[j] + 1)
                dp[i] = min(dp[i], dp[j] + 1)
                print(dp)
    return dp[n]


def pal_splice(s: str) -> int:
    r = len(s)
    dp = [float('inf')] * (r + 1)
    dp[0] = -1
    for i in range(1, r + 1):
        for j in range(i):
            sub = s[j:i]
            if sub == sub[::-1]:
                print('sub', sub, dp, 'min: ', min(dp[i], dp[j] + 1))
                dp[i] = min(dp[i], dp[j] + 1)
    return int(dp[r])

print(palyndrom_min_slices('yabcb'))
