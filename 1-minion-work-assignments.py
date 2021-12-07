from collections import Counter


def solution(data, n):
    result = []
    counts = Counter(data)

    for task in data:
        if counts[task] <= n:
            result.append(task)

    return result


print(solution([1, 2, 3], 0))
print(solution([5, 10, 15, 10, 7], 1))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
