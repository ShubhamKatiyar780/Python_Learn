import pandas as pd
data = pd.DataFrame({
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
})
print(data)
print(f"This is the current version of pandas: {pd.__version__}")


# Create a simple Pandas Series from a list
data1 = [1,7,2, 5]
# Create your own labels
data2 = pd.Series(data1, index=["A", "B", "C", 'D'])
print(data2)
print(data2["B"])
# Create a simple Pandas Series from a dictionary
data3 = pd.Series({"day1": 420, "day2": 380, "day3": 390})
print(data3)
