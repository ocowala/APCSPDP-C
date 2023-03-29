import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv("data.csv")
value = data["Sector"]
print(value)
dict1 = {}
for val in value:
    if val in dict1.keys():
        dict1[val] += 1
    else:
        dict1[val] = 1
print(dict1)
keys = dict1.keys()
values = dict1.values()

plt.bar(keys, values)
plt.show()
