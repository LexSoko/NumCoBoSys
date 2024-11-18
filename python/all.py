import numpy as np
from scipy.sparse import lil_matrix

def matelem(Sz, Jz, Jp, Nx, Ny):
    """
    Calculate matrix elements for the Heisenberg magnet.
    
    Parameters:
        Sz (int): Total spin in the z-direction.
        Jz (float): Interaction strength in z-direction.
        Jp (float): Interaction strength in x-y plane.
        Nx (int): Number of sites in x-direction.
        Ny (int): Number of sites in y-direction.
    
    Returns:
        tuple: Sparse Hamiltonian matrix and basis (list of bit patterns).
    """
    lattice, nn = tabcoord(Nx, Ny, 1)  # Generate lattice and neighbor pairs
    
    # Initialize the list of basis states
    n = Nx * Ny // 2 - Sz
    list_ = sum(2 ** (i - 1) for i in range(1, Nx * Ny // 2 + Sz + 1))
    pos = [Nx * Ny // 2 + Sz + i for i in range(1, n + 1)]
    
    # Create basis states
    basis = create2([list_], pos, n)
    N = len(basis)
    
    # Initialize sparse Hamiltonian matrix
    H = lil_matrix((N, N), dtype=np.float64)
    
    # Diagonal elements
    for i in range(N):
        st = basis[i]
        diag_term = Jz / 4 * np.dot(
            2 * np.array([bitget(st, nn[j, 0] - 1) for j in range(nn.shape[0])]) - 1,
            2 * np.array([bitget(st, nn[j, 1] - 1) for j in range(nn.shape[0])]) - 1
        )
        H[i, i] = diag_term
    
    # Off-diagonal elements
    for i in range(N):
        for k in range(nn.shape[0]):
            l = nn[k, 0]
            m = nn[k, 1]
            bitl = bitget(basis[i], l - 1)
            bitm = bitget(basis[i], m - 1)
            
            if bitl != bitm:
                # Swap bits at positions l and m
                state = bitset(basis[i], l - 1, bitm)
                state = bitset(state, m - 1, bitl)
                
                # Find the index of the new state in the basis
                y = such(basis, state, 0, N - 1)
                H[y, i] += Jp / 2
    
    return H.tocsr(), basis


def bitget(num, pos):
    """
    Get the bit at a specific position.
    """
    return (num >> pos) & 1


def bitset(num, pos, value):
    """
    Set the bit at a specific position to a given value.
    """
    if value:
        return num | (1 << pos)
    else:
        return num & ~(1 << pos)


def such(basis, state, low, high):
    """
    Perform binary search to find the index of `state` in `basis`.
    """
    while low <= high:
        mid = (low + high) // 2
        if basis[mid] == state:
            return mid
        elif basis[mid] < state:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError(f"State {state} not found in basis.")


def tabcoord(Nx, Ny, flag):
    """
    Generate lattice and nearest neighbor table.
    """
    lattice = np.arange(1, Nx * Ny + 1).reshape(Nx, Ny)
    nn = []
    for x in range(Nx):
        for y in range(Ny):
            site = lattice[x, y]
            neighbors = []
            if x > 0:  # Up
                neighbors.append(lattice[x - 1, y])
            if x < Nx - 1:  # Down
                neighbors.append(lattice[x + 1, y])
            if y > 0:  # Left
                neighbors.append(lattice[x, y - 1])
            if y < Ny - 1:  # Right
                neighbors.append(lattice[x, y + 1])
            for neighbor in neighbors:
                nn.append((site, neighbor))
    return lattice, np.array(nn)


def create2(lst, pos, n):
    """
    Generate all valid bit patterns for the basis.
    """
    i = n
    temp = lst.copy()

    while pos[-1] > n:
        if pos[i - 1] > i:
            h = 0
            while pos[i - 1] - h - 1 >= 0 and (temp[0] >> (pos[i - 1] - h - 1)) & 1 == 0:
                h += 1
            if h != 0:
                i -= h
            else:
                while pos[i - 1] > i and ((temp[0] >> (pos[i - 1] - 1)) & 1) != 0:
                    temp[0] |= (1 << (pos[i - 1] - 1))
                    temp[0] &= ~(1 << (pos[i - 1] - 2))
                    lst.append(temp[0])
                    pos[i - 1] -= 1
        elif i < n:
            for k in range(1, i + 1):
                temp[0] |= (1 << (k - 1))
            for k in range(1, i + 1):
                if pos[i] - 2 - i + k - 1 >= 0:
                    temp[0] &= ~(1 << (pos[i] - 2 - i + k - 1))
                    pos[k - 1] = pos[i] - 2 - i + k
            i += 1

    return lst



H, base = matelem(1,1,1,2,2)
print(H)
print(base)
import matplotlib.pyplot as plt
plt.matshow(H)
plt.show()