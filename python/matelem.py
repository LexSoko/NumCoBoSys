import numpy as np
from scipy.sparse import lil_matrix
from such import such
from tabcoord import tabcoord
from create2 import create2
from tqdm import tqdm
def matelem(Sz, Jz, Jp, Nx, Ny):
    """
    Calculate matrix elements for a Heisenberg magnet.

    Parameters:
        Sz: Total spin projection along z-axis.
        Jz: Coupling constant along z-axis.
        Jp: Coupling constant for spin-flip terms.
        Nx, Ny: Dimensions of the spin lattice.

    Returns:
        result: Sparse Hamiltonian matrix.
        basis: Spin configuration basis.
    """
    print("1")
    lattice, nn = tabcoord(Nx, Ny, periodic=1)

    # Initialize variables
    n = Nx * Ny // 2 - Sz
    list_ = sum(2**(i - 1) for i in range(1, Nx * Ny // 2 + Sz + 1))
    pos = [Nx * Ny // 2 + Sz + i for i in range(1, n + 1)]

    # Generate basis
    print("2")
    basis = create2(list_, pos, n)
    N = basis.bit_length()
    print("3")
    # Sparse Hamiltonian matrix
    H = lil_matrix((N, N), dtype=np.float64)

    # Diagonal elements
    for i in tqdm(range(N),desc="diagonal"):
        st = basis[i]
        diag_sum = sum(
            (2 * ((st >> (nn[k, 0] - 1)) & 1) - 1) * (2 * ((st >> (nn[k, 1] - 1)) & 1) - 1)
            for k in range(len(nn))
        )
        H[i, i] = Jz / 4 * diag_sum

    # Off-diagonal elements (spin flips)
    for i in tqdm(range(N),desc="offdiagonal"):
        for k in range(len(nn)):
            l, m = nn[k, 0], nn[k, 1]
            bitl = (basis[i] >> (l - 1)) & 1
            bitm = (basis[i] >> (m - 1)) & 1
            if bitl != bitm:
                state = basis[i] ^ (1 << (l - 1)) ^ (1 << (m - 1))  # Flip spins
                y = such(basis, state, 0, N - 1)
                if y != 0:
                    H[y - 1, i] += Jp / 2

    return H, basis

H, base = matelem(1,1,1,2,2)
print(H)
print(base)
import matplotlib.pyplot as plt
plt.matshow(H)
plt.show()