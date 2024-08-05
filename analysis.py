import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('Part3.csv')

# Display the first few rows of the dataframe
print(df.head())

# Calculate mean, median, and mode for days_diff_reg_watch
mean_reg_watch = df['days_diff_reg_watch'].mean()
median_reg_watch = df['days_diff_reg_watch'].median()
mode_reg_watch = df['days_diff_reg_watch'].mode()[0]

# Calculate mean, median, and mode for days_diff_watch_purch
mean_watch_purch = df['days_diff_watch_purch'].mean()
median_watch_purch = df['days_diff_watch_purch'].median()
mode_watch_purch = df['days_diff_watch_purch'].mode()[0]

# Print the statistics
print(f'Mean registration to engagement: {mean_reg_watch}')
print(f'Median registration to engagement: {median_reg_watch}')
print(f'Mode registration to engagement: {mode_reg_watch}')

print(f'Mean engagement to purchase: {mean_watch_purch}')
print(f'Median engagement to purchase: {median_watch_purch}')
print(f'Mode engagement to purchase: {mode_watch_purch}')


# Plot the distributions
plt.figure(figsize=(12, 6))

# Distribution for registration to engagement
plt.subplot(1, 2, 1)
sns.histplot(df['days_diff_reg_watch'], kde=True)
plt.axvline(mean_reg_watch, color='r', linestyle='--', label=f'Mean: {mean_reg_watch:.2f}')
plt.axvline(median_reg_watch, color='g', linestyle='-', label=f'Median: {median_reg_watch:.2f}')
plt.axvline(mode_reg_watch, color='b', linestyle='-', label=f'Mode: {mode_reg_watch:.2f}')
plt.title('Distribution of Days Between Registration and Engagement')
plt.legend()

# Distribution for engagement to purchase
plt.subplot(1, 2, 2)
sns.histplot(df['days_diff_watch_purch'].dropna(), kde=True)
plt.axvline(mean_watch_purch, color='r', linestyle='--', label=f'Mean: {mean_watch_purch:.2f}')
plt.axvline(median_watch_purch, color='g', linestyle='-', label=f'Median: {median_watch_purch:.2f}')
plt.axvline(mode_watch_purch, color='b', linestyle='-', label=f'Mode: {mode_watch_purch:.2f}')
plt.title('Distribution of Days Between Engagement and Purchase')
plt.legend()

plt.tight_layout()
plt.show()
