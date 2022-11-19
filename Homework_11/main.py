import numpy as np
import matplotlib.pyplot as plt

x_limit = [-50, 50]
koef = [-12, -18, 5, 10, -30]
color = "r"
x = np.arange(x_limit[0], x_limit[1], 0.1)


def func(x, a, b, c, d, e):
    return a*x**4 * np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e


extreme = []
change_dir = 1
for i in range(len(x)-1):
    if change_dir == -1:
        if func(x[i], *koef) < func(x[i+1], *koef):
            extreme.append((x[i], func(x[i], *koef)))
            change_dir = 1
    else:
        if func(x[i], *koef) > func(x[i+1], *koef):
            extreme.append((x[i], func(x[i], *koef)))
            change_dir = -1


gap = []
change_gap = 1
for i in range(len(x)-1):
    if change_gap == -1:
        if func(x[i], *koef) < 0:
            gap.append((x[i], func(x[i], *koef)))
            change_gap = 1
    if change_gap == 1:
        if func(x[i], *koef) > 0:
            gap.append((x[i], func(x[i], *koef)))
            change_gap = -1


def change_color():
    global color
    if color == "r":
        color = "g"
    else:
        color = "r"
    return color


def figure_2(x_limit, gap):
    plt.figure("График с промежутками f > 0 и f < 0")
    plt.title('График функции с  промежутками')
    plt.grid()
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('График функции')

    diap_gap = np.arange(gap[0][0], gap[0+1][0], 0.1)
    plt.plot(diap_gap, func(diap_gap, *koef), "g")

    for i in range(1, len(gap)-2):
        if gap[i][1] > -0.001:
            diap_gap = np.arange(gap[i][0], gap[i+1][0], 0.1)
            plt.plot(diap_gap, func(diap_gap, *koef), "g",)
        elif gap[i][1] < 0.001:
            diap_gap = np.arange(gap[i][0], gap[i+1][0], 0.1)
            plt.plot(diap_gap, func(diap_gap, *koef), "r--",)

    if gap[-2][1] > -0.001:
        diap_gap = np.arange(gap[-2][0], gap[-1][0], 0.1)
        plt.plot(diap_gap, func(diap_gap, *koef),
                 "g", label="Промежуток при f > 0")
    elif gap[-2][1] < 0.001:
        diap_gap = np.arange(gap[-2][0], gap[-1][0], 0.1)
        plt.plot(diap_gap, func(diap_gap, *koef),
                 "r--", label="Промежуток при f < 0")
    if gap[-1][1] > -0.001:
        diap_gap = np.arange(gap[-1][0], x_limit[1], 0.1)
        plt.plot(diap_gap, func(diap_gap, *koef),
                 "g", label="Промежуток при f > 0")
    elif gap[-1][1] < 0.001:
        diap_gap = np.arange(gap[-1][0], x_limit[1], 0.1)
        plt.plot(diap_gap, func(diap_gap, *koef),
                 "r--", label="Промежуток при f < 0")

    plt.legend(edgecolor='r')


def figure_1(x_limit, extreme):
    plt.figure("График функции")
    plt.grid()
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('График функции')

    diap = np.arange(x_limit[0], extreme[0][0], 0.1)
    plt.plot(diap, func(diap, *koef), change_color(),
             label="Промежуток возрастания")

    diap = np.arange(extreme[0][0], extreme[1][0], 0.1)
    plt.plot(diap, func(diap, *koef), change_color(),
             label="Промежуток Убывания")
    plt.plot(extreme[0][0], extreme[0][1], "bo", label="Точки перегиба")

    for i in range(1, len(extreme)-1):
        diap = np.arange(extreme[i][0], extreme[i+1][0], 0.1)
        plt.plot(diap, func(diap, *koef), change_color())
        plt.plot(extreme[i][0], extreme[i][1], "bo")

    diap = np.arange(extreme[-1][0], x_limit[1], 0.1)
    plt.plot(diap, func(diap, *koef), change_color())
    plt.plot(extreme[-1][0], extreme[-1][1], "bo")
    plt.legend(edgecolor='r')


figure_1(x_limit, extreme)
figure_2(x_limit, gap)
plt.show()
