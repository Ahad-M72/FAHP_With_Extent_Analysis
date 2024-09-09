import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'path/to/your/file.csv'
data = pd.read_csv(file_path)

# Determine the number of items (N) based on the number of rows
num_rows = data.shape[0]
N = int((1 + np.sqrt(1 + 8 * num_rows)) / 2)
print(f"Number of items (N): {N}")

# Define the base values
base_values = {
    'l': [8, 7, 6, 5, 4, 3, 2, 1, 1, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10],
    'm': [9, 8, 7, 6, 5, 4, 3, 2, 1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9],
    'u': [10, 9, 8, 7, 6, 5, 4, 3, 1, 1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8]
}

# Function to calculate weighted geometric means
def calculate_weighted_geom_mean(row, base_keys):
    results = {}
    exponent_sum = sum(row)
    for key in base_keys:
        product = np.prod([pow(base, exp) for base, exp in zip(base_values[key][:len(row)], row)])
        results[key] = pow(product, 1/exponent_sum)
    return results

# Calculating all l_i, m_i, u_i values
results = {'l': {}, 'm': {}, 'u': {}}
index = 1
for i in range(N):
    for j in range(i+1, N):
        row = data.iloc[index-1]
        result = calculate_weighted_geom_mean(row, ['l', 'm', 'u'])
        for key in results:
            results[key][f'{key}_{index}'] = result[key]
        index += 1

# Create the fuzzy matrix
labels = list('ABCDEFGHIJ'[:N])
cols = pd.MultiIndex.from_product([labels, ['l', 'm', 'u']])
df = pd.DataFrame(index=labels, columns=cols, dtype=float)

# Fill the matrix
index = 1
for i, row_label in enumerate(labels):
    for j, col_label in enumerate(labels):
        if i == j:
            df.loc[row_label, (col_label, 'l')] = 1
            df.loc[row_label, (col_label, 'm')] = 1
            df.loc[row_label, (col_label, 'u')] = 1
        elif i < j:
            for key in ['l', 'm', 'u']:
                df.loc[row_label, (col_label, key)] = results[key][f'{key}_{index}']
                inverse_key = 'l' if key == 'u' else 'u' if key == 'l' else 'm'
                df.loc[col_label, (row_label, key)] = 1 / results[inverse_key][f'{inverse_key}_{index}']
            index += 1

# Print the fuzzy integrated matrix
print("\nFuzzy Integrated Matrix:")
print(df.to_string())

# **Insert new code here for calculating CR_m and CR_g using provided RI values**
RI_m_dict = {1: 0, 2: 0, 3: 0.489, 4: 0.7937, 5: 1.072, 6: 1.1996, 7: 1.2874, 8: 1.341, 9: 1.3793, 10: 1.4095}
RI_g_dict = {1: 0, 2: 0, 3: 0.1796, 4: 0.2627, 5: 0.3597, 6: 0.3818, 7: 0.409, 8: 0.4164, 9: 0.4348, 10: 0.4455}

# Calculate CR_m
X = df.xs('m', axis=1, level=1)
Y = X.div(X.sum(axis=0), axis=1)
Z = Y.mean(axis=1)
M = X.dot(Z)
Lambdas_m = M.div(Z)
Lambda_max_m = Lambdas_m.mean()
CI_m = (Lambda_max_m - N) / (N - 1)
CR_m = CI_m / RI_m_dict[N]

# Calculate CR_g
W = np.sqrt(df.xs('l', axis=1, level=1) * df.xs('u', axis=1, level=1))
D = W.div(W.sum(axis=0), axis=1)
H = D.mean(axis=1)
Q = W.dot(H)
Lambdas_g = Q.div(H)
Lambda_max_g = Lambdas_g.mean()
CI_g = (Lambda_max_g - N) / (N - 1)
CR_g = CI_g / RI_g_dict[N]

# Print CR_m and CR_g values
print(f"\nCR_m: {CR_m:.4f}, CR_g: {CR_g:.4f}")

# ----------------------------------------------------------------
# Step 1: Calculate the Synthetic Extent Values
# Your existing code for Steps 1, 2, 3, 4 continues here...
# Step 1: Calculate the Synthetic Extent Values
s_values = {}
total_u = df.xs('u', axis=1, level=1).sum().sum()
total_m = df.xs('m', axis=1, level=1).sum().sum()
total_l = df.xs('l', axis=1, level=1).sum().sum()

for label in labels:
    l_i = df.xs('l', axis=1, level=1).loc[label].sum() / total_u
    m_i = df.xs('m', axis=1, level=1).loc[label].sum() / total_m
    u_i = df.xs('u', axis=1, level=1).loc[label].sum() / total_l
    s_values[label] = {'l': l_i, 'm': m_i, 'u': u_i}

# Print the synthetic extent values
print("\nSynthetic Extent Values (S_i):")
for label, s_value in s_values.items():
    print(f"S_{label} = (l: {s_value['l']:.4f}, m: {s_value['m']:.4f}, u: {s_value['u']:.4f})")

# Step 2: Calculate the Degree of Possibility
def degree_of_possibility(s_i, s_k):
    if s_i['m'] >= s_k['m']:
        return 1
    elif s_k['l'] > s_i['u']:
        return 0
    else:
        return (s_k['l'] - s_i['u']) / ((s_i['m'] - s_i['u']) - (s_k['m'] - s_k['l']))

v_matrix = pd.DataFrame(index=labels, columns=labels, dtype=float)

for i in labels:
    for j in labels:
        if i != j:
            v_matrix.loc[i, j] = degree_of_possibility(s_values[i], s_values[j])

# Print the degree of possibility matrix
print("\nDegree of Possibility Matrix (V(S_i >= S_k)):")
print(v_matrix.to_string())

# Step 3: Derive the Priority Weights
d_values = {}
for label in labels:
    d_values[label] = min(v_matrix.loc[label].drop(label))

# Print the priority weights
print("\nPriority Weights (d'(A_i)):")
for label, d_value in d_values.items():
    print(f"d'({label}) = {d_value}")

# Step 4: Normalize the Weights
total_d = sum(d_values.values())
normalized_weights = {label: d_values[label] / total_d for label in labels}

# Print the normalized weights
print("\nNormalized Weights:")
for label, weight in normalized_weights.items():
    print(f"{label}: {weight:.4f}")
