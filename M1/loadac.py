import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x = np.arange(1, 100)
y = x
z = x*x
arr = [y, z, y, z, z, z, y, z]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for idx in range(0, len(lst), n):
        yield lst[idx:idx + n]


row, col = 2, 2
pics = row * col
with PdfPages('multi_page_chunk.pdf') as pdf:
    for i, f in enumerate(chunks(arr, pics)):
        _fig, ax = plt.subplots(nrows=row, ncols=col)
        for j, axi in enumerate(ax.flat):
            axi.set_title(i*pics+j)
            axi.plot(x, f[j])
        pdf.savefig()
        plt.close()
