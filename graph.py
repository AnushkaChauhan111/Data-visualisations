import matplotlib.pyplot as plt

x_values = list(range(1,5))
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
ax.set_xlabel("Numbers")
ax.set_ylabel("Cubic numbers")
ax.set_title("Number with cubic values")
ax.plot(x_values,y_values)

plt.show()