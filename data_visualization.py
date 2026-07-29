import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Sample Dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [72, 88, 95, 67, 80],
    "Study_Hours": [2, 4, 6, 3, 5]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("sample_data.csv", index=False)

print("Dataset:")
print(df)

# --------------------------
# Scatter Plot
# --------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.savefig("output/scatter_plot.png")
plt.show()

# --------------------------
# Bar Chart
# --------------------------
plt.figure(figsize=(6,4))
plt.bar(df["Student"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("output/bar_chart.png")
plt.show()

# --------------------------
# Line Chart
# --------------------------
plt.figure(figsize=(6,4))
plt.plot(df["Student"], df["Marks"], marker="o")
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.savefig("output/line_chart.png")
plt.show()

print("\nAll charts created successfully!")