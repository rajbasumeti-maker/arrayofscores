import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
max_score = max(scores)
min_score = min(scores)

average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)   