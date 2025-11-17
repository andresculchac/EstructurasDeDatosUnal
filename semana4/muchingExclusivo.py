#AIII

import bisect

def main():
    C = int(input())
    for _ in range(C):
        line = input().strip()
        weights = [int(x) for x in line.split(', ')]
        n = len(weights)
        if n < 2:
            print(sum(weights))
            continue
        weights.sort()
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + weights[i - 1]
        total = prefix[n]
        target = total // 2
        pos = bisect.bisect_left(prefix, target, 1, n + 1)
        candidates = set()
        if 1 <= pos <= n - 1:
            candidates.add(pos)
        if 1 <= pos - 1 <= n - 1:
            candidates.add(pos - 1)
        if pos == n:
            candidates.add(n - 1)
        min_diff = float('inf')
        for k in candidates:
            diff = abs(2 * prefix[k] - total)
            if diff < min_diff:
                min_diff = diff
        print(min_diff)

main()


