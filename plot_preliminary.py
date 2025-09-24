import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Mantamonis_bacterial_contamination_analysis(1).xlsx")

counts = df["Preliminary Verdict:"].value_counts()

plt.figure(figsize=(8,6))
counts.plot(kind="bar", color='red')

plt.title("Counts of Preliminary Verdict:")
plt.xlabel("Preliminary Verdict:")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("preliminary_classification.png")
print("Saved figure as preliminary_classification.png")

