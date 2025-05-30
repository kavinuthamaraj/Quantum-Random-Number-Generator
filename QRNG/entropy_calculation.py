import math

# Observed frequencies of each binary outcome
counts = {
    "000": 125,
    "001": 122,
    "010": 107,
    "011": 141,
    "100": 141,
    "101": 107,
    "110": 132,
    "111": 125
}

total_runs = sum(counts.values())

# Probabilities
probabilities = [count / total_runs for count in counts.values()]

#Shannon entropy
entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)

print(f"Shannon Entropy: {entropy:.4f} bits")
