"""
@author: Luke Winter
date: 2025/03/30
"""
import numpy as np
import matplotlib.pyplot as plt


def flow_on_line(f, x0=0, t_end=10, t_steps=1000):
    t_array = np.linspace(0, t_end, num=t_steps)
    delta_t = t_end / t_steps
    x_array = np.zeros((t_steps,))
    x_array[0] = x0
    for i, t in enumerate(t_array[:-1]):
        x_array[i + 1] = x_array[i] + f(x_array[i]) * delta_t
    plt.plot(t_array, x_array)
    plt.title(f"Approximate solution for {f.__name__} at x_0={x0}")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.show()


if __name__ == '__main__':
    # plotting a solution of the one-dimensional system
    f = np.sin
    x0 = np.pi / 4
    flow_on_line(f, x0=x0)
