from math import factorial as fac
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(formatter={'float': lambda x: str(x)})

K=30
# initial probability vector
p_0 = np.array([1/K]*K)


def binomial(x, y):
    try:
        return fac(x) / fac(y) / fac(x - y)
    except ValueError:
        return 0

indices = [i for i in range(1,K+1)]
    
fig, axs = plt.subplots(3,2)
fig.suptitle("PMFs plotted for K=30, various values of M")
axs[0,0].plot(indices, p_0,".")
axs[0,0].set_title("m=0")
axs[0,0].set_xlabel("s")
axs[0,0].set_ylabel("P_0(s)", rotation=0, labelpad=20)
def plot_case(m, position):

    M = m
    shape = K, K
    neg_pascal = np.empty(shape)
    pascal = np.empty(shape)
    D = np.zeros(shape)

    for i in range(K):
        for j in range(K):
            if i == j:
                D[i,j] = (1/(i+1))**M
            if i > j:
                neg_pascal[i,j] = 0
                pascal[i,j] = 0
            else:
                neg_pascal[i,j] = (-1)**(i+j) * binomial(j,i)
                pascal[i,j] = binomial(j,i)

    final_matrix = neg_pascal @ D @ pascal
    final_p_vector = final_matrix @ p_0

    plot_values = [ final_p_vector[i] for i in range(K)]
    print(sum(plot_values))

    axs[position].plot(indices, plot_values,".")
    axs[position].set_title(f"m={m}")
    axs[position].set_xlabel("s")
    axs[position].set_ylabel(f"P_{m}(s)", rotation=0, labelpad=20)

def show_images():
    plot_case(1, (1,0))
    plot_case(2, (2,0))
    plot_case(3, (0,1))
    plot_case(4, (1,1))
    plot_case(5, (2,1))

    fig.subplots_adjust(hspace=1.0)
    plt.xticks(range(0,K+1,2))
    plt.show()

show_images()
