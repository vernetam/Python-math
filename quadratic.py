'''
Quadratic calculator and plotting
'''
import matplotlib.pyplot as plt

x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y_values = []
for x in x_values:
    y = x**2 + 2*x + 1
    y_values.append(y)
    print('x={0} y={1}'.format(x, y))

plt.plot(x_values,y_values)
plt.show()


















