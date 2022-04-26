import matplotlib.pyplot as plt
import numpy as np
import math

ValueFromTable = input("Enter value from the table: ")
changes = True
n = 100
np.random.seed()
e = input("Enter expected value: ")
s = input("Enter arithmetic mean deviation: ")
x = np.random.normal(e, s, n)

print(x)

minValue = x.min()
maxValue = x.max()
average_Value = sum(x) / n
dispersionValue = sum((i - average_Value) ** 2 for i in range(n)) / n
sValue = n * dispersionValue / (n - 1)

print(maxValue)
print(minValue)
print(average_Value)
print(sValue)
print((maxValue - average_Value) / sValue)
print((average_Value - minValue) / sValue)

fig, ax = plt.subplots()
ax.plot(x, marker="o", linestyle='')
plt.show()

while changes:
    if ((maxValue - average_Value) / sValue) > ValueFromTable:
        x.max = average_Value
        maxValue = max(x)
        changes = True
        print("change was")
    else:
        changes = False
    if ((average_Value - minValue) / sValue) > ValueFromTable:
        x.min = average_Value
        minValue = min(x)
        changes = True
        print("change was")
    else:
        changes = False
    ax.plot(x, marker="o", linestyle='')
    plt.show()

fig, ax = plt.subplots()
ax.plot(x, marker="o", linestyle='')
plt.show()
