import matplotlib.pyplot as plt

# Years
years = ['2020', '2021', '2022', '2023', '2024']

# Number of people recruited each year
recruits = [100, 120, 150, 130, 160]

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(years, recruits, color='skyblue', edgecolor='grey', linewidth=1.5)

# Adding labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Recruits', fontsize=12)
plt.title('Recruitment Trend (2020-2024)', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Adding value labels on top of each bar
for i in range(len(years)):
    plt.text(i, recruits[i] + 5, str(recruits[i]), ha='center', va='bottom', fontsize=10)

# Removing the top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Displaying the graph
plt.tight_layout()
plt.show()
