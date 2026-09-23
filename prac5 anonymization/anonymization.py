import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("student data.csv")

print("Original Dataset")
print(df)

# data masking

df_masked = df.copy()

df_masked["Phone"] = (
    df_masked["Phone"]
    .astype(str)
    .str[:2] + "******"
)

print("\nData after masking phone numbers")
print(df_masked)


# k-anonymity

df_k = df.drop(columns=["Name", "Phone"]).copy()

# generalize age into age groups
df_k["Age Group"] = (
    (df_k["Age"] // 5) * 5
).astype(str) + "-" + (
    (df_k["Age"] // 5) * 5 + 4
).astype(str)

# remove the original age
df_k = df_k.drop(columns=["Age"])

print("\nData after generalization for k-anonymity")
print(df_k)

# check combinations of quasi-identifiers
quasi_identifiers = ["Age Group", "Gender", "City", "Course"]

group_sizes = df_k.groupby(quasi_identifiers).size()

print("\nGroup sizes")
print(group_sizes)

# differential privacy

original_mean = df["Age"].mean()

# add Laplace noise
noise = np.random.laplace(loc=0, scale=1)

private_mean = original_mean + noise

print("\nDifferential Privacy")
print("Original Mean Age:", original_mean)
print("Noise Added:", noise)
print("Private Mean Age:", private_mean)