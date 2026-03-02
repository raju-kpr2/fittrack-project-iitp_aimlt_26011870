import numpy as np

# -----------------------------
# Task 1 — Generate & Inspect
# -----------------------------
np.random.seed(42)

# Generate 5x4 array (5 students, 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))

print("Scores:\n", scores)

# Score of 3rd student in 2nd subject
print("\n3rd student, 2nd subject:", scores[2, 1])

# All scores of last 2 students
print("\nLast 2 students (all subjects):\n", scores[-2:, :])

# First 3 students, subjects 2 and 3 only
print("\nFirst 3 students, subjects 2 & 3:\n", scores[:3, 1:3])


# -----------------------------
# Task 2 — Broadcasting
# -----------------------------

# Column-wise mean (rounded to 2 decimals)
column_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise mean:", column_mean)

# Add curve [5, 3, 7, 2] using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = np.minimum(scores + curve, 100)
print("\nCurved Scores:\n", curved_scores)

# Row-wise max (best subject per student)
row_max = curved_scores.max(axis=1)
print("\nBest score per student:", row_max)


# -----------------------------
# Task 3 — Normalize & Identify
# -----------------------------

# 1. Min-max normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)
print("\nNormalized Scores:\n", normalized)


# 2. Identify student and subject index of the single highest value
# argmax returns a flat index, unravel_index converts it to (row, col)
flat_idx = normalized.argmax()
student_idx, subject_idx = np.unravel_index(flat_idx, normalized.shape)
print(f"\nHighest value at: Student {student_idx}, Subject {subject_idx}")

# 3. Boolean masking: Extract scores strictly above 90
# All scores strictly above 90 (1D array)
above_90 = curved_scores[curved_scores > 90]
print("\nScores above 90:", above_90)




