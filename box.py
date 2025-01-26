# import matplotlib.pyplot as plt

# data = [3, 4, 5, 6, 7, 8, 9]

# plt.boxplot(data, vert=False)
# plt.title('Box-and-Whisker Plot')
# plt.xlabel('Value')
# plt.show()


import matplotlib.pyplot as plt

# Given data
data = [3, 4, 5, 6, 7, 8, 9]

# Creating the box-and-whisker plot
plt.figure(figsize=(10, 6))
plt.boxplot(data, vert=False, patch_artist=True, 
            boxprops=dict(facecolor="lightblue", color="blue"),
            whiskerprops=dict(color="blue"),
            capprops=dict(color="blue"),
            medianprops=dict(color="red"),
            flierprops=dict(marker='o', color='red', alpha=0.5))
plt.title('Box-and-Whisker Plot')
plt.xlabel('Value')
plt.grid(True)
plt.show()
