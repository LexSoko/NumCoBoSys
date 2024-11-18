import numpy as np

def tabcoord(Nx, Ny, periodic):
    """
    Generate lattice coordinates and nearest neighbor (nn) pairs.

    Parameters:
        Nx, Ny: Dimensions of the lattice.
        periodic: Whether the lattice is periodic (1 for periodic, 0 otherwise).

    Returns:
        lattice: Lattice coordinates as an Nx2 array.
        nn: Nearest neighbor pairs as an array of shape (num_pairs, 2).
    """
    N = Nx * Ny
    lattice = np.zeros((N, 2), dtype=int)

    einsx = np.ones(Nx, dtype=int)
    einsy = np.ones(Ny, dtype=int)
    xvek = np.arange(1, Nx + 1)
    yvek = np.arange(1, Ny + 1)

    lattice[:, 0] = np.tile(xvek, Ny)
    lattice[:, 1] = np.repeat(yvek, Nx)

    nn = []
    if not periodic:
        for n in range(Ny):
            for m in range(Nx):
                if m < Nx - 1:
                    nn.append([(n * Nx) + m + 1, (n * Nx) + m + 2])
                if n < Ny - 1:
                    nn.append([(n * Nx) + m + 1, ((n + 1) * Nx) + m + 1])
    elif Ny > 1:
        for n in range(Ny):
            for m in range(Nx):
                nn.append([(n * Nx) + m + 1, (n * Nx) + (m + 1) % Nx + 1])
                nn.append([(n * Nx) + m + 1, ((n + 1) % Ny * Nx) + m + 1])
    else:
        for m in range(Nx):
            nn.append([m + 1, (m + 1) % Nx + 1])

    return lattice, np.array(nn)
