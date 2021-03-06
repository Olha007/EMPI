import matplotlib.pyplot as plt
import numpy as np

changes = True
ValueFromTable = input("Enter value from the table: ")
n = 100
np.random.seed()
e = input("Enter expected value: ")
s = input("Enter arithmetic mean deviation: ")
x = np.random.normal(e, s, n)
print(x)

minValue = x.min()
print(minValue)

maxValue = x.max()
print(maxValue)

average_Value = sum(x) / n
print(average_Value)

dispersionValue = sum((i - average_Value) ** 2 for i in range(n)) / n
print(dispersionValue)

sValue = n * dispersionValue / (n - 1)
print (sValue)
print((maxValue - average_Value) / sValue)
print((average_Value - minValue) / sValue)

fig, ax = plt.subplots()
ax.plot(x, marker="o", linestyle='')
plt.show()

while changes:
    if ((maxValue - average_Value) / sValue) > ValueFromTable:
        x.max = average_Value
        maxValue = max(x)
        print("Previous changes")
        changes = True
    else:
        changes = False
    if ((average_Value - minValue) / sValue) > ValueFromTable:
        x.min = average_Value
        minValue = min(x)
        print("Previous changes")
        changes = True
    else:
        changes = False
fig, ax = plt.subplots()
ax.plot(x, marker="o", linestyle='')
plt.show()
