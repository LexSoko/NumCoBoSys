import numpy as np 
def create2(lst, pos, n):
    i = n
    temp = np.copy(lst)

    # Ensure i remains valid and within the bounds of `pos`
    while i > 0 and pos[n - 1] > n:
        if pos[i - 1] > i:
            h = 0
            while pos[i - 1] - h - 1 >= 0 and (temp >> (pos[i - 1] - h - 1)) & 1 == 0:
                h += 1

            if h != 0:
                i = i - h
            else:
                while pos[i - 1] > i and ((temp >> (pos[i - 1] - 1)) & 1) != 0:
                    temp = temp | (1 << (pos[i - 1] - 1))  # Set bit at pos[i-1] - 1
                    temp = temp & ~(1 << (pos[i - 1] - 2))  # Clear bit at pos[i-1] - 2
                    lst.append(temp)
                    pos[i - 1] -= 1
        elif i < n:
            for k in range(1, i + 1):
                temp = temp | (1 << (k - 1))  # Set bit at position k-1
            for k in range(1, i + 1):
                if pos[i] - 2 - i + k - 1 >= 0:  # Ensure valid index
                    temp = temp & ~(1 << (pos[i] - 2 - i + k - 1))  # Clear bit
                    pos[k - 1] = pos[i] - 2 - i + k
            i += 1
    print("lst", lst)
    return lst
