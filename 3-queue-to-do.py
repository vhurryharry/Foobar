

def solution(start, length):

    def findXOR(n):
        mod = n % 4

        if mod == 0:
            return n
        elif mod == 1:
            return 1
        elif mod == 2:
            return n + 1
        else:
            return 0

    def findXORLR(l, r):
        return findXOR(l - 1) ^ findXOR(r)

    result = 0

    for i in range(length):
        result ^= findXORLR(start + i * length, start +
                            i * length + length - i - 1)

    return result


print(solution(17, 4))
# print(solution(2000000000, 2000000000))
