import numpy as np


def strToNp(str):
    rows = str.replace("[", "").replace("]", "").split("\n")

    rows = list(filter(lambda x: x.strip() != "", rows))

    np_arr = np.vstack([np.fromstring(row, sep=" ") for row in rows])

    return np_arr
