def nthSuperUglyNumber(n: int, primes: list[int]) -> int:
    dp = [0] * n
    dp[0] = 1

    # one pointer per prime, all start at index 0
    pointers = [0] * len(primes)

    for i in range(1, n):
        # candidate next value for each prime
        candidates = [dp[pointers[j]] * primes[j] for j in range(len(primes))]

        nxt = min(candidates)
        dp[i] = nxt

        # advance ALL pointers that produced the min (dedup)
        for j in range(len(primes)):
            if candidates[j] == nxt:
                pointers[j] += 1

    return dp[n - 1]
