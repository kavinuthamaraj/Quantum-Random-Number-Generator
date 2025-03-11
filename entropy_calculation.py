import math

# Observed frequencies of each binary outcome
counts = {
    "000": 123,
    "001": 141,
    "010": 117,
    "011": 122,
    "100": 118,
    "101": 132,
    "110": 107,
    "111": 140
}

total_runs = sum(counts.values())

# Probabilities
probabilities = [count / total_runs for count in counts.values()]

#Shannon entropy
entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)

print(f"Shannon Entropy: {entropy:.4f} bits")
