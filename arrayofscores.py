import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
max_score = max(scores)
min_score = min(scores)

average = total / len(scores)

print("Scores:", scores)
print("Maximum:", max_score)
print("Minimum:", min_score)
print("Sum:", total)
print("Average:", average)   
