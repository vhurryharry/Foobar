
def solution(l):
    c = [0] * len(l)
    total = 0

    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                total += c[j]

    return total


print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
