def getTotalX(a, b):
    # Write your code here
    b.sort()
    all_factors = []
    factors = []
    answers = []
    for divisor in range(1, int(b[-1]) + 1):
        all_factors.append(divisor)
    for factor in all_factors:
        results = map(lambda nums: nums % factor == 0, b)
        if list(results).count(True) == len(b):
            factors.append(factor)
    for answer in factors:
        results = map(lambda nums: answer % nums == 0, a)
        if list(results).count(True) == len(a):
            answers.append(answer)
    print(answers)
    return len(answers)
test1 = [1]
test2 = [100]
print(getTotalX(test1, test2))
