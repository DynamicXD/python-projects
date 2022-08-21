import matplotlib.pyplot as plt
labels = ["Tamil", "English", "Maths", "Physics", "Chemistry", "Computer"]
usage = [79.8, 67.3, 77.8, 68.4, 70.2, 88.5]
y = range(len(labels))
plt.bar(y, usage)
plt.xticks(y, labels)
plt.ylabel("Range")
plt.title("Marks")
plt.show()
