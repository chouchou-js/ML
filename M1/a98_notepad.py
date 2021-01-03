import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x = np.arange(1, 100)
y = x
z = x*x
arr = [y, z, y, z, z, z, y, z, z]

row, col = 2, 2
pics = row * col
with PdfPages('multi_page_pdf.pdf') as pdf:
    idx = 0
    for _ in range(len(arr) // pics):
        _fig, ax = plt.subplots(nrows=row, ncols=col)
        for axi in ax.flat:
            axi.set_title(idx)
            axi.plot(x, arr[idx])
            idx += 1
        pdf.savefig()
        plt.close()
