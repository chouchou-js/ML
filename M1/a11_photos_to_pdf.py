import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# 파일 탐색
def search_files(path):
    for root, _, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file).replace('\\', '/')
            yield file_name


def gather_data(data_dir):
    return [plt.imread(f) for f in search_files(data_dir)]


if __name__ == '__main__':
    data_directory = '../data'
    arr = gather_data(f'{data_directory}/photo')

    # 사진 개수 초과 수정중
    row, col = 3, 3
    pics = row * col
    with PdfPages(f'{data_directory}/wrong_photos.pdf') as pdf:
        idx = 0
        for _ in range(len(arr) // pics):
            fig, ax = plt.subplots(nrows=row, ncols=col)
            fig.tight_layout()
            for axi in ax.flat:
                axi.imshow(arr[idx])
                axi.axis('off')
                idx += 1
            pdf.savefig()
            plt.close()
