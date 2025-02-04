from numpy import *
c=array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original Matrix")
print(c)
# ---------Using triu (triangular upper) method---------
# upper_triangular = triu(c)
# print("Upper Triangular Matrix:")
# print(upper_triangular)
# ---------Using tril (triangular lower) method---------
# Lower_triangular = tril(c)
# print("Lower Triangular Matrix:")
# print(Lower_triangular)

rows, cols = c.shape
# for i in range(rows):
#     for j in range(cols):
#         if i > j:
#             c[i][j] = 0
# print("Upper Triangular Matrix:")        
# for i in c:
#     print(i)

for i in range(rows):
    for j in range(cols):
        if i < j:
            c[i][j] = 0
print("Lower Triangular Matrix:")        
for i in c:
    print(i)

